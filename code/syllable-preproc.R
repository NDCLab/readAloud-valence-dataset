#title: "syllable-preproc.R"
#author: "Jessica M. Alexander"
#input: coded mantis file (XLSX)
#output: preprocessed mantis file (CSV), at the syllable level, in data-monitoring/postprocessing-check/ folder

#set up libraries
library(readxl)

#select subject
subject <- 190001

#read in the passage structure to scaffold output
path1 <- '~/github/readAloud-valence-dataset/code/'
filename1 <- 'mantis_structure'
ext1 <- '.xlsx'
passage1 = 'neg-pos_mantis'
mantis_str <- data.frame(read_excel(paste(path1,filename1,ext1, sep = "", collapse = NULL),
                            sheet = passage1))

#append subject name as column 1
mantis_read <- cbind(rep(subject, nrow(mantis_str)), mantis_str)


#read in the coded file and create a dataframe from which to pull syllable-level data
path2 <- '~/github/readAloud-valence-dataset/code/'
filename2 <- paste("sub-", subject, sep = "", collapse = NULL)
ext2 <- '.xlsx'
passage2 = "mantis"
df <- data.frame(read_excel(paste(path2,filename2,ext2, sep = "", collapse = NULL),
                            sheet = passage2, skip=1, n_max=6))

#select error cells, re-name rows, assign numbers to columns (aka syllables)
df <- df[,-1]
df <- df[-c(5),] #remove correction row
rownames(df) <- c("hesitate", "insert", "mispronounce", "drop", "duplicate")
colnames(df) <- c(1:ncol(df))

#append syllable-level errors as columns in passage structure dataframe
mantis_read$hesitate <- unlist(df["hesitate",])
mantis_read$insert <- unlist(df["insert",])
mantis_read$mispronounce <- unlist(df["mispronounce",])
mantis_read$drop <- unlist(df["drop",])
mantis_read$duplicate <- unlist(df["duplicate",])


#specify disfluent or not

#specify corrected or not
