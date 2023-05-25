# Draft script: reading in reconciled Excels, summarizing the errors of each, 
# and writing that to a new CSV
#
# Luc Sahar and Jessica M. Alexander -- NDCLab, Florida International University
# last updated 5/25/23

# used as samples:

# 150077
# 150079
# 150086

# library(tidyverse)
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


# headers_idiomatic_given = c(
#   "id",
#   "passage",
#   "mispron",               # "misprod",
#   "insert",                # "ins_dup",
#   "omit",                  # "omit",
#   "stress",                # "word_stress",
#   "filled",                # "filled_pause",
#   "hes",                   # "hesitation",
#   "elong",                 # "elongation",
#   "correction",            # "corrected",
#   "totalErrSyll",          # "last_precorrection",
#   "totalUncorrErr"         # "actual_prod",
# ) # uncommented ones are taken from jess' spec


## Read in XLSXes as arguments

build_participant_dirname <- function(dir_root, participant_id) {
  paste(
    dir_root,
    '/sub-', participant_id, '_reconciled',
    sep = ""
  )
}

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

ls_root = "~/Documents/ndclab/analysis-sandbox/reconciled-sheets"
sample_root = "~/Documents/ndclab/analysis-sandbox/sample-sheets"
# FIXME for HPC


## transform and stuff
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


count_errors_by_type <- function(passage_df) {
  error_counts <- passage_df %>%
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


error_summary <- function(passage_df) { # maybe: condense this (top half is not strictly necessary)
  errors_by_type <- count_errors_by_type(passage_df)
  error_syllable_count <- count_error_syllables_any_type(passage_df)
  corrected_error_syllable_count <- count_corrected_error_syllables(passage_df)
  uncorrected_error_syllable_count <- count_uncorrected_error_syllables(passage_df)
  
  summary <- errors_by_type
  summary$total_errors <- error_syllable_count
  summary$total_corrections <- corrected_error_syllable_count
  summary$total_uncorrected_errors <- uncorrected_error_syllable_count
  
  return(summary)
}

error_summary_with_metadata <- function(passage_name, participant_id, dir_root) {
  passage_df = passage_name_to_df(passage_name, 
                                  participant_id,
                                  dir_root)
  
  summary = error_summary(passage_df)
  
  return(
    cbind(
      id = participant_id, # pre-pose an id column
      passage = fs::path_ext_remove(passage_name), # pre-pose a passage column, chomping 'bees.xlsx' to 'bees', e.g.
      summary
    )
  )
}


# all passages for a participant
generate_summary_for_each_passage_with_metadata <- function(dir_root, participant_id) {
  build_participant_dirname(dir_root, participant_id) %>% 
    dir %>% # passage name _with_ the extension
    map_df(error_summary_with_metadata, participant_id, dir_root)
}


# finally: all participants under a directory
# for every participant in the directory, identified by the form sub_XXXXXX_reconciled,
# call generate_summary_for_each_passage_with_metadata(the_parentdir_of_all_those, that_id)

find_participant_id_from_dirname <- function(dirname) {
  str_extract(dirname, "\\d+")
}

# e.g
# > find_participant_id_from_dirname("sub-150077_reconciled/") 
# [1] "150077"

summarize_errors_in_subdirectories <- function(dir_root, subfolder_match) {
  dir_root %>%
    dir(pattern = subfolder_match) %>% # walk the directory
    map(find_participant_id_from_dirname) %>% # split it up: sub-150079_reconciled -> 150079
    map_df(generate_summary_for_each_passage_with_metadata, dir_root = dir_root) # summarize all spreadsheets for that participant, for each participant
}

# format_to_spec <- function(summary_df) {
#   # put corrected errors before total errors, based on order in Jess' Google doc
#   pretty <- relocate(summary_df, total_corrections, .before = total_errors) 
#   
#   # give the requested titles
#   colnames(pretty) <- headers_idiomatic_given
#   
#   return(pretty)
# }

# and then write it to a file (a CSV)

# current_time <- now("America/New_York") %>% format("%Y%m%d_%I%M%P")
# e.g. 20230520_1240pm

ext_default = 'csv'
tz_default = "America/New_York"
date_format_default = "%Y%m%d_%I%M%P"
folder_regex_default = "sub-\\d{6}_reconciled"


build_output_filename <- function(label, ext = ext_default, timezone = tz_default, date_format = date_format_default) {
  # `label` may include the destination directory, if different from script location  
  current_datetime <- now(timezone) %>% format(date_format)
  
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
  summary_df <- summarize_errors_in_subdirectories(dir_root, subfolder_match) # %>% format_to_spec
  
  write_csv(summary_df, outpath_name)
  return(outpath_name)
}

# compute_summary_and_write_to_file(ls_root, "~/Documents/ndclab/analysis-sandbox/disfluencies_subject-x-passage")
