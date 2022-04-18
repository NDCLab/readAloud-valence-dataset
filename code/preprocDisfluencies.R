# readAloud-valence-dataset Error Coding Preprocessing
# Author: Jessica M. Alexander
# Last Updated: 2022-04-18

### SECTION 1: SETTING UP
library(readxl)

#set up date for output file naming
today <- Sys.Date()
today <- format(today, "%Y%m%d")

#set up directories for input/output data
#hpc
#blank_scaffolds <- '/home/data/NDClab/datasets/readAloud-valence-dataset/code/scaffolds.xlsx'
#input_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/derivatives/preprocessed/error-coding/'
#out_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/derivatives/preprocessed/error-coding/'
#local
blank_scaffolds <- '/Users/jalexand/github/readAloud-valence-dataset/code/scaffolds.xlsx'
input_path <- '/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/error-coding/'
out_path <- '/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/error-coding/'

#identify participant folders within input dir
sub_folders <- list.files(input_path, pattern = "sub")

#create dataframe for storing output data and define output file name
disfluencySummaryDat <- data.frame(matrix(ncol=5, nrow=0))
colnames(disfluencySummaryDat) <- c("id",
                                    "passage",
                                    "percDisfluent_firstHalf",
                                    "percDisfluent_lastHalf",
                                    "percDisfluent_switch")
disfluency_out <- paste("disfluencies_subject-by-passage_summary_", today, ".csv", sep="", collapse=NULL)

### SECTION 2: START PARTICIPANT LOOP
#loop over participants (subfolders)
for(i in 1:length(sub_folders)){
  
  #identify the list of error-coded files for the participant along with participant id
  sub_files <- list.files(paste(input_path,sub_folders[i], sep = "", collapse = NULL))
  id <- strsplit(sub_folders, "-")[[1]][2]
  
  ### SECTION 3: START PASSAGE LOOP
  #establish passage name
  for(j in 1:length(allFiles)){
    errorCoded_file <- paste(input_path, sub_folders[i],"/", sub_files[j], sep = "", collapse = NULL)
    passage <- strsplit(errorCoded_file, "_")[[1]][2]
    print(paste("Woohoo! Processing << ", passage, " >> for ", sub_folders[i], "!", sep = "", collapse = NULL))
    
    #load disfluency data onto scaffold
    scaffold <- read_xlsx(blank_scaffolds, sheet=passage)
    colnameVector <- colnames(scaffold) #capture column names for renaming passageErrors
    
    errorData <- read_xlsx(errorCoded_file, sheet=NULL, range=anchored("B2", dim=c(10, dim(scaffold)[1]), col_names=FALSE))
    errorDataT <- t(errorData) #transpose matrix to align with scaffold
    colnames(errorDataT) <- c("mispron", "wordstress", "duplicate", "falsestart", "insertion", "hesitation", "elongation", "omission","flipped")

    passageErrors <- cbind(scaffold, errorDataT)
    
    #calculate percentage disfluency in each passage half and switch group
  }
  
  
  
  

  
