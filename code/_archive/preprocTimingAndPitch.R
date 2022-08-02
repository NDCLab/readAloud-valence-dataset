# readAloud-valence-dataset Timing and Pitch Preprocessing
# Author: Jessica M. Alexander
# Last Updated: 2022-05-19

### SECTION 1: SETTING UP
library(readxl)

#set up date for output file naming
today <- Sys.Date()
today <- format(today, "%Y%m%d")

#set up directories for input/output data
#hpc
#blank_scaffolds <- '/home/data/NDClab/datasets/readAloud-valence-dataset/code/scaffolds.xlsx'
#input_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/derivatives/preprocessed/timing-and-pitch/'
#out_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/derivatives/preprocessed/'
#local
blank_scaffolds <- '/Users/jalexand/github/readAloud-valence-dataset/code/scaffolds.xlsx'
input_path <- '/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/timing-and-pitch/'
out_path <- '/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/'

#identify participant files within input dir
sub_files <- list.files(input_path, pattern = "sub")

#create dataframes for storing output data and define output file names
#timing
timingSummaryDat <- data.frame(matrix(ncol=8, nrow=0))
colnames(timingSummaryDat) <- c("id",
                             "passage",
                             "syllPerSec_firstHalf",
                             "syllPerSec_lastHalf",
                             "syllPerSec_prePREswitch",
                             "syllPerSec_preswitch",
                             "syllPerSec_switch",
                             "syllPerSec_postswitch")
timing_out <- paste("timing_subject-by-passage_", today, ".csv", sep="", collapse=NULL)

#pitch
pitchSummaryDat <- data.frame(matrix(ncol=8, nrow=0))
colnames(pitchSummaryDat) <- c("id",
                              "passage",
                              "vocalPitch_firstHalf",
                              "vocalPitch_lastHalf",
                              "vocalPitch_prePREswitch",
                              "vocalPitch_preswitch",
                              "vocalPitch_switch",
                              "vocalPitch_postswitch")
pitch_out <- paste("pitch_subject-by-passage_", today, ".csv", sep="", collapse=NULL)


### SECTION 2: START PARTICIPANT LOOP
#loop over participants (subfiles)
for(i in 1:length(sub_files)){
  
  #find the timing and pitch file for this participant
  timingPitch_file <- paste(input_path,sub_files[i], sep = "", collapse = NULL)
  print(paste("Woohoo! Processing ", sub_files[i], "!"))

  #read in the data for this participant, establish id
  timingPitchDat <- read_excel(timingPitch_file, sheet = NULL)
  id <- strsplit(strsplit(sub_files[i], "_")[[1]][1], "-")[[1]][2]
  
  
  ### SECTION 3: START PASSAGE LOOP
  for(j in 1:nrow(timingPitchDat)){
    passage <- toString(timingPitchDat[j,1])
    scaffold <- read_xlsx(blank_scaffolds, sheet=passage)
    passageDat <- timingPitchDat[j,]
    
    ### SECTION 4: CALCULATE READING SPEEDS
    #first passage half
    secondsProduced <- passageDat$switchWord - passageDat$readStart
    numSyll <- length(1:(match("switch", scaffold$wordGroup)-1))
    syllPerSec_firstHalf <- secondsProduced/numSyll
    
    #last passage half
    secondsProduced <- passageDat$readEnd - passageDat$switchWord
    numSyll <-nrow(tail(scaffold, (length(scaffold$wordGroup) - match("switch", scaffold$wordGroup) + 1)))
    syllPerSec_lastHalf <- secondsProduced/numSyll
    
    #prePREswitch group
    secondsProduced <- passageDat$preswitchStart - passageDat$prePREswitchStart
    numSyll <- nrow(scaffold[scaffold$wordGroup %in% c("prePREswitchGroup"),])
    syllPerSec_prePREswitch <- secondsProduced/numSyll
    
    #preswitch group
    secondsProduced <- passageDat$switchStart - passageDat$preswitchStart
    numSyll <- nrow(scaffold[scaffold$wordGroup %in% c("preswitchGroup"),])
    syllPerSec_preswitch <- secondsProduced/numSyll
    
    #switch group
    secondsProduced <- passageDat$postswitchStart - passageDat$switchStart
    numSyll <- nrow(scaffold[scaffold$wordGroup %in% c("switchGroup"),])
    syllPerSec_switch <- secondsProduced/numSyll
    
    #postswitch group
    secondsProduced <- passageDat$postswitchEnd - passageDat$postswitchStart
    numSyll <- nrow(scaffold[scaffold$wordGroup %in% c("postswitchGroup"),])
    syllPerSec_postswitch <- secondsProduced/numSyll
    
    
    ### SECTION 5: EXTRACT READING PITCH
    vocalPitch_firstHalf <- passageDat$pitchStartToSwitch
    vocalPitch_lastHalf <- passageDat$pitchSwitchToEnd
    vocalPitch_prePREswitch <- passageDat$pitchPrePREswitchGroup
    vocalPitch_preswitch <- passageDat$pitchPreswitchGroup
    vocalPitch_switch <- passageDat$pitchSwitchGroup
    vocalPitch_postswitch <- passageDat$pitchPostswitchGroup
    
    
    ### SECTION 6: STORE OUTPUT DATA IN SUMMARY MATRICES
    timingSummaryDat[nrow(timingSummaryDat) + 1,] <-c(id,
                                                      passage,
                                                      syllPerSec_firstHalf,
                                                      syllPerSec_lastHalf,
                                                      syllPerSec_prePREswitch,
                                                      syllPerSec_preswitch,
                                                      syllPerSec_switch,
                                                      syllPerSec_postswitch)
    
    pitchSummaryDat[nrow(pitchSummaryDat) +1,] <- c(id,
                                                    passage,
                                                    vocalPitch_firstHalf,
                                                    vocalPitch_lastHalf,
                                                    vocalPitch_prePREswitch,
                                                    vocalPitch_preswitch,
                                                    vocalPitch_switch,
                                                    vocalPitch_postswitch)
  }

}


### SECTION 7: OUTPUT DATA
#write the extracted summary scores to CSV
write.csv(timingSummaryDat,paste(out_path,timing_out, sep = "", collapse = NULL), row.names=FALSE)
write.csv(pitchSummaryDat,paste(out_path,pitch_out, sep = "", collapse = NULL), row.names=FALSE)


### SECTION 8: UPDATE CENTRAL TRACKER FOR STUDY
#load central tracker
track_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/data-monitoring/central-tracker_readAloud-valence.csv'
trackerDat <- read.csv(track_path, header=TRUE, check.names=FALSE)

#readAloudTiming_s1_r1_e1
for(row in 1:length(trackerDat$id)){
  id <- trackerDat[row, "id"]
  if (id %in% unique(timingSummaryDat$id)){
    trackerDat[trackerDat$id == id, ]$readAloudTiming_s1_r1_e1 = "11"
  } else {
    trackerDat[trackerDat$id == id, ]$readAloudTiming_s1_r1_e1 = "0"
  }
}
print("Updated readAloudTiming_s1_r1_e1!")

#readAloudPitch_s1_r1_e1
for(row in 1:length(trackerDat$id)){
  id <- trackerDat[row, "id"]
  if (id %in% unique(pitchSummaryDat$id)){
    trackerDat[trackerDat$id == id, ]$readAloudPitch_s1_r1_e1 = "11"
  } else {
    trackerDat[trackerDat$id == id, ]$readAloudPitch_s1_r1_e1 = "0"
  }
}
print("Updated readAloudPitch_s1_r1_e1!")

#write back to central tracker
write.csv(trackerDat, track_path, row.names = FALSE)