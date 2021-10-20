#title: "syllable-preproc.R"
#author: "Jessica M. Alexander"
#input: coded mantis file (XLSX)
#output: preprocessed mantis file (CSV), at the syllable level, in data-monitoring/postprocessing-check/ folder

#set up libraries
library(readxl)

#select subject
subject <- 190001

#READ IN PASSAGE STRUCTURE TO SCAFFOLD SYLLABLE-LEVEL OUTPUT
path1 <- '~/github/readAloud-valence-dataset/code/'
filename1 <- 'mantis_structure'
ext1 <- '.xlsx'
passage1 = 'neg-pos_mantis'
mantis_syll <- data.frame(read_excel(paste(path1,filename1,ext1, sep = "", collapse = NULL),
                            sheet = passage1))

#append subject name as column 1
mantis_syll <- cbind(rep(subject, nrow(mantis_syll)), mantis_syll)
colnames(mantis_syll)[1] <- c("subject")


#READ IN CODED FILE AND SET UP TWO DATAFRAMES, ONE FOR ERRORS AND ONE FOR CORRECTIONS
#create a dataframe from which to pull syllable-level data
path2 <- '~/github/readAloud-valence-dataset/code/'
filename2 <- paste("sub-", subject, sep = "", collapse = NULL)
ext2 <- '.xlsx'
passage2 = "mantis"
df <- data.frame(read_excel(paste(path2,filename2,ext2, sep = "", collapse = NULL),
                            sheet = passage2, skip=1, n_max=6))
df <- df[,-1] #remove coding instructions column

#select corrections, set aside in separate dataframe
df_correct <- df[5,]

#select error cells (by removing correction row), re-name rows, assign numbers to columns (aka syllables)
df <- df[-5,]
rownames(df) <- c("hesitate", "insert", "mispronounce", "drop", "duplicate")
colnames(df) <- c(1:ncol(df))

#APPEND CODED DATA TO SYLLABLE-LEVEL SCAFFOLD
#append syllable-level errors as columns in passage structure dataframe
mantis_syll$hesitate <- unlist(df["hesitate",])
mantis_syll$insert <- unlist(df["insert",])
mantis_syll$mispronounce <- unlist(df["mispronounce",])
mantis_syll$drop <- unlist(df["drop",])
mantis_syll$duplicate <- unlist(df["duplicate",])

#specify disfluent or not
mantis_syll$disfluent <- as.numeric(rowSums(mantis_syll[,5:9])>0)

#specify corrected or not
mantis_syll$corrected <- unlist(df_correct)

#OUTPUT PREPROCESSED CSV
output_path <- "/Users/jalexand/github/readAloud-valence-dataset/data-monitoring/postprocessing-check/"
output_name <- paste("sub-",subject, sep = "", collapse = NULL)
write.csv(mantis_syll, paste(output_path,output_name,"_syllable_preproc_", today(), ".csv", sep = "", collapse = NULL), row.names=FALSE)