# Reading in reconciled Excels, summarizing the errors of each, and writing that
# to a new CSV
#
# Luc Sahar and Jessica M. Alexander -- NDCLab, Florida International University
# last updated 5/31/23

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
  "misprod", 
  "ins_dup", 
  "omit", 
  "word_stress", 
  "filled_pause", 
  "hesitation", 
  "elongation",
  "corrected"
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


# Calculations about the very passages themselves, for things like word ratios
# base = "~/Documents/ndclab/analysis-sandbox/github-structure-mirror/readAloud-valence-dataset"
base = "/home/data/NDClab/datasets/readAloud-valence-dataset"



read_all_sheets <- function(excel_path) {
  sheet_names = excel_sheets(excel_path)
  read_sheet = function(sheet_name) { read_xlsx(excel_path, sheet = sheet_name)}
  
  map_df(sheet_names, read_sheet)
}

scaffolds_path = paste(base, "code/scaffolds.xlsx", sep = '/')
scaffolds <- read_all_sheets(scaffolds_path)
# problem: there's an empty cell in the dams sheet

word_counts <- scaffolds %>% group_by(passage) %>% summarize(across(wordOnset, sum))
syllable_counts <- scaffolds %>% group_by(passage) %>% summarize(across(syllable_id, length))

word_count <- function(passage_name) { filter(word_counts, passage == passage_name)$wordOnset }
syllable_count <- function(passage_name) { filter(syllable_counts, passage == passage_name)$syllable_id }
# FIXME: don't use passage as a column, use it as the row name
# then use a dataframe with the columns "word_count" and "syllable_count"
# TODO


## Read in XLSXes as arguments

build_participant_dirname <- function(dir_root, participant_id) {
  paste(
    dir_root,
    '/sub-', participant_id,
    '/sub-', participant_id, '_reconciled',
    sep = ""
  )
}
# > build_participant_dirname(github_root, 150077)
# [1] "/home/[...]/preprocessed/error-coding/sub-150077/sub-150077_reconciled"

build_full_passage_path <- function(dir_root, participant_id, passage_name) {
  paste(
    build_participant_dirname(dir_root, participant_id),
    '/', 
    passage_name,
    sep = ""
  )
}

read_in <- function(passage_name, participant_id, dir_root) {
  read_xlsx(
    build_full_passage_path(dir_root, participant_id, passage_name)
  )
}


## transform to a dataframe
raw_readxl_to_df <- function(raw_passage_matrix) {
  df = data.frame(
    raw_passage_matrix[2:9,], # get only the rows misprod ... corrected
    row.names = error_types_idiomatic
  ) %>% t
  
  return(df[-1,] %>% # ignore the original titles
           as.data.frame) # and convert back to a dataframe
}

passage_name_to_df <- function(passage_name, participant_id, dir_root) {
  passage <- read_in(passage_name, participant_id, dir_root)
  
  return(raw_readxl_to_df(passage))
}

## Count up totals per error type for a given passage

ones <- function(row){ which(row == 1) } # for a given error type, which cells are marked?
count_errors <- function(row){ length(ones(row)) } # for a given error type, how many cells are marked?

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

count_errors_by_type <- function(passage_df) {
  passage_df %>%
    select(misprod:elongation) %>%
    map_df(count_errors)
}

## For all error types for a given passage
count_error_syllables_any_type <- function(passage_df) {
  passage_df %>%
    select(misprod:elongation) %>% # only the error columns
    filter_all(any_vars(. == 1)) %>% # get only the rows that have a 1 somewhere
    nrow # count them
}

count_corrected_error_syllables <- function(passage_df) {
  passage_df %>% 
    filter(corrected == 1) %>% # only get corrected rows
    select(misprod:elongation) %>% # now let's only look at their error columns
    filter_all(any_vars(. == 1)) %>% # get only the rows that have an error somewhere
    nrow # count them
}

count_uncorrected_error_syllables <- function(passage_df) {
  passage_df %>% 
    filter(corrected == 0) %>% # only get uncorrected ones
    select(misprod:elongation) %>% # now let's only look at their error columns
    filter_all(any_vars(. == 1)) %>% # get only the rows that have an error somewhere
    nrow # count them
}


error_summary <- function(passage_df) {
  if (any(passage_df == FALSE)) {
    # a quick repair instead instead of an error: so we don't have to halt everything and start over
    summary = passage_df
    summary$total_errors <- -1
    summary$total_corrections <- -1
    summary$total_uncorrected_errors <- -1
    return(summary)
  }
  
  summary <- count_errors_by_type(passage_df)
  summary$total_errors <- count_error_syllables_any_type(passage_df)
  summary$total_corrections <- count_corrected_error_syllables(passage_df)
  summary$total_uncorrected_errors <- count_uncorrected_error_syllables(passage_df)
  
  return(summary)
}


status_message <- function(passage_name, participant_id) {
  status = paste("Generating summary from participant ", participant_id, "'s ", 
                 passage_name, " passage...",
                 sep = '')
  message(status)
}

error_summary_with_metadata <- function(passage_name, participant_id, dir_root) {
  if(DEBUG_MODE) status_message(passage_name, participant_id)

  summary = 
    passage_name_to_df(passage_name, participant_id, dir_root) %>%
    complain_when_invalid(participant_id, passage_name) %>%
    error_summary
  
  return(
    cbind(
      id = participant_id, # pre-pose an id column
      passage = fs::path_ext_remove(passage_name), # pre-pose a passage column, chomping 'bees.xlsx' to 'bees', e.g.
      error_rate = summary$total_errors / syllable_count(passage_name), # errors per syllable- TODO change to words?
      summary
    )
  )
}



# all passages for a participant
generate_summary_for_each_passage_with_metadata <- function(dir_root, participant_id, write_to = incremental_writeout, date_format = date_format_default) {
  df = build_participant_dirname(dir_root, participant_id) %>% dir %>% # passage name _with_ the extension
      map_df(error_summary_with_metadata, participant_id, dir_root)

  if (!is.null(write_to) && fs::is_dir(write_to)) {
    outfile_debug = paste(write_to, "/", participant_id, "_", now() %>% format(date_format), '.csv', sep = "")
    write_csv(df, outfile_debug)
  }

  return(df)
}


# Now, for each participant under a directory, each identified by the form sub_XXXXXX_reconciled,
# call generate_summary_for_each_passage_with_metadata(the_parentdir_of_all_those, that_id)

find_participant_id_from_dirname <- function(dirname) {
  str_extract(dirname, "\\d+")
}

# e.g
# > find_participant_id_from_dirname("sub-150077/sub-150077_reconciled") 
# [1] "150077"

summarize_errors_in_subdirectories <- function(dir_root, subfolder_match) {
  dir_root %>%
    dir(include.dirs = TRUE, recursive = TRUE, pattern = subfolder_match) %>% # walk the directory
    map(find_participant_id_from_dirname) %>% # split it up: sub-150079_reconciled -> 150079
    map_df(generate_summary_for_each_passage_with_metadata, dir_root = dir_root) # summarize all spreadsheets for that participant, for each participant
}


# TLDR we don't have to change the regex: we just match on subfolders by 
# explicitly returning directories (include.dirs = TRUE) and recursing
# (recursive = TRUE), so that it catches the "_reconciled"-suffixed subfolders

# Now finally: write all our results to a file (a CSV)

build_output_filename <- function(label, ext = ext_default, timezone = tz_default, date_format = date_format_default) {
  # `label` may include the destination directory, if different from the working directory when the script is run  
  current_datetime <- now(timezone) %>% format(date_format)
  # current_time <- now("America/New_York") %>% format("%Y%m%d_%I%M%P")
  # e.g. 20230520_1240pm
  
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
