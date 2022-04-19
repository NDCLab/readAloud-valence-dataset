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
#out_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/derivatives/preprocessed/'
#local
blank_scaffolds <- '/Users/jalexand/github/readAloud-valence-dataset/code/scaffolds.xlsx'
input_path <- '/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/error-coding/'
out_path <- '/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/'

#identify participant folders within input dir
sub_folders <- list.files(input_path, pattern = "sub")

#create dataframe for storing output data and define output file name
disfluencySummaryDat <- data.frame(matrix(ncol=8, nrow=0))
colnames(disfluencySummaryDat) <- c("id",
                                    "passage",
                                    "percDisfluent_firstHalf",
                                    "percDisfluent_lastHalf",
                                    "percDisfluent_prePREswitch",
                                    "percDisfluent_preswitch",
                                    "percDisfluent_switch",
                                    "percDisfluent_postswitch")
disfluency_out <- paste("disfluencies_subject-by-passage_", today, ".csv", sep="", collapse=NULL)

### SECTION 2: START PARTICIPANT LOOP
#loop over participants (subfolders)
for(i in 1:length(sub_folders)){
  
  #identify the list of error-coded files for the participant along with participant id
  sub_files <- list.files(paste(input_path,sub_folders[i], sep = "", collapse = NULL))
  id <- strsplit(sub_folders, "-")[[1]][2]
  
  ### SECTION 3: START PASSAGE LOOP
  #establish passage name
  for(j in 1:length(sub_files)){
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
    
    #add column to indicate all disfluent syllables
    passageErrors$disfluent <- rowSums(passageErrors[,6:14])>0
    
    #calculate percentage disfluency in each passage half
    #first half
    passageErrors_first <- passageErrors[1:(match("switch", passageErrors$wordGroup)-1),]
    numSyll_first <- length(passageErrors_first$disfluent) #count number of syllables in group
    passageErrors_first_disfluent <- passageErrors_first[passageErrors_first$disfluent,] #subset to disfluent rows
    numSyll_first_disfluent <- length(passageErrors_first_disfluent$disfluent) #count number of disfluent syllables
    percDisfluent_firstHalf <- numSyll_first_disfluent / numSyll_first
    
    #second half
    passageErrors_last <- tail(passageErrors, (length(passageErrors$wordGroup) - match("switch", passageErrors$wordGroup) + 1) )
    numSyll_last <- length(passageErrors_last$disfluent) #count number of syllables in group
    passageErrors_last_disfluent <- passageErrors_last[passageErrors_last$disfluent,] #subset to disfluent rows
    numSyll_last_disfluent <- length(passageErrors_last_disfluent$disfluent) #count number of disfluent syllables
    percDisfluent_lastHalf <- numSyll_last_disfluent / numSyll_last
    
    #calculate percentage disfluency in word groups around the switch
    #prePREswitch group
    passageErrors_prePREswitch <- passageErrors[passageErrors$wordGroup %in% c("prePREswitchGroup"),] #subset to prePREswitch group rows
    numSyll_prePREswitch <- length(passageErrors_prePREswitch$disfluent) #count number of syllables in group
    passageErrors_prePREswitch_disfluent <- passageErrors_prePREswitch[passageErrors_prePREswitch$disfluent,] #subset to disfluent rows
    numSyll_prePREswitch_disfluent <- length(passageErrors_prePREswitch_disfluent$disfluent) #count number of disfluent syllables
    percDisfluent_prePREswitch <- numSyll_prePREswitch_disfluent / numSyll_prePREswitch
    
    #preswitch group
    passageErrors_preswitch <- passageErrors[passageErrors$wordGroup %in% c("preswitchGroup"),] #subset to preswitch group rows
    numSyll_preswitch <- length(passageErrors_preswitch$disfluent) #count number of syllables in group
    passageErrors_preswitch_disfluent <- passageErrors_preswitch[passageErrors_preswitch$disfluent,] #subset to disfluent rows
    numSyll_preswitch_disfluent <- length(passageErrors_preswitch_disfluent$disfluent) #count number of disfluent syllables
    percDisfluent_preswitch <- numSyll_preswitch_disfluent / numSyll_preswitch
    
    #switch group
    passageErrors_switch <- passageErrors[passageErrors$wordGroup %in% c("switchGroup", "switch"),] #subset to switch group rows
    numSyll_switch <- length(passageErrors_switch$disfluent) #count number of syllables in group
    passageErrors_switch_disfluent <- passageErrors_switch[passageErrors_switch$disfluent,] #subset to disfluent rows
    numSyll_switch_disfluent <- length(passageErrors_switch_disfluent$disfluent) #count number of disfluent syllables
    percDisfluent_switch <- numSyll_switch_disfluent / numSyll_switch
    
    #postswitch group
    passageErrors_postswitch <- passageErrors[passageErrors$wordGroup %in% c("postswitchGroup"),] #subset to postswitch group rows
    numSyll_postswitch <- length(passageErrors_postswitch$disfluent) #count number of syllables in group
    passageErrors_postswitch_disfluent <- passageErrors_postswitch[passageErrors_postswitch$disfluent,] #subset to disfluent rows
    numSyll_postswitch_disfluent <- length(passageErrors_postswitch_disfluent$disfluent) #count number of disfluent syllables
    percDisfluent_postswitch <- numSyll_postswitch_disfluent / numSyll_postswitch
    
    
    #store output data in summary matrices
    disfluencySummaryDat[nrow(disfluencySummaryDat) + 1,] <-c(id,
                                                              passage,
                                                              percDisfluent_firstHalf,
                                                              percDisfluent_lastHalf,
                                                              percDisfluent_prePREswitch,
                                                              percDisfluent_preswitch,
                                                              percDisfluent_switch,
                                                              percDisfluent_postswitch)
  
  }
}

### SECTION 4: OUTPUT DATA
write.csv(disfluencySummaryDat,paste(out_path, disfluency_out, sep = "", collapse = NULL), row.names=FALSE)