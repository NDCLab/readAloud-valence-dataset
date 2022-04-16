# readAloud-valence-dataset Timingn and Pitch Preprocessing
# Author: Jessica M. Alexander
# Last Updated: 2022-04-14

### SECTION 1: SETTING UP
library(readxl)

#set up date for output file naming
today <- Sys.Date()
today <- format(today, "%Y%m%d")

#set up directories for input/output data
#hpc
#passageChar_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/materials/readAloud-ldt/stimuli/readAloud/readAloud-stimuli_characteristics.xlsx'
#input_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/derivatives/preprocessed/timing-and-pitch/'
#out_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/derivatives/preprocessed/timing-and-pitch/'
#local
passageChar_path <- '/Users/jalexand/github/readAloud-valence-dataset/materials/readAloud-ldt/stimuli/readAloud/readAloud-stimuli_characteristics.xlsx'
input_path <- '/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/timing-and-pitch/'
out_path <- '/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/timing-and-pitch/'

#load passage characteristics data
passageChar <- read_excel(passageChar_path, sheet="passages")

#identify participant folders within input dir
sub_files <- list.files(input_path, pattern = "sub")

#create dataframes for storing output data and define output file names
#timing
timingSummaryDat <- data.frame(matrix(ncol=13, nrow=0))
colnames(timingSummaryDat) <- c("id",
                               "posFirstSpeed", "negFirstSpeed",
                               "posLastSpeed", "negLastSpeed",
                               "prePREswitchSpeed_pos2neg", "prePREswitchSpeed_neg2pos",
                               "preswitchSpeed_pos2neg", "preswitchSpeed_neg2pos",
                               "switchSpeed_pos2neg", "switchSpeed_neg2pos",
                               "postswitchSpeed_pos2neg", "postswitchSpeed_neg2pos")
timing_out_subjectLevel <- paste("timing_subject-level_summary_", today, ".csv", sep="", collapse=NULL)

timingTrialDat <- data.frame(matrix(ncol=9, nrow=0))
colnames(timingTrialDat) <- c("id",
                             "passage",
                             "switchType",
                             "firstSpeed",
                             "lastSpeed",
                             "prePREswitchSpeed",
                             "preswitchSpeed",
                             "switchSpeed",
                             "postswitchSpeed")
timing_out_trialLevel <- paste("timing_trial-level_summary_", today, ".csv", sep="", collapse=NULL)

#pitch
pitchSummaryDat <- data.frame(matrix(ncol=13, nrow=0))
colnames(pitchSummaryDat) <- c("id",
                               "pitchStartToSwitch_pos2neg", "pitchStartToSwitch_neg2pos",
                               "pitchSwitchToEnd_pos2neg", "pitchSwitchToEnd_pos2neg",
                               "pitchPrePREswitchGroup_pos2neg", "pitchPrePREswitchGroup_neg2pos",
                               "pitchPreswitchGroup_pos2neg", "pitchPreswitchGroup_neg2pos",
                               "pitchSwitchGroup_pos2neg", "pitchSwitchGroup_neg2pos",
                               "pitchPostswitchGroup_pos2neg", "pitchPostswitchGroup_neg2pos")
pitch_out_subjectLevel <- paste("pitch_subject-level_summary_", today, ".csv", sep="", collapse=NULL)

pitchTrialDat <- data.frame(matrix(ncol=9, nrow=0))
colnames(pitchTrialDat) <- c("id",
                              "passage",
                              "switchType",
                              "firstPitch",
                              "lastPitch",
                              "prePREswitchPitch",
                              "preswitchPitch",
                              "switchPitch",
                              "postswitchPitch")
pitch_out_trialLevel <- paste("pitch_trial-level_summary_", today, ".csv", sep="", collapse=NULL)


### SECTION 2: START PARTICIPANT LOOP AND CLEAN INCOMING DATAFRAME
#loop over participants (subfiles)
for(i in 1:length(sub_files)){
  
  #find the timing and pitch file for this participant
  timingPitch_file <- paste(input_path,sub_files[i], sep = "", collapse = NULL)
  print(paste("Woohoo! Processing ", sub_files[i], "!"))

  #read in the data for this participant, establish id, and add passage type (pos2neg or neg2pos)
  timingPitchDat <- read_excel(timingPitch_file, sheet = NULL)
  id <- strsplit(sub_files[i], "_")[[1]][1]
  timingPitchDat$switchType <- passageChar$switchType
  
  
  ### SECTION 3: SPLIT INTO DATAFRAMES BY SWITCH TYPE
  timingPitchDat_pos2neg <- timingPitchDat[timingPitchDat$switchType=="pos2neg",]
  timingPitchDat_neg2pos <- timingPitchDat[timingPitchDat$switchType=="neg2pos",]
  
  
  ### SECTION 4: CALCULATE PASSAGE HALF READING SPEEDS
  #first passage half
  timingPitchDat_pos2neg$posFirstTime <- timingPitchDat_pos2neg$switchWord - timingPitchDat_pos2neg$readStart
  posFirstLength <- NUMBER OF SYLLABLES HERE
  timingPitchDat_pos2neg$posFirstSpeed <- timingPitchDat_pos2neg$posFirstTime/posFirstLength
  posFirstSpeed <- mean(timingPitchDat_pos2neg$posFirstSpeed)
  
  timingPitchDat_neg2pos$negFirstTime <- timingPitchDat_neg2pos$switchWord - timingPitchDat_neg2pos$readStart
  negFirstLength <- NUMBER OF SYLLABLES HERE
  timingPitchDat_neg2pos$negFirstSpeed <- timingPitchDat_neg2pos$negFirstTime/negFirstLength
  negFirstSpeed <- mean(timingPitchDat_neg2pos$negFirstSpeed)
  
  #second passage half
  timingPitchDat_pos2neg$posLastTime <- timingPitchDat_pos2neg$readEnd - timingPitchDat_pos2neg$switchWord
  posLastLength <- NUMBER OF SYLLABLES HERE
  timingPitchDat_pos2neg$posLastSpeed <- timingPitchDat_pos2neg$posLastTime/posLastLength
  posLastSpeed <- mean(timingPitchDat_pos2neg$posLastSpeed)
  
  timingPitchDat_neg2pos$negLastTime <- timingPitchDat_neg2pos$readEnd - timingPitchDat_neg2pos$switchWord
  negLastLength <- NUMBER OF SYLLABLES HERE
  timingPitchDat_neg2pos$negLastSpeed <- timingPitchDat_neg2pos$negLastTime/negLastLength
  negLastSpeed <- mean(timingPitchDat_neg2pos$negLastSpeed)
  
  ### SECTION 5: CALCULATE PASSAGE HALF READING PITCH
  pitchStartToSwitch_pos2neg <- mean(timingPitchDat_pos2neg$pitchStartToSwitch)
  pitchStartToSwitch_neg2pos <- mean(timingPitchDat_neg2pos$pitchStartToSwitch)
  pitchSwitchToEnd_pos2neg <- mean(timingPitchDat_pos2neg$pitchSwitchToEnd)
  pitchSwitchToEnd_neg2pos <- mean(timingPitchDat_neg2pos$pitchSwitchToEnd)
  
  ### SECTION 6: CALCULATE SWITCH GROUP READING SPEED
  #pos2neg: prePREswitch group
  timingPitchDat_pos2neg$prePREswitchTime_pos2neg <- timingPitchDat_pos2neg$preswitchStart - timingPitchDat_pos2neg$prePREswitchStart
  prePREswitchLength_pos2neg <- NUMBER OF SYLLABLES HERE
  timingPitchDat_pos2neg$prePREswitchSpeed_pos2neg <- timingPitchDat_pos2neg$prePREswitchTime_pos2neg/prePREswitchLength_pos2neg
  prePREswitchSpeed_pos2neg <- mean(timingPitchDat_pos2neg$prePREswitchSpeed_pos2neg)
  
  #pos2neg: preswitch group
  timingPitchDat_pos2neg$preswitchTime_pos2neg <- timingPitchDat_pos2neg$switchStart - timingPitchDat_pos2neg$preswitchStart
  preswitchLength_pos2neg <- NUMBER OF SYLLABLES HERE
  timingPitchDat_pos2neg$preswitchSpeed_pos2neg <- timingPitchDat_pos2neg$preswitchTime_pos2neg/preswitchLength_pos2neg
  preswitchSpeed_pos2neg <- mean(timingPitchDat_pos2neg$preswitchSpeed_pos2neg)
  
  #pos2neg: switch group
  timingPitchDat_pos2neg$switchTime_pos2neg <- timingPitchDat_pos2neg$postswitchStart - timingPitchDat_pos2neg$switchStart
  switchLength_pos2neg <- NUMBER OF SYLLABLES HERE
  timingPitchDat_pos2neg$switchSpeed_pos2neg <- timingPitchDat_pos2neg$switchTime_pos2neg/switchLength_pos2neg
  switchSpeed_pos2neg <- mean(timingPitchDat_pos2neg$switchSpeed_pos2neg)
  
  #pos2neg: postswitch group
  timingPitchDat_pos2neg$postswitchTime_pos2neg <- timingPitchDat_pos2neg$postswitchEnd - timingPitchDat_pos2neg$postswitchStart
  postswitchLength_pos2neg <- NUMBER OF SYLLABLES HERE
  timingPitchDat_pos2neg$postswitchSpeed_pos2neg <- timingPitchDat_pos2neg$postswitchTime_pos2neg/postswitchLength_pos2neg
  postswitchSpeed_pos2neg <- mean(timingPitchDat_pos2neg$postswitchSpeed_pos2neg)
  
  #neg2pos: prePREswitch group
  timingPitchDat_neg2pos$prePREswitchTime_neg2pos <- timingPitchDat_neg2pos$preswitchStart - timingPitchDat_neg2pos$prePREswitchStart
  prePREswitchLength_neg2pos <- NUMBER OF SYLLABLES HERE
  timingPitchDat_neg2pos$prePREswitchSpeed_neg2pos <- timingPitchDat_neg2pos$prePREswitchTime_neg2pos/prePREswitchLength_neg2pos
  prePREswitchSpeed_neg2pos <- mean(timingPitchDat_neg2pos$prePREswitchSpeed_neg2pos)
  
  #neg2pos: preswitch group
  timingPitchDat_neg2pos$preswitchTime_neg2pos <- timingPitchDat_neg2pos$switchStart - timingPitchDat_neg2pos$preswitchStart
  preswitchLength_neg2pos <- NUMBER OF SYLLABLES HERE
  timingPitchDat_neg2pos$preswitchSpeed_neg2pos <- timingPitchDat_neg2pos$preswitchTime_neg2pos/preswitchLength_neg2pos
  preswitchSpeed_neg2pos <- mean(timingPitchDat_neg2pos$preswitchSpeed_neg2pos)
  
  #neg2pos: switch group
  timingPitchDat_neg2pos$switchTime_neg2pos <- timingPitchDat_neg2pos$postswitchStart - timingPitchDat_neg2pos$switchStart
  switchLength_neg2pos <- NUMBER OF SYLLABLES HERE
  timingPitchDat_neg2pos$switchSpeed_neg2pos <- timingPitchDat_neg2pos$switchTime_neg2pos/switchLength_neg2pos
  switchSpeed_neg2pos <- mean(timingPitchDat_neg2pos$switchSpeed_neg2pos)
  
  #neg2pos: postswitch group
  timingPitchDat_neg2pos$postswitchTime_neg2pos <- timingPitchDat_neg2pos$postswitchEnd - timingPitchDat_neg2pos$postswitchStart
  postswitchLength_neg2pos <- NUMBER OF SYLLABLES HERE
  timingPitchDat_neg2pos$postswitchSpeed_neg2pos <- timingPitchDat_neg2pos$postswitchTime_neg2pos/postswitchLength_neg2pos
  postswitchSpeed_neg2pos <- mean(timingPitchDat_neg2pos$postswitchSpeed_neg2pos)
  
  ### SECTION 7: CALCULATE SWITCH GROUP READING PITCH
  pitchPrePREswitchGroup_pos2neg <- mean(timingPitchDat_pos2neg$pitchPrePREswitchGroup)
  pitchPrePREswitchGroup_neg2pos <- mean(timingPitchDat_neg2pos$pitchPrePREswitchGroup)
  
  pitchPreswitchGroup_pos2neg <- mean(timingPitchDat_pos2neg$pitchPreswitchGroup)
  pitchPreswitchGroup_neg2pos <- mean(timingPitchDat_neg2pos$pitchPreswitchGroup)
  
  pitchSwitchGroup_pos2neg <- mean(timingPitchDat_pos2neg$pitchSwitchGroup)
  pitchSwitchGroup_neg2pos <- mean(timingPitchDat_neg2pos$pitchSwitchGroup)
  
  pitchPostswitchGroup_pos2neg <- mean(timingPitchDat_pos2neg$pitchPostswitchGroup)
  pitchPostswitchGroup_neg2pos <- mean(timingPitchDat_neg2pos$pitchPostswitchGroup)

  #store output data in summary matrices
  timingSummaryDat[nrow(timingSummaryDat) + 1,] <-c(id,
                                                    posFirstSpeed, negFirstSpeed,
                                                    posLastSpeed, negLastSpeed,
                                                    prePREswitchSpeed_pos2neg, prePREswitchSpeed_neg2pos,
                                                    preswitchSpeed_pos2neg, preswitchSpeed_neg2pos,
                                                    switchSpeed_pos2neg, switchSpeed_neg2pos,
                                                    postswitchSpeed_pos2neg, postswitchSpeed_neg2pos)

  pitchSummaryDat[nrow(pitchSummaryDat) +1,] <- c(id,
                                                  pitchStartToSwitch_pos2neg, pitchStartToSwitch_neg2pos,
                                                  pitchSwitchToEnd_pos2neg, pitchSwitchToEnd_pos2neg,
                                                  pitchPrePREswitchGroup_pos2neg, pitchPrePREswitchGroup_neg2pos,
                                                  pitchPreswitchGroup_pos2neg, pitchPreswitchGroup_neg2pos,
                                                  pitchSwitchGroup_pos2neg, pitchSwitchGroup_neg2pos,
                                                  pitchPostswitchGroup_pos2neg, pitchPostswitchGroup_neg2pos)
  
  
  
  for (j in 1:nrow(ldtDat)){
    trial_no <- j
    acc <- ldtDat$ldtResponse.corr[j]
    rt <- ldtDat$ldtResponse.rt[j]
    stimString <- ldtDat$ldtStim[j]
    wordType <- ldtDat$wordType[j]
    
    ldtTrialDat[nrow(ldtTrialDat) + 1,] <-c(id, trial_no, acc, rt, stimString, wordType)
    }
  
  
}



### SECTION 7: OUTPUT DATA
#write the extracted summary scores to CSV
write.csv(readAloudChallengeDat,paste(out_path,readAloud_out_passageLevel, sep = "", collapse = NULL), row.names=FALSE)
write.csv(readAloudSummaryDat,paste(out_path,readAloud_out_subjectLevel, sep = "", collapse = NULL), row.names=FALSE)
write.csv(ldtSummaryDat,paste(out_path,ldt_out_subjectLevel, sep = "", collapse = NULL), row.names=FALSE)
write.csv(ldtTrialDat,paste(out_path,ldt_out_trialLevel, sep = "", collapse = NULL), row.names=FALSE)
write.csv(dccsSummaryDat,paste(out_path,dccs_out_subjectLevel, sep = "", collapse = NULL), row.names=FALSE)
write.csv(dccsTrialDat,paste(out_path,dccs_out_trialLevel, sep = "", collapse = NULL), row.names=FALSE)