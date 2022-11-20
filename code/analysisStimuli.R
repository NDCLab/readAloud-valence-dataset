# readAloud-valence-dataset Stimuli Frequency
# Authors: Jessica M. Alexander
# Last Updated: 2022-11-20


### SECTION 1: SETTING UP
library(readxl)
library(ggplot2)
library(devtools)
library(wordcloud2)
library(gridExtra)
library(grid)
library(cowplot)
library(colorspace)
library(colorblindr)

#set up date for output file naming
today <- Sys.Date()
today <- format(today, "%Y%m%d")

#set up directories for input/output data
main_dataset <- '/Users/jalexand/github/readAloud-valence-dataset/'
out_path <- '/Users/jalexand/github/readAloud-valence-alpha/'

#set up directories for input/output data
passage_list <- list.files(paste(main_dataset, 'materials/readAloud-ldt/stimuli/readAloud/liwc-analysis/input', sep="", collapse="NULL"))
readAloudStimChar <- paste(main_dataset, 'materials/readAloud-ldt/stimuli/readAloud/readAloud-stimuli_characteristics.xlsx', sep="", collapse=NULL)
ldtWordList <- paste(main_dataset, 'materials/readAloud-ldt/stimuli/ldt/ldt_wordList.csv', sep="", collapse=NULL)
warriner_path <- paste(main_dataset, 'materials/readAloud-ldt/stimuli/resources/BRM-emot-submit_downloaded_2021-08-08.csv', sep="", collapse=NULL) #downloaded from https://link.springer.com/article/10.3758/s13428-012-0314-x on 08/08/2021
koustaCatList <- paste(main_dataset, 'materials/readAloud-ldt/stimuli/resources/kousta-categories.csv', sep="", collapse=NULL) #extracted from https://doi.org/10.1016/j.cognition.2009.06.007
extendKoustaList <- paste(main_dataset, 'materials/readAloud-ldt/stimuli/resources/valence_AnEW+_2796.xlsx', sep="", collapse=NULL) #kindly provided by the authors of https://doi.org/10.1016/j.cognition.2009.06.007 via personal correspondence
SUBList <- paste(main_dataset, 'materials/readAloud-ldt/stimuli/resources/SUBTLEXus74286wordstextversion.txt', sep="", collapse=NULL) #downloaded from https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus on 06/13/2022

switchDat <- read_xlsx(readAloudStimChar, sheet="switches", skip=1, na="#")
passDat <- read_xlsx(readAloudStimChar, sheet="passages", na="#")
ldtDat <- read.csv(ldtWordList)
warriner <- read.csv(warriner_path)
koustaCatDat <- read.csv(koustaCatList)
extKoustaDat <- read_xlsx(extendKoustaList, sheet="Sheet1")
subtlexus <- read.table(SUBList, header=TRUE)
subtlexus$Word <- tolower(subtlexus$Word)


### SECTION 2: LEXICAL DECISION TASK
ldtDat <- ldtDat[which(ldtDat$wordType=='word'),]

for(a in 1:nrow(ldtDat)){
  ldtDat$freq[a] <- subtlexus$Lg10WF[match(ldtDat$ldtStim[a], subtlexus$Word)]
  ldtDat$valenceWAR[a] <- warriner$V.Mean.Sum[match(ldtDat$ldtStim[a], warriner$Word)]
  ldtDat$valenceKOU[a] <- extKoustaDat$val[match(ldtDat$ldtStim[a], extKoustaDat$word)]
  ldtDat$koustaCat[a] <- koustaCatDat$valenceKousta[match(ldtDat$ldtStim[a], koustaCatDat$stimWord)]
  ldtDat$length[a] <- nchar(ldtDat$ldtStim[a])
  if(is.na(ldtDat$valenceWAR[a])){next}else if(ldtDat$valenceWAR[a]>5){ldtDat$binary[a] <- 'pos'}else{ldtDat$binary[a] <- 'neg'}
  ldtDat$magnitude[a] <- abs(5.2-ldtDat$valenceWAR[a]) #add magnitude against Warriner dataset median (5.2)
}

#frequency: matched
ggplot(data=ldtDat, aes(x=koustaCat, y=freq)) + geom_boxplot()
t.test(ldtDat$freq[which(ldtDat$koustaCat=='positive')], ldtDat$freq[which(ldtDat$koustaCat=='negative')])
t.test(ldtDat$freq[which(ldtDat$koustaCat=='positive')], ldtDat$freq[which(ldtDat$koustaCat=='neutral')])
t.test(ldtDat$freq[which(ldtDat$koustaCat=='neutral')], ldtDat$freq[which(ldtDat$koustaCat=='negative')]) #borderline

ggplot(data=ldtDat, aes(x=binary, y=freq)) + geom_boxplot()
t.test(ldtDat$freq[which(ldtDat$binary=='pos')], ldtDat$freq[which(ldtDat$binary=='neg')])

#length: matched
ggplot(data=ldtDat, aes(x=koustaCat, y=length)) + geom_boxplot()

#valence: matched
ggplot(data=ldtDat, aes(x=valenceWAR, y=valenceKOU, color=koustaCat)) + geom_point()
ggplot(data=ldtDat, aes(x=valenceWAR, y=freq, color=koustaCat)) + geom_point()

#valence magnitude: NOT MATCHED
ggplot(data=ldtDat, aes(x=koustaCat, y=magnitude)) + geom_boxplot() #Kousta pos/neg stimuli differ significantly on valence magnitude
t.test(ldtDat[ldtDat$koustaCat=="negative",]$magnitude, ldtDat[ldtDat$koustaCat=="positive",]$magnitude)


### SECTION 3: READALOUD TASK
passages <- c()
for(i in 1:length(passage_list)){
  passages <- c(passages, strsplit(passage_list[i], "_")[[1]][1])
}
passages <- unique(passages)

readDat <- data.frame(matrix(ncol=7, nrow=0))
colnames(readDat) <- c("passage",
                     "position",
                     "valence",
                     "length",
                     "avgFreq",
                     "sdFreq",
                     "avgMag")

#calculate per passage frequencies
for(j in 1:length(passages)){
  passage <- passages[j]
  passageDat <- read_xlsx(readAloudStimChar, sheet=passage, skip=1, na="#") #read in passage data
  switchType <- switchDat$switchType[match(passage, switchDat$passage)] #identify passage switch type (neg2pos or pos2neg)
  preSwitchVal <- substr(switchType, 1, 3) #identify valence of preswitch passage half
  postSwitchVal <-substr(switchType, 5, 7) #identify valence of postswitch passage half
  switchWord <- switchDat$switchWord[match(passage, switchDat$passage)] #identify passage switch word
  switchWordIdx <- match(switchWord, passageDat$stimRoot) #identify index of passage switch word
  
  lenWordPos <- passDat$lenWORDpos[match(passage, passDat$passage)] #identify number of syllables in positive passage half
  lenWordNeg <- passDat$lenWORDneg[match(passage, passDat$passage)] #identify number of syllables in negative passage half
  if(switchType=="pos2neg"){
    preLenWord <- lenWordPos
    postLenWord <- lenWordNeg
  }
  if(switchType=="neg2pos"){
    preLenWord <- lenWordNeg
    postLenWord <- lenWordPos
  }
  
  preSwitchFreq <- passageDat$logFreqSUB[1:(switchWordIdx-1)] #slice frequency into pre-...
  postSwitchFreq <- passageDat$logFreqSUB[switchWordIdx:nrow(passageDat)] #...and post-switch halves
  
  preSwitchFreqAvg <- mean(preSwitchFreq, na.rm=TRUE) #calculate mean frequency for preswitch half
  preSwitchFreqSd <- sd(preSwitchFreq, na.rm=TRUE) #calculate standard deviation for preswitch half
  postSwitchFreqAvg <- mean(postSwitchFreq, na.rm=TRUE) #calculate mean frequency for postswitch half
  postSwitchFreqSd <- sd(postSwitchFreq, na.rm=TRUE) #calculate standard deviation for postswitch half
  
  preSwitchMag <- passageDat$valenceStrengthWAR[1:(switchWordIdx-1)] #slice magnitude into pre-...
  postSwitchMag <- passageDat$valenceStrengthWAR[switchWordIdx:nrow(passageDat)] #...and post-switch halves
  
  preSwitchMagAvg <- mean(preSwitchMag, na.rm=TRUE) #calculate mean valence magnitude for preswitch half
  postSwitchMagAvg <- mean(postSwitchMag, na.rm=TRUE) #calculate mean valence magnitude for postswitch half
  
  vectorPre <- c(passage, "pre", preSwitchVal, (-1*preLenWord), preSwitchFreqAvg, preSwitchFreqSd, preSwitchMagAvg)
  readDat[nrow(readDat) + 1,] <- c(vectorPre)
  
  vectorPost <- c(passage, "post", postSwitchVal, postLenWord, postSwitchFreqAvg, postSwitchFreqSd, postSwitchMagAvg)
  readDat[nrow(readDat) + 1,] <- c(vectorPost)
}

#add flesch reading score
for(k in 1:nrow(readDat)){
  passage <- readDat$passage[k]
  valence <- readDat$valence[k]
  if(valence=='pos'){readDat$flesch[k] <- passDat$fleschPOS[which(passDat$passage==passage)]}
  else{readDat$flesch[k] <- passDat$fleschNEG[which(passDat$passage==passage)]}
}

#add warriner valence averages
for(m in 1:nrow(readDat)){
  passage <- readDat$passage[m]
  valence <- readDat$valence[m]
  if(valence=='pos'){readDat$valenceWARAvg[m] <- passDat$posAvgWAR[which(passDat$passage==passage)]}
  else{readDat$valenceWARAvg[m] <- passDat$negAvgWAR[which(passDat$passage==passage)]}
}
readDat$valCenter <- readDat$valenceWARAvg - 5.2

#organize data types
readDat$avgFreq <- as.numeric(readDat$avgFreq)
readDat$sdFreq <- as.numeric(readDat$sdFreq)
readDat$avgMag <- as.numeric(readDat$avgMag)
readDat$length <- as.numeric(readDat$length)

#output readDat
#write.csv(readDat, paste('/Users/jalexand/github/readAloud-valence-dataset/derivatives/analysisStimuli_readDat_', today, '.csv', sep="", collapse=NULL))

#calculate grand means
avgTotals <- data.frame(matrix(ncol=5, nrow=3))
colnames(avgTotals) <- c("variable", "prePos", "postPos", "preNeg", "postNeg")

dfPosPre <- readDat[readDat$position=="pre" & readDat$valence=="pos",] #subset into positive, preswitch data
posPreFreqAvg <- mean(as.numeric(dfPosPre$avgFreq))
posPreFreqSd <- mean(as.numeric(dfPosPre$sdFreq))
posPreValAvg <- mean(as.numeric(dfPosPre$valenceWARAvg))
posPreMagAvg <- mean(as.numeric(dfPosPre$avgMag))
posPreFleschAvg <- mean(as.numeric(dfPosPre$flesch))

dfPosPost <- readDat[readDat$position=="post" & readDat$valence=="pos",] #subset into positive, postswitch data
posPostFreqAvg <- mean(as.numeric(dfPosPost$avgFreq))
posPostFreqSd <- mean(as.numeric(dfPosPost$sdFreq))
posPostValAvg <- mean(as.numeric(dfPosPost$valenceWARAvg))
posPostMagAvg <- mean(as.numeric(dfPosPost$avgMag))
posPostFleschAvg <- mean(as.numeric(dfPosPost$flesch))

dfNegPre <- readDat[readDat$position=="pre" & readDat$valence=="neg",] #subset into negative, preswitch data
negPreFreqAvg <- mean(as.numeric(dfNegPre$avgFreq))
negPreFreqSd <- mean(as.numeric(dfNegPre$sdFreq))
negPreValAvg <- mean(as.numeric(dfNegPre$valenceWARAvg))
negPreMagAvg <- mean(as.numeric(dfNegPre$avgMag))
negPreFleschAvg <- mean(as.numeric(dfNegPre$flesch))

dfNegPost <- readDat[readDat$position=="post" & readDat$valence=="neg",] #subset into negative, postswitch data
negPostFreqAvg <- mean(as.numeric(dfNegPost$avgFreq))
negPostFreqSd <- mean(as.numeric(dfNegPost$sdFreq))
negPostValAvg <- mean(as.numeric(dfNegPost$valenceWARAvg))
negPostMagAvg <- mean(as.numeric(dfNegPost$avgMag))
negPostFleschAvg <- mean(as.numeric(dfNegPost$flesch))

avgTotals[1,] <- c("AvgFreq", posPreFreqAvg, posPostFreqAvg, negPreFreqAvg, negPostFreqAvg)
avgTotals[2,] <- c("SdFreq", posPreFreqSd, posPostFreqSd, negPreFreqSd, negPostFreqSd)
avgTotals[3,] <- c("AvgVal", posPreValAvg, posPostValAvg, negPreValAvg, negPostValAvg)
avgTotals[4,] <- c("AvgMag", posPreMagAvg, posPostMagAvg, negPreMagAvg, negPostMagAvg)
avgTotals[5,] <- c("AvgFlesch", posPreFleschAvg, posPostFleschAvg, negPreFleschAvg, negPostFleschAvg)

#organize data types
avgTotals$prePos <- as.numeric(avgTotals$prePos)
avgTotals$postPos <- as.numeric(avgTotals$postPos)
avgTotals$preNeg <- as.numeric(avgTotals$preNeg)
avgTotals$postNeg <- as.numeric(avgTotals$postNeg)


#FREQUENCY: not fully matched
#plot
ggplot(data=readDat, aes(x=position, y=avgFreq, fill=valence)) + geom_boxplot()

#compare averages
posPrevPostAvg <- t.test(x=as.numeric(dfPosPre$avgFreq), y=as.numeric(dfPosPost$avgFreq), alternative="two.sided")
negPrevPostAvg <- t.test(x=as.numeric(dfNegPre$avgFreq), y=as.numeric(dfNegPost$avgFreq), alternative="two.sided")
prePosvNegAvg <- t.test(x=as.numeric(dfPosPre$avgFreq), y=as.numeric(dfNegPre$avgFreq), alternative="two.sided") #significant
postPosvNegAvg <- t.test(x=as.numeric(dfPosPost$avgFreq), y=as.numeric(dfNegPost$avgFreq), alternative="two.sided")

#compare standard deviations
posPrevPostSd <- t.test(x=as.numeric(dfPosPre$sdFreq), y=as.numeric(dfPosPost$sdFreq), alternative="two.sided")
negPrevPostSd <- t.test(x=as.numeric(dfNegPre$sdFreq), y=as.numeric(dfNegPost$sdFreq), alternative="two.sided")
prePosvNegSd <- t.test(x=as.numeric(dfPosPre$sdFreq), y=as.numeric(dfNegPre$sdFreq), alternative="two.sided") #borderline significant
postPosvNegSd <- t.test(x=as.numeric(dfPosPost$sdFreq), y=as.numeric(dfNegPost$sdFreq), alternative="two.sided")


#VALENCE: manipulated
ggplot(data=readDat, aes(x=position, y=valenceWARAvg, fill=valence)) + geom_boxplot()

t.test(x=as.numeric(dfPosPre$valenceWARAvg), y=as.numeric(dfPosPost$valenceWARAvg), alternative="two.sided")
t.test(x=as.numeric(dfNegPre$valenceWARAvg), y=as.numeric(dfNegPost$valenceWARAvg), alternative="two.sided")
t.test(x=as.numeric(dfPosPre$valenceWARAvg), y=as.numeric(dfNegPre$valenceWARAvg), alternative="two.sided")
t.test(x=as.numeric(dfPosPost$valenceWARAvg), y=as.numeric(dfNegPost$valenceWARAvg), alternative="two.sided")


#VALENCE MAGNITUDE: matched
ggplot(data=readDat, aes(x=position, y=avgMag, fill=valence)) + geom_boxplot()

t.test(x=as.numeric(dfPosPre$avgMag), y=as.numeric(dfPosPost$avgMag), alternative="two.sided")
t.test(x=as.numeric(dfNegPre$avgMag), y=as.numeric(dfNegPost$avgMag), alternative="two.sided")
t.test(x=as.numeric(dfPosPre$avgMag), y=as.numeric(dfNegPre$avgMag), alternative="two.sided")
t.test(x=as.numeric(dfPosPost$avgMag), y=as.numeric(dfNegPost$avgMag), alternative="two.sided")


#FLESCH: matched
ggplot(data=readDat, aes(x=position, y=flesch, fill=valence)) + geom_boxplot()

t.test(x=as.numeric(dfPosPre$flesch), y=as.numeric(dfPosPost$flesch), alternative="two.sided")
t.test(x=as.numeric(dfNegPre$flesch), y=as.numeric(dfNegPost$flesch), alternative="two.sided")
t.test(x=as.numeric(dfPosPre$flesch), y=as.numeric(dfNegPre$flesch), alternative="two.sided")
t.test(x=as.numeric(dfPosPost$flesch), y=as.numeric(dfNegPost$flesch), alternative="two.sided")


#PLOTS
#passage characteristics (SNL poster)
plot1 <- ggplot(data=readDat, aes(x=passage, y=length, fill=valCenter, group=position)) + geom_col(width=0.8) +
          theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1, face="bold", size=10, color="black"),
                axis.text.y = element_text(size=10, color="black"),
                axis.title.x = element_text(size=13, face="bold", color="black"),
                axis.title.y = element_blank(),
                panel.grid.major = element_blank(), legend.position="top",
                panel.grid.minor = element_blank(), panel.background = element_blank(),
                legend.text = element_text(color="black"), legend.title = element_text(color="black")) +
          scale_fill_gradient(low="#e76e5b", high="#fccd25", name="Valence", breaks=c(-0.5, 0, 0.5, 1.0), labels=c("4.7", "5.2", "5.7", "6.2")) +
          ylab('Length in Words') + 
          coord_flip(ylim=c(-105,105)) +
          scale_y_continuous(labels=c("100", "50", "0", "50", "100")) +
          scale_x_discrete(position="top")

plot2 <- ggplot(data=readDat, aes(x=passage, y=length, fill=avgFreq, group=position)) + geom_col(width=0.8) +
          theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1, face="bold", size=10, color="black"),
                axis.text.y = element_text(size=10, color="black"),
                axis.title.x = element_text(size=13, face="bold", color="black"), axis.title.y = element_text(size=13, face="bold", color="black"),
                panel.grid.major = element_blank(), legend.position="top",
                panel.grid.minor = element_blank(), panel.background = element_blank(),
                legend.text = element_text(color="black"), legend.title = element_text(color="black")) +
          scale_fill_gradient(low="#9511a1", high="#2c0594", name="Frequency") +
          ylab('Length in Words') + xlab('Passage Name') +
          coord_flip(ylim=c(-105,105)) +
          scale_y_continuous(labels=c("100", "50", "0", "50", "100"))

comboPlot <- grid.arrange(plot2, plot1, ncol=2, top=textGrob("Passage Characteristics", gp=gpar(fontsize=20,font=2, color="black")))
ggsave(paste(out_path, "products/poster-neurolang2022/results/plot_stim1", "_", today, ".png", sep="", collapse=NULL),
       arrangeGrob(comboPlot))

#dolphins word clouds (SNL poster)
dolphinsDat <- read_xlsx(readAloudStimChar, sheet="dolphins", skip=1, na="#") #read in dolphin data for wordcloud
dolphinsDat$valenceStrengthWAR[is.na(dolphinsDat$valenceStrengthWAR)] <- 0
dolphinsDat$freq <- (dolphinsDat$valenceStrengthWAR*10)^2

dolphinsDatPre <- dolphinsDat[1:101, c("stimWord", "freq")]
dolphinsDatPre <- subset(dolphinsDatPre, !duplicated(dolphinsDatPre$stimWord))
dolphinsDatPre <- dolphinsDatPre[order(dolphinsDatPre$freq, decreasing=TRUE),]
dolphinsDatPre$freq[31:77] <- 100

dolphinsDatPost <- dolphinsDat[102:198, c("stimWord", "freq")]
dolphinsDatPost <- subset(dolphinsDatPost, !duplicated(dolphinsDatPost$stimWord))
dolphinsDatPost <- dolphinsDatPost[order(dolphinsDatPost$freq, decreasing=TRUE),]
dolphinsDatPost$freq[1:3] <- 700
dolphinsDatPost$freq[4:6] <- 500
dolphinsDatPost$freq[26:70] <- 100

wordcloud2(dolphinsDatPre, size=1, shape="pentagon", color=rep_len(c("#feb72d", "#f07f4f"), nrow(dolphinsDatPre)))
wordcloud2(dolphinsDatPost, size=1, shape="pentagon", color=rep_len(c("#e76e5b", "#d14e72"), nrow(dolphinsDatPost)))

#passage characteristics (paper)
#1: valence and length
plot1 <- ggplot(data=readDat, aes(x=passage, y=length, fill=valCenter, group=position)) + geom_col(width=0.8) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1, face="bold", size=10, color="black"),
        axis.text.y = element_blank(),
        axis.ticks.y = element_blank(),
        axis.title.x = element_text(size=13, face="bold", color="black"),
        axis.title.y = element_blank(),
        panel.grid.major = element_blank(), legend.position="right",
        panel.grid.minor = element_blank(), panel.background = element_blank(),
        legend.text = element_text(color="black"), legend.title = element_text(color="black")) +
  scale_fill_gradient(low="#202A44", high="#E1AD01", name="Valence", breaks=c(-0.5, 0, 0.5, 1.0), labels=c("4.7", "5.2", "5.7", "6.2")) +
  ylab('Length in Words') + 
  coord_flip(ylim=c(-105,105)) +
  scale_y_continuous(labels=c("100", "50", "0", "50", "100"))
cvd_grid(plot1)

#2: frequency
readDat$avgFreqPlot <- readDat$avgFreq
vec <- rep(c(-1,1), nrow(readDat)/2)
readDat$avgFreqPlot <- readDat$avgFreqPlot * vec

plot2 <- ggplot(data=readDat, aes(x=passage, y=avgFreqPlot, fill=position, group=position)) + geom_col(width=0.8) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1, face="bold", size=11, color="black"),
        axis.text.y = element_blank(),
        axis.title.x = element_text(size=13, face="bold", color="black"),
        axis.title.y = element_blank(),
        axis.ticks.y = element_blank(),
        panel.grid.major = element_blank(), legend.position="left",
        panel.grid.minor = element_blank(), panel.background = element_blank(),
        legend.text = element_text(color="black"), legend.title = element_text(color="black")) +
  scale_fill_manual(values = c(alpha("#999933", 0.7), "#882255", 0.7), name="Position",
                    labels=c("Postswitch", "Preswitch"), guide = guide_legend(reverse = TRUE)) +
  ylab('Average Log Frequency') + xlab('Passage Name') +
  coord_flip(ylim=c(-4,4)) +
  scale_y_continuous(labels=c("4.0", "2.0", "0", "2.0", "4.0"))
cvd_grid(plot2)

#3: name
readDat$placeholder <- rep(1, nrow(readDat))
readDat_trim <- readDat
toDelete <- seq(1, nrow(readDat), 2)
readDat_trim <- readDat_trim[toDelete,]

plot3 <- ggplot(data=readDat_trim, aes(x=passage, y=placeholder)) + geom_col(fill="white") + coord_flip() +
  geom_text(aes(y=0.5, label=passage)) +
  ylab("Name") +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1, face="bold", size=10, color="white"),
        axis.text.y = element_blank(),
        axis.title.x = element_text(size=13, face="bold", color="black"),
        axis.title.y = element_blank(),
        axis.ticks = element_blank(),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(), panel.background = element_blank()) +
  scale_y_continuous(labels=c("5.0", "2.5", "0", "2.5", "5.0"))

#combo:
comboPlot <- grid.arrange(plot2, plot3, plot1, ncol=3, widths=unit(c(4,2,4), c("in", "in", "in")), top=textGrob("Passage Characteristics", gp=gpar(fontsize=20,font=2, color="black")))
#cvd_grid(comboPlot)
ggsave(paste(out_path, "products/paper-readAloud/results/figure1_", today, ".png", sep="", collapse=NULL),
       arrangeGrob(comboPlot))