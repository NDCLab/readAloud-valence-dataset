# readAloud-valence-dataset Stimuli Frequency
# Authors: Jessica M. Alexander
# Last Updated: 2023-04-25


### SECTION 1: SETTING UP
library(readxl) #load excel files
library(textstem) #lemmatize_words function

#visualization tools
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
scaffolds <- paste(main_dataset, 'code/scaffolds.xlsx', sep="", collapse=NULL)
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
subtlexus$Word <- tolower(subtlexus$Word) #make all entries in SUBTLEXUS lower-case


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

#create manual mapping of words to SUBTLEXUS corpus when lemma doesn't automatically match
noFreq <- data.frame(matrix(ncol=2, nrow=0)) #initialize a table to hold words without a frequency match
colnames(noFreq) <- c("stimWord",
                       "lemma")
for(i in 1:length(passages)){
  passage <- passages[i]
  passageDat <- read_xlsx(readAloudStimChar, sheet=passage, skip=1, na="#") #read in passage data
  passWords <- passageDat[,1:2] #pull word list
  for(a in 1:length(passWords$stimWord)){ #correct apostrophes (curly to straight)
    string <- passWords$stimWord[a]
    passWords$stimWord[a] <- gsub("’", "'",string)
  } 
  passWords$stimWord <- tolower(passWords$stimWord) #shift word list to lowercase to match SUBTLEXUS
  passWords$lemma <- lemmatize_words(passWords$stimWord) #lemmatize word list
  passWords$freq <- rep(0, nrow(passWords)) #add log word frequency from SUBTLEXUS corpus for each word lemma in the passage
  for(f in 1:nrow(passWords)){
    passWords$freq[f] <- subtlexus$Lg10WF[match(passWords$lemma[f], subtlexus$Word)]
  }
  noFreqTable <- subset(passWords, is.na(passWords$freq))[,2:3] #extract words that did not get a frequency match
  noFreq <- rbind(noFreq, noFreqTable) #bind to running table of words without a frequency match
}
noFreq <- noFreq[!duplicated(noFreq$stimWord),] #remove duplicate rows
noFreq <- noFreq[order(noFreq$stimWord),] #alphabetize df
noFreq$manualLemma <- c(rep(0,nrow(noFreq))) #initialize column to hold manual lemmas extracted by researcher
for(lemma in 1:nrow(noFreq)){ #manually adjust possessives
  string <- noFreq$lemma[lemma]
  if(substr(string, nchar(string)-1, nchar(string))=="'s" & string!="it's"){
    noFreq$manualLemma[lemma] <- substr(string, 0, nchar(string)-2)
    }
}
#manually adjust plurals
noFreq[match("brittles", noFreq$stimWord),3] <- "brittle"
#manually adjust adjectives
noFreq[match("club-like", noFreq$stimWord),3] <- "club"
noFreq[match("in-flight", noFreq$stimWord),3] <- "flight"
noFreq[match("mid-", noFreq$stimWord),3] <- "middle"
#ccc, don't, it's, long-term: compound words with no obvious "primary" lemma
#delano, nissan: proper nouns
#ecotourism, hydropower, jetsetter, megabat, microbats, photoreceptor, plumicorn, powertrain, spearer, trinocular: words not in database
#nineteeth, second, twentieth: ordinal numbers ("second" may have different connotations than "two")
noFreq <- subset(noFreq, noFreq$manualLemma!=0) #drop words without a manual mapping
noFreq$freq <- rep(0, nrow(noFreq)) #add log word frequency from SUBTLEXUS corpus
for(f in 1:nrow(noFreq)){
  noFreq$freq[f] <- subtlexus$Lg10WF[match(noFreq$manualLemma[f], subtlexus$Word)]
}


readDat <- data.frame(matrix(ncol=9, nrow=0))
colnames(readDat) <- c("passage",
                     "position",
                     "valence",
                     "lengthSyll",
                     "lengthWord",
                     "avgSyllPerWord",
                     "avgFreq",
                     "avgVal",
                     "avgValTest")

#calculate characteristics per passage half
for(j in 1:length(passages)){
  passage <- passages[j]
  passageDat <- read_xlsx(readAloudStimChar, sheet=passage, skip=1, na="#") #read in passage data
  scaffDat <- read_xlsx(scaffolds, sheet=passage) #read in passage scaffold
  
  #extract data from switchDat
  switchType <- switchDat$switchType[match(passage, switchDat$passage)] #identify passage switch type (neg2pos or pos2neg)
  preSwitchVal <- substr(switchType, 1, 3) #identify valence of preswitch passage half (pos or neg)
  postSwitchVal <-substr(switchType, 5, 7) #identify valence of postswitch passage half (pos or neg)
  switchWord <- switchDat$switchWord[match(passage, switchDat$passage)] #identify passage switch word
  
  #extract data from scaffDat
  scaffSwitch <- match("switch", scaffDat$wordGroup) #identify index of passage switch word in scaffDat
  preLenSyll <- scaffSwitch - 1 #identify number of syllables in first passage half
  postLenSyll <- length(scaffDat$wordGroup) - preLenSyll #identify number of syllables in second passage half
  preLenWord <- sum(scaffDat$wordOnset[1:(scaffSwitch - 1)]) #identify number of syllables in first passage half
  postLenWord <- sum(scaffDat$wordOnset) - preLenWord #identify number of syllables in second passage half
  preSyllPerWord <- preLenSyll/preLenWord
  postSyllPerWord <- postLenSyll/postLenWord
  
  #extract passage word list
  passWords <- passageDat[,1:2] #pull word list
  for(a in 1:length(passWords$stimWord)){ #correct apostrophes (curly to straight)
    string <- passWords$stimWord[a]
    passWords$stimWord[a] <- gsub("’", "'",string)
  }
  passWords$stimWord <- tolower(passWords$stimWord) #shift word list to lowercase to match SUBTLEXUS
  passWords$lemma <- lemmatize_words(passWords$stimWord) #lemmatize word list
  
  #add frequency data
  passWords$freq <- rep(0, nrow(passWords)) #add log word frequency from SUBTLEXUS corpus for each word lemma in the passage
  for(f in 1:nrow(passWords)){
    if(!is.na(subtlexus$Lg10WF[match(passWords$lemma[f], subtlexus$Word)])){
      passWords$freq[f] <- subtlexus$Lg10WF[match(passWords$lemma[f], subtlexus$Word)]
    } else if (passWords$lemma[f] %in% noFreq$lemma){
      passWords$freq[f] <- noFreq$freq[match(passWords$lemma[f], noFreq$lemma)]
    }
  }
  
  #add valence data
  passWords$val <- rep(0, nrow(passWords)) #add word valence from Warriner corpus for each word lemma in the passage
  for(v in 1:nrow(passWords)){
    passWords$val[v] <- warriner$V.Mean.Sum[match(passWords$lemma[v], warriner$Word)]
  }
  passWords$test <- passWords$val #make test copy of val column CHECKME
  for(x in 1:nrow(passWords)){if(is.na(passWords$test[x])){passWords$test[x] <- 5.2}} #impute median value CHECKME
  passSwitch <- match(switchWord, passWords$stimWord) #identify index of passage switch word in passWords matrix
  
  #calculate average frequency
  preFreqAvg <- mean(passWords$freq[1:(passSwitch-1)], na.rm=TRUE) #calculate mean frequency for preswitch half
  postFreqAvg <- mean(passWords$freq[passSwitch:length(passWords$freq)], na.rm=TRUE) #calculate mean frequency for postswitch half
  
  #calculate average valence
  preValAvg <- mean(passWords$val[1:(passSwitch-1)], na.rm=TRUE) #calculate mean valence for preswitch half
  postValAvg <- mean(passWords$val[passSwitch:length(passWords$val)], na.rm=TRUE) #calculate mean valence for postswitch half
  
  #calculate average valence w/imputed values CHECKME
  preValTestAvg <- mean(passWords$test[1:(passSwitch-1)], na.rm=TRUE) #calculate mean valence for preswitch half
  postValTestAvg <- mean(passWords$test[passSwitch:length(passWords$test)], na.rm=TRUE) #calculate mean valence for postswitch half
  
  vectorPre <- c(passage, "pre", preSwitchVal, preLenSyll, preLenWord, preSyllPerWord, preFreqAvg, preValAvg, preValTestAvg)
  readDat[nrow(readDat) + 1,] <- c(vectorPre)
  
  vectorPost <- c(passage, "post", postSwitchVal, postLenSyll, postLenWord, postSyllPerWord, postFreqAvg, postValAvg, postValTestAvg)
  readDat[nrow(readDat) + 1,] <- c(vectorPost)
}

#add flesch reading score to readDat
for(k in 1:nrow(readDat)){
  passage <- readDat$passage[k]
  valence <- readDat$valence[k]
  if(valence=='pos'){readDat$flesch[k] <- passDat$fleschPOS[which(passDat$passage==passage)]}
  else{readDat$flesch[k] <- passDat$fleschNEG[which(passDat$passage==passage)]}
}

#organize data types
readDat$avgFreq <- as.numeric(readDat$avgFreq)
readDat$avgVal <- as.numeric(readDat$avgVal)
readDat$avgValTest <- as.numeric(readDat$avgValTest)
readDat$lengthSyll <- as.numeric(readDat$lengthSyll)
readDat$lengthWord <- as.numeric(readDat$lengthWord)
readDat$avgSyllPerWord <- as.numeric(readDat$avgSyllPerWord)

#output readDat
#write.csv(readDat, paste('/Users/jalexand/github/readAloud-valence-dataset/derivatives/analysisStimuli_readDat_', today, '.csv', sep="", collapse=NULL))

#calculate grand means
avgTotals <- data.frame(matrix(ncol=5, nrow=3))
colnames(avgTotals) <- c("variable", "prePos", "postPos", "preNeg", "postNeg")

dfPosPre <- readDat[readDat$position=="pre" & readDat$valence=="pos",] #subset into positive, preswitch data
posPreFreqAvg <- mean(as.numeric(dfPosPre$avgFreq))
posPreValAvg <- mean(as.numeric(dfPosPre$avgVal))
posPreValTestAvg <- mean(as.numeric(dfPosPre$avgValTest))
posPreFleschAvg <- mean(as.numeric(dfPosPre$flesch))

dfPosPost <- readDat[readDat$position=="post" & readDat$valence=="pos",] #subset into positive, postswitch data
posPostFreqAvg <- mean(as.numeric(dfPosPost$avgFreq))
posPostValAvg <- mean(as.numeric(dfPosPost$avgVal))
posPostValTestAvg <- mean(as.numeric(dfPosPost$avgValTest))
posPostFleschAvg <- mean(as.numeric(dfPosPost$flesch))

dfNegPre <- readDat[readDat$position=="pre" & readDat$valence=="neg",] #subset into negative, preswitch data
negPreFreqAvg <- mean(as.numeric(dfNegPre$avgFreq))
negPreValAvg <- mean(as.numeric(dfNegPre$avgVal))
negPreValTestAvg <- mean(as.numeric(dfNegPre$avgValTest))
negPreFleschAvg <- mean(as.numeric(dfNegPre$flesch))

dfNegPost <- readDat[readDat$position=="post" & readDat$valence=="neg",] #subset into negative, postswitch data
negPostFreqAvg <- mean(as.numeric(dfNegPost$avgFreq))
negPostValAvg <- mean(as.numeric(dfNegPost$avgVal))
negPostValTestAvg <- mean(as.numeric(dfNegPost$avgValTest))
negPostFleschAvg <- mean(as.numeric(dfNegPost$flesch))

avgTotals[1,] <- c("AvgFreq", posPreFreqAvg, posPostFreqAvg, negPreFreqAvg, negPostFreqAvg)
avgTotals[2,] <- c("AvgVal", posPreValAvg, posPostValAvg, negPreValAvg, negPostValAvg)
avgTotals[3,] <- c("AvgValTest", posPreValTestAvg, posPostValTestAvg, negPreValTestAvg, negPostValTestAvg)
avgTotals[4,] <- c("AvgFlesch", posPreFleschAvg, posPostFleschAvg, negPreFleschAvg, negPostFleschAvg)

#organize data types
avgTotals$prePos <- as.numeric(avgTotals$prePos)
avgTotals$postPos <- as.numeric(avgTotals$postPos)
avgTotals$preNeg <- as.numeric(avgTotals$preNeg)
avgTotals$postNeg <- as.numeric(avgTotals$postNeg)
readDat$position <- as.factor(readDat$position)
readDat$valence <- as.factor(readDat$valence)


#FREQUENCY: not fully matched
#plot
ggplot(data=readDat, aes(x=position, y=avgFreq, fill=valence)) + geom_boxplot()
summary(aov(avgFreq ~ position * valence, data=readDat))


#VALENCE: manipulated
ggplot(data=readDat, aes(x=position, y=avgVal, fill=valence)) + geom_boxplot()
summary(aov(avgVal ~ position * valence, data=readDat))


#VALENCE TEST: manipulated
ggplot(data=readDat, aes(x=position, y=avgValTest, fill=valence)) + geom_boxplot()
summary(aov(avgValTest ~ position * valence, data=readDat))


#FLESCH: matched
ggplot(data=readDat, aes(x=position, y=flesch, fill=valence)) + geom_boxplot()
summary(aov(flesch ~ position * valence, data=readDat))


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