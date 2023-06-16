# Reading in reconciled Excels, summarizing the errors of each, and writing that
# to a new CSV
# Luc Sahar and Jessica M. Alexander -- NDCLab, Florida International University
# last updated 2023-06-13

# NB passages "sun" and "broccoli" as coded contain errors. Namely, broccoli had
# "iodized _table_ counteracts" instead of the intended "table salt", and sun
# showed participants "_empower_ individuals" whereas it was coded as "enable"

### --- IO information --- ###
##  INPUTS
#     This script relies on two external stateful components:
#       - scaffolds
#       - passage annotations
#
#     Scaffolds are stored in an Excel file with one sheet per passage. Each
#     sheet contains a list of each syllable and a list of each word, aligned
#     such that it is apparent which syllables belong to which word.
#
#     For our purposes, this is important for calculating word-level errors (as
#     in "word stress errors", which we have considered to be errors that affect
#     whole words rather than individual errors), for determining whether errors
#     marked on adjacent syllables constitute discrete errors or just one error
#     (as in misproductions, which we here consider to be discrete when they
#     don't touch or when they touch at a word boundary, but not when they touch
#     inside a word), and for calculating rates of errors per syllable or per
#     word (the scaffolds make it simple to count the words or syllables that
#     each passage has).
#
#     Each passage annotation is a single Excel file consisting of rows with the
#     error types and two header rows---one for the passage's words, and another
#     below it for the passage's syllables. Below that, each cell thus
#     represents the presence or absence of an error of a particular type on a
#     particular syllable in the text. Because we're interested in calculations
#     by error type, we will transpose each annotation once it is read into a
#     dataframe, such that its columns are the error types and its rows are the
#     syllables.
#
#
##  PARAMETERS
#     This script uses a couple of repeat conventions. Hopefully it is as clear
#     and consistent as intended. Some clarifications:
#       -  path: a fully specified filesystem path to a file
#       -  dir: likewise, but for a directory (folder)
#       - "name": often used to distinguish whether we're talking about the text
#                 label -- the string identifying a file -- rather than the file
#                 itself or its contents
#       - df: dataframe, the R structure
#       - DEBUG_MODE: a 'flag' which when set to TRUE enables features including
#                 increased verbosity and incremental outputs (in case the
#                 program fails before creating the intended file per below)
#       - incremental_writeout: the name of the directory to which incremental
#                 outputs will periodically be saved in debug mode
#       - error_types_idiomatic: R-/dataframe- friendly names of the error types
#       - dict: a dictionary, used here for storing the scaffolds, the word
#               counts per passage, and the syllable counts per passage. This
#               prevents this from having to be recomputed for >1000 passages.
#               This is implemented as a new environment, but the idea of a
#               dictionary is familiar and the syntax of accessing an `env` in
#               R is similar to that of dictionaries in languages like Python.
#               Another option would be memoizing the function.
#       - lookbacks: columns appended to a df representing, at each row, the
#               value of some other column X rows back. This appears to be the
#               best way to perform sophisticated comparisons across errors over
#               a range of previous syllables.
#               For example, we might want to look for all misproductions,
#               insertions, and omissions occurring within four syllables of a
#               following hesitation or elongation---one way we might want to
#               look for potential cases of post-error slowing.
#
#     Everything else is intended to be as simple and self-explanatory as
#     possible. The spirit of the style is to have functions that are modular,
#     digestible, and whose titles are informative enough that reading the body
#     is typically unnecessary. Ideally, this makes code easier to understand
#     and to maintain.
#
#
##  OUTPUT
#     This script, when debug mode is not turned on (see above), writes only one
#     file: a massive CSV containing one row per participant per passage (there
#     are 20 rows per participant, assuming they read all passages).
#     Specific directories (rather than parameter names) are named with "base";
#     this was arbitrary.
#
#     That CSV is written to `outpath`, which is currently the concatenation of
#     the annotations root directory `annotations_base`, a somewhat useful
#     file name prefix (`label`), the current date and time (`timestamp`), and
#     the file extension '.csv'.
#
#     That file name is the last value returned if the script has run through in
#     its entirety. Other information is emitted by R along the way, along with
#     some other status updates when debug mode is turned on.
##
### --- IO information --- ###

DEBUG_MODE = FALSE

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
timestamp = now("America/New_York") %>% format("%Y%m%d_%I%M%P")
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

errcols <- function(passage_df) select(passage_df, misprod:elongation)

count_errors_by_type <- function(passage_df)
  errcols(passage_df) %>% map_df(as.numeric) %>% colSums %>% t %>% as.data.frame

count_error_syllables_any_type <- function(passage_df) # grand total, across types
  passage_df %>%
    errcols %>% # only the error columns
    get_rows_with_a_one %>% # only the rows that have an error somewhere
    nrow # count them

count_corrected_error_syllables <- function(passage_df)
  passage_df %>%
    filter(corrected == 1) %>% # only get corrected rows
    errcols %>% # now let's only look at their error columns
    get_rows_with_a_one %>% # only the rows that have an error somewhere
    nrow

count_uncorrected_error_syllables <- function(passage_df)
  passage_df %>%
    filter(corrected == 0) %>% # only get uncorrected ones
    errcols %>% # now let's only look at their error columns
    get_rows_with_a_one %>% # only the rows that have an error somewhere
    nrow

count_distinct <- function(passage_df, passage_scaffold, error_type)
  # Distinct if they don't touch. But if they're in separate words, they can touch.
  cbind(passage_scaffold, passage_df) %>% # align scaffold info with annotated syllables
    filter({{error_type}} == 1 & (wordOnset == 1 | lag({{error_type}}) != 1)) %>% # an error that's (a) a new word or (b) *not* preceded by an adjacent error
    nrow

count_distinct_across_words <- function(passage_df, passage_scaffold, error_type)
  # Even if they're in different words, they can't touch
  cbind(passage_scaffold, passage_df) %>%
    filter({{error_type}} == 1 & lag({{error_type}}) != 1) %>% # it's an error and the syllable before it isn't
    nrow

drop_first_syllable <- function(df) slice(df, -1)

drop_until_next_word <- function(df) {
  df = drop_first_syllable(df) # we don't care about this row we've already compared to

  first_word_onset = match(1, df$wordOnset, nomatch = 0) # first matching index, else 0
  end_index        = ifelse(first_word_onset == 0, 0, nrow(df)) # the actual end, unless there's no more new words left to check

  return(df[first_word_onset:end_index,])
}

count_errors_by_word <- function(df, error_type, acc = 0) { # -> int
  if(nrow(df) == 0) return(acc) # stop: we're at the end of the passage
  err_on_current_syllable = df[1,] %>% select({{error_type}})

  if(err_on_current_syllable == 1) { # this syllable has this error!
    acc = acc + 1                    # therefore another word (this one) has this error!
    rest = drop_until_next_word(df)  # so we skip ahead to the next word
  } else {
    rest = drop_first_syllable(df)   # otherwise, no skipping - we just move on to the next syllable
  }

  # now recurse on rest of passage, with potentially increased accumulator
  return(count_errors_by_word(rest, {{error_type}}, acc))
}


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


a_b_sequence <- function(df, errtypes_a, errtypes_b, prior_context = 1) {
  # a: LHS errors; b: RHS errors; context: how many rows back we can look for LHS errors

  lhs_cols = colnames_from_range(df, {{errtypes_a}})
  rhs_cols = colnames_from_range(df, {{errtypes_b}})

  lookbacks_regex = lhs_cols %>% paste(collapse = "|") %>% paste("prev_(", ., ").*", sep = "") # as in prev_(misprod|hesitation).*

  df_with_lhs_lookbacks = append_lookbacks_multicol(df, {{errtypes_a}}, prior_context)


  filter(df_with_lhs_lookbacks,
         if_any(rhs_cols, ~ . == 1) & if_any(matches(lookbacks_regex), ~ . == 1))
}

count_a_b_sequences <- function(df, errtypes_a, errtypes_b, prior_context = 1)
  a_b_sequence(df, {{errtypes_a}}, {{errtypes_b}}, prior_context) %>% nrow


error_summary <- function(passage_df, passage_name) {
  # a quick repair instead instead of an error: so we don't have to halt everything and start over
  if (any(passage_df == FALSE)) {
    return(passage_df %>% fill_dummy(c("errors", "corrections", "uncorrected_errors", "skipped_end")))
  }

  summary <- count_errors_by_type(passage_df)
  streaks <- error_streak_lengths(passage_df)
  passage_x_scaffold <- cbind(scaffolds[[passage_name]], passage_df)
  return(summary %>% cbind(
    words_with_misprod   = count_errors_by_word(passage_x_scaffold, misprod),
    # distinct_ins_dup     = count_without_sequences_beyond_length_n(summary, streaks, "ins_dup", n = 6),
    # distinct_word_stress = count_distinct(passage_df, scaffolds[[passage_name]], word_stress),
    words_with_hes       = count_errors_by_word(passage_x_scaffold, hesitation),

    hes_after_misprod    = count_a_b_sequences(passage_df, misprod, hesitation, prior_context = 4),
    hes_after_err        = count_a_b_sequences(passage_df, misprod:word_stress, hesitation, prior_context = 4), # all the error types not associated with speed or fluency
    elong_after_misprod  = count_a_b_sequences(passage_df, misprod, elongation, prior_context = 4),
    elong_after_err      = count_a_b_sequences(passage_df, misprod:word_stress, elongation, prior_context = 4), # all the error types not associated with speed or fluency
    hes_after_elong      = count_a_b_sequences(passage_df, elongation, hesitation),
    elong_after_hes      = count_a_b_sequences(passage_df, hesitation, elongation), # FIXME: it would be nice to generate all these at once

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

append_rates <- function(error_df, colrange, count) {
  mutate(error_df, across({{colrange}}, \(x) x / count, .names = "{.col}_rate"))
}

error_summary_with_metadata <- function(passage_name, participant_id, dir_root) {
  passage_nickname = fs::path_ext_remove(passage_name) # chomp 'bees.xlsx' to 'bees', e.g.
  if(DEBUG_MODE) status_message(passage_nickname, participant_id)

  summary =
    passage_name_to_df(passage_name, participant_id, dir_root) %>%
    complain_when_invalid(participant_id, passage_name) %>%
    error_summary(passage_nickname) %>%
    append_rates(misprod:elongation, syllable_counts[[passage_nickname]]) %>% # then errors per syllable
    append_rates(starts_with("words_with"), word_counts[[passage_nickname]])  # then errors per word, where applicable

  return(cbind(
    id = participant_id, # pre-pose an id column
    passage = passage_nickname, # then a passage column
    summary
  ))
}


# All passages for a participant
generate_summary_for_each_passage_with_metadata <- function(dir_root, participant_id, write_to = incremental_writeout) {
  df = build_participant_dirname(dir_root, participant_id) %>% dir %>% # passage name _with_ the extension
      map_df(error_summary_with_metadata, participant_id, dir_root)

  if (!is.null(write_to) && fs::is_dir(write_to)) { # incremental CSV: just this participant, with all their passages
    outfile_debug = paste(write_to, "/", participant_id, "_", timestamp, '.csv', sep = "")
    write_csv(df, outfile_debug)
  }

  return(df)
}

summarize_numeric_cols <- function(df, f, label = as.character(substitute(f))) # currently unused- previously in function below with mean and sd
  cbind(id = label, reframe(df, across(where(is.numeric), f)))

# Now, for each participant under a directory, each identified by the form sub_XXXXXX_reconciled,
# call generate_summary_for_each_passage_with_metadata(the_parentdir_of_all_those, that_id)
summarize_errors_in_subdirectories <- function(dir_root, subfolder_match)
  dir_root %>%
    dir(include.dirs = TRUE, recursive = TRUE, pattern = subfolder_match) %>% # walk the directory
    map(\(dir) str_extract(dir,  "\\d+")) %>% # split them up: sub-150079_reconciled -> 150079
    map_df(generate_summary_for_each_passage_with_metadata, dir_root = dir_root) # summarize all spreadsheets for that participant, for each participant

# we've matched subfolders by explicitly returning directories (include.dirs =
# TRUE) and recursing (recursive = TRUE), thus catching -"_reconciled" subfolders

## Now finally: write all our results to a file (a CSV)
annotations_base = paste(base, "derivatives/preprocessed", sep = '/')
github_root = paste(annotations_base, "error-coding", sep = '/')

label = "disfluencies_subject-x-passage_"

outpath <- paste(sep = "", annotations_base, '/', label, timestamp, ".csv")
# e.g. "./some/path/disfluencies_20230520_1240pm.csv"

github_root %>%
  summarize_errors_in_subdirectories("^sub-\\d{6}_reconciled$") %>%
  write_csv(outpath)

print(outpath)
