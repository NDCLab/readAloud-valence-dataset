# Reading in reconciled Excels, summarizing the errors of each, and writing that
# to a new CSV
#
# Luc Sahar and Jessica M. Alexander -- NDCLab, Florida International University
# last updated 6/11/23

# NB passages "sun" and "broccoli" as coded contain errors. Namely, broccoli had
# "iodized _table_ counteracts" instead of the intended "table salt", and sun
# showed participants "_empower_ individuals" whereas it was coded as "enable"

DEBUG_MODE = TRUE

library(readxl) # read_xlsx
library(stringr) # str_extract
library(dplyr) # most things
library(purrr) # map, map_df; generally good to have
library(lubridate) # now
library(readr) # write_csv


error_types_idiomatic = c(
  "misprod", "ins_dup", "omit", "word_stress",
  "filled_pause", "hesitation", "elongation", "corrected"
)

folder_regex_default = "sub-\\d{6}_reconciled"
ext_default = 'csv'
tz_default = "America/New_York"
date_format_default = "%Y%m%d_%I%M%P"

# if we're in debug mode, write output dataframes to disk as they are made
incremental_writeout = if(DEBUG_MODE) "incremental-passages_debugging" else NULL

if(DEBUG_MODE && !fs::is_dir(incremental_writeout))
  stop(
    paste("Intended debugging CSV directory (", incremental_writeout, ") not found. Try creating it?", sep = ""))

filler = data.frame( # what we'll use when data is empty or invalid, until the files are manually fixed
  logical(7), # FALSE 7 times
  row.names = error_types_idiomatic[1:7] # misprod...elongation
) %>% t %>% as.data.frame

dummy <- function(.) NA # ignore argument, just return dummy value
fill_dummy <- function(df, cols) cbind(df, setNames(lapply(cols, dummy), cols)) # fill dummy value into all listed cols

## Calculations about the passages themselves, for things like word ratios
# base = "~/Documents/ndclab/analysis-sandbox/github-structure-mirror/readAloud-valence-dataset"
base = "/home/data/NDClab/datasets/readAloud-valence-dataset"
scaffolds_path = paste(base, "code/scaffolds.xlsx", sep = '/')
titles = excel_sheets(scaffolds_path) # antarctica ... vegas

into_dict <- function(sequence, f, env = new.env()) {
  map(sequence, \(x) env[[x]] = f(x)) # fill a dictionary that maps x -> f(x)
  return(env)
}

tally_up <- function(df, col) # how many unique values in col?
  df[[col]] %>% unique %>% length

scaffolds       = into_dict(titles, \(x) read_xlsx(scaffolds_path, sheet = x)) # syntax: scaffolds[[passage_name]]   -> scaffold df for that passage
word_counts     = into_dict(titles, \(x) tally_up(scaffolds[[x]], "word_id"))  # syntax: word_counts[[passage_name]] -> number of words in that passage
syllable_counts = into_dict(titles, \(x) tally_up(scaffolds[[x]], "syllable_id"))


## Now: logic to read in the error passage XLSXes
build_participant_dirname <- function(dir_root, participant_id) # github_root, 150077 -> "/home/[...]/sub-150077/sub-150077_reconciled"
  paste(sep = "",
    dir_root,
    '/sub-', participant_id,
    '/sub-', participant_id, '_reconciled')

build_full_passage_path <- function(dir_root, participant_id, passage_name)
  paste(sep = "",
    build_participant_dirname(dir_root, participant_id),
    '/', 
    passage_name)

raw_readxl_to_df <- function(raw_passage_matrix) {
  df = data.frame(
    raw_passage_matrix[2:9,], # get only the rows misprod ... corrected
    row.names = error_types_idiomatic
  ) %>% t
  
  return(df[-1,] %>% # ignore the original titles
           as.data.frame) # and convert back to a dataframe
}

passage_name_to_df <- function(passage_name, participant_id, dir_root)
  build_full_passage_path(dir_root, participant_id, passage_name) %>%
    read_xlsx %>%
    raw_readxl_to_df


## Counting up totals for a given passage
get_rows_with_a_one <- function(df) filter(df, if_any(everything(), ~ . == 1))

complain_when_invalid <- function(passage_df, participant_id, passage_name) {
  report = paste("\n\t\t<< ERROR REPORT", participant_id, "-", passage_name, ">>")
  
  any_empty = sum(is.na(passage_df)) != 0
  if (any_empty) {
    message(report); message("Empty value (NA) in the dataframe!\n")
    return(filler) # 7 values of FALSE
  }
  
  any_invalid = any(passage_df !=0 & passage_df != 1)
  if(any_invalid) {
    message(report); message("Invalid value (neither 1 nor 0) in the dataframe!\n")
    return(filler) # 7 values of FALSE
  }

  return(passage_df)
}

count_errors_by_type <- function(passage_df)
  passage_df %>% select(misprod:elongation) %>% map_df(as.numeric) %>% colSums

count_error_syllables_any_type <- function(passage_df) # grand total, across types
  passage_df %>%
    select(misprod:elongation) %>% # only the error columns
    get_rows_with_a_one %>% # only the rows that have an error somewhere
    nrow # count them

count_corrected_error_syllables <- function(passage_df)
  passage_df %>% 
    filter(corrected == 1) %>% # only get corrected rows
    select(misprod:elongation) %>% # now let's only look at their error columns
    get_rows_with_a_one %>% # only the rows that have an error somewhere
    nrow

count_uncorrected_error_syllables <- function(passage_df)
  passage_df %>% 
    filter(corrected == 0) %>% # only get uncorrected ones
    select(misprod:elongation) %>% # now let's only look at their error columns
    get_rows_with_a_one %>% # only the rows that have an error somewhere
    nrow

count_distinct <- function(passage_df, passage_scaffold, error_type)
  # Distinct if they don't touch. But if they're in separate words, they can touch.
  cbind(passage_scaffold, passage_df) %>% # align scaffold info with annotated syllables
    filter({{error_type}} == 1 & (wordOnset == 1 | lag({{error_type}}) != 1)) %>% # an error that's (a) word-initial or (b) *not* preceded by an adjacent one
    nrow

count_distinct_across_words <- function(passage_df, passage_scaffold, error_type)
  # Even if they're in different words, they can't touch
  cbind(passage_scaffold, passage_df) %>%
    filter({{error_type}} == 1 & lag({{error_type}}) != 1) %>% # it's an error and the syllable before it isn't
    nrow

last_n_rows_are <- function(df, col, n, val) all(df[[col]] %>% tail(n) == val)

error_streak_lengths <- function(passage_df) {
  streak_lengths_for_error_type = compose(
    rle, # streaks of repeat values
    as.list.data.frame, # as lists
    as.data.frame, # as df: lengths and values
    \(df) filter(df, values == 1)$lengths, # lengths of the error streaks only
    .dir = "forward"
  )
  map(passage_df, streak_lengths_for_error_type) # do this for each error type
}

tally_repeat_errors_beyond_length_n <- function(error_streaks_df, error_type, n) {
  # first get each sequence of at least n errors of the same type in a row:
  streaks = error_streaks_df[[{{error_type}}]] %>% keep(\(x) x >= n)
  sum(streaks) - length(streaks) # ignore errors beyond the first in each streak; this gets the overcount
}

count_without_sequences_beyond_length_n <- function(summary_df, error_streaks_df, error_type, n) {
  summary_df[[{{error_type}}]] - # raw count
    tally_repeat_errors_beyond_length_n(error_streaks_df, {{error_type}}, n) # minus excess count
}


colnames_from_range <- function(df, colrange)
  colnames(select(df, {{colrange}}))

append_lookback <- function(df, col, lookback_index)
  # Add a new column (e.g. prev_misprod4) representing the value of e.g. misprod, four rows prior.
  # This is useful for hunting for patterns of errors in a particular sequence
  mutate(df,
         "prev_{col}{lookback_index}" := lag(df[[col]], n = lookback_index))

append_lookback_multicol <- function(df, colrange, loopback_index) {
  # for every column in passed range, create a new column looking back at the indexth row for that column
  col_list = colnames_from_range(df, {{colrange}})

  reduce(col_list,
      \(df_acc, colname) append_lookback(df_acc, {{colname}}, loopback_index),
      .init = df)
}

append_lookbacks_multicol <- function(df, colrange, lookback_count)
  # Use append_lookback_multicol successively on the same df, on each index from 1..lookback_count
  # Ex: col=hesitation, lookback_count=3 will add a column for hesitations three rows prior, 
  # another for hesitations two rows prior, and another for hesitations one row prior
  reduce(1:lookback_count,
         partial(append_lookback_multicol, colrange = {{colrange}}),
         .init = df)


a_b_sequence_multicol <- function(df, errtypes_a, errtypes_b, prior_context = 1) {   
  # a: LHS errors; b: RHS errors; context: how many rows back we can look for LHS errors

  lhs_cols = colnames_from_range(df, {{errtypes_a}})
  rhs_cols = colnames_from_range(df, {{errtypes_b}})
  
  lookbacks_regex = lhs_cols %>% paste(collapse = "|") %>% paste("prev_(", ., ").*", sep = "") # as in prev_(misprod|hesitation).*

  df_with_lhs_lookbacks = append_lookbacks_multicol(df, {{errtypes_a}}, prior_context)
  
  
  filter(df_with_lhs_lookbacks,
         if_any(rhs_cols, ~ . == 1) & if_any(matches(lookbacks_regex), ~ . == 1))
}

count_a_b_sequence_multicol <- function(df, errtypes_a, errtypes_b, prior_context = 1)
  a_b_sequence_multicol(df, {{errtypes_a}}, {{errtypes_b}}, prior_context) %>% nrow


error_summary <- function(passage_df, passage_name) {
  # a quick repair instead instead of an error: so we don't have to halt everything and start over
  if (any(passage_df == FALSE)) {
    return(passage_df %>% fill_dummy(c("errors", "corrections", "uncorrected_errors", "skipped_end")))
  }

  summary <- count_errors_by_type(passage_df)
  streaks <- error_streak_lengths(passage_df)
  return(summary %>% cbind(
    distinct_misprod     = count_distinct(passage_df, scaffolds[[passage_name]], misprod),
    distinct_ins_dup     = count_without_sequences_beyond_length_n(summary, streaks, "ins_dup", n = 6),
    distinct_word_stress = count_distinct(passage_df, scaffolds[[passage_name]], word_stress),
    distinct_hesitation  = count_distinct_across_words(passage_df, scaffolds[[passage_name]], hesitation),

    hes_after_misprod    = count_a_b_sequence_multicol(passage_df, misprod, hesitation, prior_context = 4),
    hes_after_err        = count_a_b_sequence_multicol(passage_df, misprod:word_stress, hesitation, prior_context = 4), # all the error types not associated with speed or fluency
    elong_after_misprod  = count_a_b_sequence_multicol(passage_df, misprod, elongation, prior_context = 4),
    elong_after_err      = count_a_b_sequence_multicol(passage_df, misprod:word_stress, elongation, prior_context = 4), # all the error types not associated with speed or fluency
    hes_after_elong      = count_a_b_sequence_multicol(passage_df, elongation, hesitation),
    elong_after_hes      = count_a_b_sequence_multicol(passage_df, hesitation, elongation), # FIXME: it would be nice to generate all these at once

    errors               = count_error_syllables_any_type(passage_df),
    corrections          = count_corrected_error_syllables(passage_df),
    uncorrected_errors   = count_uncorrected_error_syllables(passage_df),
    skipped_end          = last_n_rows_are(passage_df, "omit", n = 10, val = 1)
  ))
}


status_message <- function(passage_name, participant_id) {
  status = paste("Generating summary from participant ", participant_id, "'s ", 
                 passage_name, " passage...",
                 sep = '')
  message(status)
}

append_per_syllable_rates <- function(error_df, count) {
  mutate(error_df, across(misprod:uncorrected_errors, \(x) x / count, .names = "{.col}_rate"))
}

error_summary_with_metadata <- function(passage_name, participant_id, dir_root) {
  passage_nickname = fs::path_ext_remove(passage_name) # chomp 'bees.xlsx' to 'bees', e.g.
  if(DEBUG_MODE) status_message(passage_nickname, participant_id)

  summary = 
    passage_name_to_df(passage_name, participant_id, dir_root) %>%
    complain_when_invalid(participant_id, passage_name) %>%
    error_summary(passage_nickname) %>%
    append_per_syllable_rates(syllable_counts[[passage_nickname]]) # then errors per syllable- TODO change to per word?
  
  return(cbind(
    id = participant_id, # pre-pose an id column
    passage = passage_nickname, # then a passage column
    summary
  ))
}


# all passages for a participant
generate_summary_for_each_passage_with_metadata <- function(dir_root, participant_id, write_to = incremental_writeout, date_format = date_format_default) {
  df = build_participant_dirname(dir_root, participant_id) %>% dir %>% # passage name _with_ the extension
      map_df(error_summary_with_metadata, participant_id, dir_root)

  if (!is.null(write_to) && fs::is_dir(write_to)) { # incremental CSV: just this participant, with all their passages
    outfile_debug = paste(write_to, "/", participant_id, "_", now() %>% format(date_format), '.csv', sep = "")
    write_csv(df, outfile_debug)
  }

  return(df)
}

# Now, for each participant under a directory, each identified by the form sub_XXXXXX_reconciled,
# call generate_summary_for_each_passage_with_metadata(the_parentdir_of_all_those, that_id)

find_participant_id_from_dirname <- function(dirname) # "sub-150077/sub-150077_reconciled" -> "150077"
  str_extract(dirname, "\\d+")

summarize_numeric_cols <- function(df, f, label = as.character(substitute(f)))
  cbind(id = label, reframe(df, across(where(is.numeric), f)))

append_summary_stats <- function(df)
  bind_rows(df, summarize_numeric_cols(df, mean), summarize_numeric_cols(df, sd))

summarize_errors_in_subdirectories <- function(dir_root, subfolder_match)
  dir_root %>%
    dir(include.dirs = TRUE, recursive = TRUE, pattern = subfolder_match) %>% # walk the directory
    map(find_participant_id_from_dirname) %>% # split it up: sub-150079_reconciled -> 150079
    map_df(generate_summary_for_each_passage_with_metadata, dir_root = dir_root) %>% # summarize all spreadsheets for that participant, for each participant
    append_summary_stats # add rows for mean and standard deviation

# we've matched subfolders by explicitly returning directories (include.dirs = 
# TRUE) and recursing (recursive = TRUE), thus catching -"_reconciled" subfolders

# Now finally: write all our results to a file (a CSV)

build_output_filename <- function(label, ext = ext_default, timezone = tz_default, date_format = date_format_default) {
  # `label` may include the destination directory, if different from the working directory when the script is run  
  current_datetime <- now(timezone) %>% format(date_format) # e.g. 20230520_1240pm

  paste(
    label, '_', current_datetime,
    '.', ext,
    sep = ""
  )
}

compute_summary_and_write_to_file <- function(dir_root, label, ext = ext_default, timezone = tz_default, 
                                              date_format = date_format_default, subfolder_match = folder_regex_default)
{
  outpath_name <- build_output_filename(label, ext, timezone, date_format)
  summary_df <- summarize_errors_in_subdirectories(dir_root, subfolder_match)
  
  write_csv(summary_df, outpath_name)
  return(outpath_name)
}

annotations_base = paste(base, "derivatives/preprocessed", sep = '/')
github_root = paste(annotations_base, "error-coding", sep = '/')
outname_base = paste(annotations_base, "disfluencies_subject-x-passage", sep = '/')
compute_summary_and_write_to_file(github_root, outname_base)
