#title: "passage-preproc.R"
#author: "Jessica M. Alexander"
#input: coded mantis file (XLSX)
#output: preprocessed mantis file (CSV), in data-monitoring/postprocessing-check/ folder


#set up libraries
library(lubridate)
library(readxl)

#READ IN THE CODED FILE AND ESTABLISH TWO DATAFRAMES, ERRORS AND TIMING
path <- '~/github/readAloud-valence-dataset/code/fakedata/'
subject <- 190001
filename <- paste("sub-", subject, sep = "", collapse = NULL)
ext <- '.xlsx'
passage = "mantis"

#select error cells, re-name rows, assign numbers to columns (aka syllables)
df <- data.frame(read_excel(paste(path,filename,ext, sep = "", collapse = NULL), sheet = passage, range="b2:zz8"))
df <- df[-c(5),] #remove correction row
rownames(df) <- c("hesitate", "insert", "mispronounce", "drop", "duplicate")
colnames(df) <- c(1:ncol(df))

#select timing cells, re-name rows, assign numbers to columns (aka syllables)
times <- data.frame(read_excel(paste(path,filename,ext, sep = "", collapse = NULL), sheet = passage, range="b8:zz10"))
rownames(times) <- c("onset", "end")
colnames(times) <- c(1:ncol(times))


#HARD CODING OF PASSAGE-SPECIFIC LOCATIONS
#establish location of start, switch point, and end
first_syll <- 1
switch_syll <- 168
last_syll <- 361

#establish locations of preswitch group, switch group, and postswitch group
pre_start <- 159
pre_end <- 165
switch_start <- 166
switch_end <- 174
post_start <- 175
post_end <- 185

#CALCULATE SPEED OF TWO PASSAGE HALVES
#establish chronology of the task: start of the negative passage portion, start of the positive passage portion, and end
first_half_onset <- as.integer(minute(ymd_hms(times[1,first_syll]))*60 + second(ymd_hms(times[1,first_syll])))
first_half_end <- as.integer(minute(ymd_hms(times[2,(switch_syll-1)]))*60 + second(ymd_hms(times[2,(switch_syll-1)])))
second_half_end <- as.integer(minute(ymd_hms(times[2,last_syll]))*60 + second(ymd_hms(times[2,last_syll])))

#establish syllabic lengths of each passage half
first_half_length <- ncol(times[1:(switch_syll-1)])
second_half_length <- ncol(times[switch_syll:last_syll])

#calculate reading speed of positive and negative passage portions (syllables/second)
first_half_speed <- (first_half_end - first_half_onset)/first_half_length
second_half_speed <- (second_half_end - first_half_end)/second_half_length

#CALCULATE ERROR RATES IN PASSAGE HALVES AND SWITCH GROUPS
#establish error count by type of error in each passage half
cum_error_first <- lapply(rowSums(df[,1:(switch_syll-1)]), sum)
error_hes_first <- cum_error_first$hesitate
error_ins_first <- cum_error_first$insert
error_mis_first <- cum_error_first$mispronounce
error_drop_first <- cum_error_first$drop
error_dup_first <- cum_error_first$duplicate

cum_error_second <- lapply(rowSums(df[,switch_syll:last_syll]), sum)
error_hes_second <- cum_error_second$hesitate
error_ins_second <- cum_error_second$insert
error_mis_second <- cum_error_second$mispronounce
error_drop_second <- cum_error_second$drop
error_dup_second <- cum_error_second$duplicate

#calculate total number of erroneous syllables in each passage half, along with error rate
first_half_total_error <- 0
for(i in 1:(switch_syll-1)) {
  col_total <- sum(df[,i])
  if(col_total == 0) {
    next
  }
  first_half_total_error <- first_half_total_error + 1
}
first_half_error_rate <- first_half_total_error/first_half_length

second_half_total_error <- 0
for(i in switch_syll:last_syll) {
  col_total <- sum(df[,i])
  if(col_total == 0) {
    next
  }
  second_half_total_error <- second_half_total_error + 1
}
second_half_error_rate <- second_half_total_error/second_half_length

#create mini dataframes for preswitch group, switch group, and postswitch group
preswitch <- df[,pre_start:pre_end]
switch <- df[,switch_start:switch_end]
postswitch <- df[,post_start:post_end]

#establish syllabic lengths of preswitch group, switch group, and postswitch group
preswitch_length <- ncol(preswitch)
switch_length <- ncol(switch)
postswitch_length <- ncol(postswitch)

#establish error count by type of error in preswitch group, switch group, and postswitch group
cum_error_pre <- lapply(rowSums(preswitch[,1:ncol(preswitch)]), sum)
error_hes_pre <- cum_error_pre$hesitate
error_ins_pre <- cum_error_pre$insert
error_mis_pre <- cum_error_pre$mispronounce
error_drop_pre <- cum_error_pre$drop
error_dup_pre <- cum_error_pre$duplicate

cum_error_switch <- lapply(rowSums(switch[,1:ncol(switch)]), sum)
error_hes_switch <- cum_error_switch$hesitate
error_ins_switch <- cum_error_switch$insert
error_mis_switch <- cum_error_switch$mispronounce
error_drop_switch <- cum_error_switch$drop
error_dup_switch <- cum_error_switch$duplicate

cum_error_post <- lapply(rowSums(postswitch[,1:ncol(postswitch)]), sum)
error_hes_post <- cum_error_post$hesitate
error_ins_post <- cum_error_post$insert
error_mis_post <- cum_error_post$mispronounce
error_drop_post <- cum_error_post$drop
error_dup_post <- cum_error_post$duplicate

#calculate total number of erroneous syllables in preswitch group, switch group, and postswitch group, along with error rate
preswitch_total_error <- 0
for(i in 1:ncol(preswitch)) {
  col_total <- sum(preswitch[,i])
  if(col_total == 0) {
    next
  }
  preswitch_total_error <- preswitch_total_error + 1
}
preswitch_error_rate <- preswitch_total_error/preswitch_length

switch_total_error <- 0
for(i in 1:ncol(switch)) {
  col_total <- sum(switch[,i])
  if(col_total == 0) {
    next
  }
  switch_total_error <- switch_total_error + 1
}
switch_error_rate <- switch_total_error/switch_length

postswitch_total_error <- 0
for(i in 1:ncol(postswitch)) {
  col_total <- sum(postswitch[,i])
  if(col_total == 0) {
    next
  }
  postswitch_total_error <- postswitch_total_error + 1
}
postswitch_error_rate <- postswitch_total_error/postswitch_length

#OUTPUT PREPROCESSED CSV
#build dataframe
output <- data.frame("subject" = c(subject),
                     "passage" = c(passage),
                     "first_half_length" = c(first_half_length),
                     "second_half_length" = c(second_half_length),
                     "first_half_speed" = c(first_half_speed),
                     "second_half_speed" = c(second_half_speed),
                     "first_half_total_error" = c(first_half_total_error),
                     "second_half_total_error" = c(second_half_total_error),
                     "first_half_error_rate" = c(first_half_error_rate),
                     "second_half_error_rate" = c(second_half_error_rate),
                     "error_hes_first" = c(error_hes_first),
                     "error_ins_first" = c(error_ins_first),
                     "error_mis_first" = c(error_mis_first),
                     "error_drop_first" = c(error_drop_first),
                     "error_dup_first" = c(error_dup_first),
                     "error_hes_second" = c(error_hes_second),
                     "error_ins_second" = c(error_ins_second),
                     "error_mis_second" = c(error_mis_second),
                     "error_drop_second" = c(error_drop_second),
                     "error_dup_second" = c(error_dup_second),
                     "preswitch_length" = c(preswitch_length),
                     "switch_length" = c(switch_length),
                     "postswitch_length" = c(postswitch_length),
                     "preswitch_total_error" = c(preswitch_total_error),
                     "switch_total_error" = c(switch_total_error),
                     "postswitch_total_error" = c(postswitch_total_error),
                     "preswitch_error_rate" = c(preswitch_error_rate),
                     "switch_error_rate" = c(switch_error_rate),
                     "postswitch_error_rate" = c(postswitch_error_rate),
                     "error_hes_pre" = c(error_hes_pre),
                     "error_ins_pre" = c(error_ins_pre),
                     "error_mis_pre" = c(error_mis_pre),
                     "error_drop_pre" = c(error_drop_pre),
                     "error_dup_pre" = c(error_dup_pre),
                     "error_hes_switch" = c(error_hes_switch),
                     "error_ins_switch" = c(error_ins_switch),
                     "error_mis_switch" = c(error_mis_switch),
                     "error_drop_switch" = c(error_drop_switch),
                     "error_dup_switch" = c(error_dup_switch),
                     "error_hes_post" = c(error_hes_post),
                     "error_ins_post" = c(error_ins_post),
                     "error_mis_post" = c(error_mis_post),
                     "error_drop_post" = c(error_drop_post),
                     "error_dup_post" = c(error_dup_post)
)

output_path <- '~/github/readAloud-valence-dataset/data-monitoring/postprocessing-check/'
write.csv(output, paste(output_path,filename,"_passage_preproc_", today(), ".csv", sep = "", collapse = NULL), row.names=FALSE)