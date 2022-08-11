# readAloud-valence-dataset Stimuli Frequency
# Authors: Jessica M. Alexander
# Last Updated: 2022-08-09


### SECTION 1: SETTING UP
library(readxl)
library(ggplot2)

stimfile <- "/Users/jalexand/github/readAloud-valence-dataset/materials/readAloud-ldt/stimuli/readAloud/readAloud-stimuli_characteristics.xlsx"
switchDat <- read_xlsx(stimfile, sheet="switches", skip=1, na="#")

passage_list <- list.files("/Users/jalexand/github/readAloud-valence-dataset/materials/readAloud-ldt/stimuli/readAloud/liwc-analysis/input")

passages <- c()
for(i in 1:length(passage_list)){
  passages <- c(passages, strsplit(passage_list[i], "_")[[1]][1])
}
passages <- unique(passages)

df <- data.frame(matrix(ncol=5, nrow=0))
colnames(df) <- c("passage",
                   "position",
                   "valence",
                   "avgFreq",
                   "sdFreq")

### SECTION 2: CALCULATE PER PASSAGE FREQUENCIES
for(j in 1:length(passages)){
  passage <- passages[j]
  passageDat <- read_xlsx(stimfile, sheet=passage, skip=1, na="#") #read in passage data
  switchType <- switchDat$switchType[match(passage, switchDat$passage)] #identify passage switch type (neg2pos or pos2neg)
  preSwitchVal <- substr(switchType, 1, 3) #identify valence of preswitch passage half
  postSwitchVal <-substr(switchType, 5, 7) #identify valence of postswitch passage half
  switchWord <- switchDat$switchWord[match(passage, switchDat$passage)] #identify passage switch word
  switchWordIdx <- match(switchWord, passageDat$stimRoot) #identify index of passage switch word
  
  preSwitchDat <- passageDat$logFreqSUB[1:(switchWordIdx-1)] #slice vector into pre-...
  postSwitchDat <- passageDat$logFreqSUB[switchWordIdx:nrow(passageDat)] #...and post-switch halves
  
  preSwitchFreqAvg <- mean(preSwitchDat, na.rm=TRUE) #calculate mean for preswitch half
  preSwitchFreqSd <- sd(preSwitchDat, na.rm=TRUE) #calculate standard deviation for preswitch half
  postSwitchFreqAvg <- mean(postSwitchDat, na.rm=TRUE) #calculate mean for postswitch half
  postSwitchFreqSd <- sd(postSwitchDat, na.rm=TRUE) #calculate standard deviation for postswitch half
  
  vectorPre <- c(passage, "pre", preSwitchVal, preSwitchFreqAvg, preSwitchFreqSd)
  df[nrow(df) + 1,] <- c(vectorPre)
  
  vectorPost <- c(passage, "post", postSwitchVal, postSwitchFreqAvg, postSwitchFreqSd)
  df[nrow(df) + 1,] <- c(vectorPost)
}


### SECTION 3: CALCULATE GRAND MEANS
dfPosPre <- df[df$position=="pre" & df$valence=="pos",] #subset into positive, preswitch data
posPreAvg <- mean(as.numeric(dfPosPre$avgFreq)) #calculate grand mean
posPreSd <- mean(as.numeric(dfPosPre$sdFreq)) #calculate grand sd

dfPosPost <- df[df$position=="post" & df$valence=="pos",] #subset into positive, postswitch data
posPostAvg <- mean(as.numeric(dfPosPost$avgFreq)) #calculate grand mean
posPostSd <- mean(as.numeric(dfPosPost$sdFreq)) #calculate grand sd

vectorPosAvg <- c(posPreAvg, posPostAvg) #create positive vector of grand means
vectorPosSd <- c(posPreSd, posPostSd) #create positive vector of grand standard deviations


dfNegPre <- df[df$position=="pre" & df$valence=="neg",] #subset into negative, preswitch data
negPreAvg <- mean(as.numeric(dfNegPre$avgFreq)) #calculate grand mean
negPreSd <- mean(as.numeric(dfNegPre$sdFreq)) #calculate grand sd

dfNegPost <- df[df$position=="post" & df$valence=="neg",] #subset into negative, postswitch data
negPostAvg <- mean(as.numeric(dfNegPost$avgFreq)) #calculate grand mean
negPostSd <- mean(as.numeric(dfNegPost$sdFreq)) #calculate grand sd

vectorNegAvg <- c(negPreAvg,negPostAvg) #create negative vector of grand means
vectorNegSd <- c(negPreSd, negPostSd) #create negative vector of grand standard deviations


### SECTION 4: OUTPUT DFs
#output mean frequency by valence x position
avgTotals <- data.frame(matrix(ncol=2, nrow=2))
colnames(avgTotals) <- c("pre", "post")
avgTotals[1,] <- vectorPosAvg
avgTotals[2,] <- vectorNegAvg
rownames(avgTotals) <- c("pos", "neg")

#output frequency standard deviation by valence x position
sdTotals <- data.frame(matrix(ncol=2, nrow=2))
colnames(sdTotals) <- c("pre", "post")
sdTotals[1,] <- vectorPosSd
sdTotals[2,] <- vectorNegSd
rownames(sdTotals) <- c("pos", "neg")


### SECTION 5: T-TESTS
#compare averages
posPrevPostAvg <- t.test(x=as.numeric(dfPosPre$avgFreq), y=as.numeric(dfPosPost$avgFreq), alternative="two.sided")
negPrevPostAvg <- t.test(x=as.numeric(dfNegPre$avgFreq), y=as.numeric(dfNegPost$avgFreq), alternative="two.sided")
prePosvNegAvg <- t.test(x=as.numeric(dfPosPre$avgFreq), y=as.numeric(dfNegPre$avgFreq), alternative="two.sided")
postPosvNegAvg <- t.test(x=as.numeric(dfPosPost$avgFreq), y=as.numeric(dfNegPost$avgFreq), alternative="two.sided")

#compare standard deviations
posPrevPostSd <- t.test(x=as.numeric(dfPosPre$sdFreq), y=as.numeric(dfPosPost$sdFreq), alternative="two.sided")
negPrevPostSd <- t.test(x=as.numeric(dfNegPre$sdFreq), y=as.numeric(dfNegPost$sdFreq), alternative="two.sided")
prePosvNegSd <- t.test(x=as.numeric(dfPosPre$sdFreq), y=as.numeric(dfNegPre$sdFreq), alternative="two.sided")
postPosvNegSd <- t.test(x=as.numeric(dfPosPost$sdFreq), y=as.numeric(dfNegPost$sdFreq), alternative="two.sided")