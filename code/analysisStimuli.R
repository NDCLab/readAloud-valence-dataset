# readAloud-valence-dataset ReadAloud Task Stimuli Characteristics
# Author: Jessica M. Alexander
# Last Updated: 2023-06-14

# INPUTS
# Inputs are characteristics of the passages read aloud by participants, specifically:
# passage_list: list of the names of all 20 passage stimuli
# switchDat: information on the switch word in each passage
# passDat: information on each unique word in each passage, flesch scores for passage halves
# scaffolds: a mapping of each syllable in each passage to the index of its associated word
# warriner: valence ratings (details below)
# subtlexus: log10 word frequency ratings (details below)

# OUTPUTS
# readDat: for each passage half (pre/post), details on:
    # switchType: indication of whether passage is pos2neg or neg2pos
    # valence: binary valence (pos or neg)
    # lengthSyll: total number of syllables
    # lengthWord: total number of words
    # avgSyllPerWord: average number of syllables in each word
    # avgFreq: log10 word frequency averaged over all words (imputation of median for missing values)
    # avgVal: word valence averaged over all words (imputation of median for missing values)
    # questionHalf: binary indication of whether the comprehension question was drawn from this specific passage half
    # flesh: Flesch reading ease score
# anovas and plots to confirm matching and/or manipulation of stimuli characteristics (console output)
# passage characteristics plots for publication

# NOTES
# A prior iteration of this script included stimuli characteristics for a lexical decision task, as well as outputs
# for the initial poster presentation and preprint.  In response to reviewer comments, the script was updated in
# April 2023 and those aspects were archived in an older copy of the script, residing within this same folder. In addition,
# syllable length in the prior version of the script was incorrectly drawn from the length of the lemma; the error
# has been corrected here. Lastly, the process to identify frequency and valence values from the respective corpora
# was refined and missing values were imputed to the corpus median.


### SECTION 1: SETTING UP
library(readxl) #load excel files
library(textstem) #lemmatize_words function

#visualization tools
library(ggplot2)
library(gridExtra)
library(grid)
library(cowplot)
library(colorspace)
library(colorblindr)

#set up date for output file naming
today <- Sys.Date()
today <- format(today, "%Y%m%d")

#set up directories for input/output
# main_dataset <- '/Users/jalexand/github/readAloud-valence-dataset/'
main_dataset <- '~/Documents/ndclab/analysis-sandbox/rwe-dataset/'
# out_path_readDat <- '/Users/jalexand/github/readAloud-valence-dataset/derivatives/'
out_path_readDat <- paste(main_dataset, 'derivatives', sep = '')
# out_path_plots <- '/Users/jalexand/github/readAloud-valence-alpha/'
out_path_plots <- paste(out_path_readDat, 'plots/')

#load input files
passage_list <- list.files(paste(main_dataset, 'materials/readAloud-ldt/stimuli/readAloud/liwc-analysis/input', sep="", collapse="NULL"))
scaffolds <- paste(main_dataset, 'code/scaffolds.xlsx', sep="", collapse=NULL)
readAloudStimChar <- paste(main_dataset, 'materials/readAloud-ldt/stimuli/readAloud/readAloud-stimuli_characteristics.xlsx', sep="", collapse=NULL)
warriner_path <- paste(main_dataset, 'materials/readAloud-ldt/stimuli/resources/BRM-emot-submit_downloaded_2021-08-08.csv', sep="", collapse=NULL) #downloaded from https://link.springer.com/article/10.3758/s13428-012-0314-x on 08/08/2021
SUBList <- paste(main_dataset, 'materials/readAloud-ldt/stimuli/resources/SUBTLEXus74286wordstextversion.txt', sep="", collapse=NULL) #downloaded from https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus on 06/13/2022

switchDat <- read_xlsx(readAloudStimChar, sheet="switches", skip=1, na="#")
passDat <- read_xlsx(readAloudStimChar, sheet="passages", na="#")
warriner <- read.csv(warriner_path)
subtlexus <- read.table(SUBList, header=TRUE)
subtlexus$Word <- tolower(subtlexus$Word) #make all entries in SUBTLEXUS lower-case


### SECTION 2: SET UP PASSAGE LIST AND PREPARE LEMMAS FOR ACCESSING FREQUENCY INFO
passages <- c()
for(i in 1:length(passage_list)){
  passages <- c(passages, strsplit(passage_list[i], "_")[[1]][1])
}
passages <- unique(passages)

#create manual mapping of words to SUBTLEXUS corpus when lemma doesn't automatically match
manualLemma <- data.frame(matrix(ncol=2, nrow=0)) #initialize a table to hold words without a frequency match
colnames(manualLemma) <- c("stimWord",
                       "lemma")
for(i in 1:length(passages)){
  passage <- passages[i]
  passageDat <- read_xlsx(readAloudStimChar, sheet=passage, skip=1, na="#") #read in passage data
  passWords <- passageDat[,1:2] #pull word list
  for(a in 1:length(passWords$stimWord)){        #correct apostrophes (curly to straight)
    string <- passWords$stimWord[a]
    passWords$stimWord[a] <- gsub("’", "'",string)
  }
  passWords$stimWord <- tolower(passWords$stimWord) #shift word list to lowercase to match SUBTLEXUS
  passWords$lemma <- lemmatize_words(passWords$stimWord) #lemmatize word list
  passWords$freq <- rep(0, nrow(passWords)) #initialize new column to hold word frequency data
  for(f in 1:nrow(passWords)){        #add log word frequency from SUBTLEXUS corpus for each word lemma in the passage
    passWords$freq[f] <- subtlexus$Lg10WF[match(passWords$lemma[f], subtlexus$Word)]
  }
  noFreqTable <- subset(passWords, is.na(passWords$freq))[,2:3] #extract words that did not get a frequency match
  manualLemma <- rbind(manualLemma, noFreqTable) #bind to running table of words without a frequency match
}
manualLemma <- manualLemma[!duplicated(manualLemma$stimWord),] #remove duplicate rows
manualLemma <- manualLemma[order(manualLemma$stimWord),] #alphabetize
manualLemma$newLemma <- c(rep(0,nrow(manualLemma))) #initialize column to hold manual lemmas extracted by researcher
for(lemma in 1:nrow(manualLemma)){       #manually adjust possessives by dropping "'s" (except for "it's")
  string <- manualLemma$lemma[lemma]
  if(substr(string, nchar(string)-1, nchar(string))=="'s" & string!="it's"){
    manualLemma$newLemma[lemma] <- substr(string, 0, nchar(string)-2)
    }
}
#manually adjust plurals
manualLemma[match("brittles", manualLemma$stimWord),3] <- "brittle"
#manually adjust adjectives
manualLemma[match("club-like", manualLemma$stimWord),3] <- "club"
manualLemma[match("in-flight", manualLemma$stimWord),3] <- "flight"
manualLemma[match("mid-", manualLemma$stimWord),3] <- "middle"
#no manual adjustment of the following categories:
#compound words with no obvious "primary" lemma: ccc, don't, it's, long-term
#proper nouns: delano, nissan
#words simply not in the SUBTLEXUS database: ecotourism, hydropower, jetsetter, megabat, microbats, photoreceptor, plumicorn, powertrain, spearer, trinocular
#ordinal numbers: nineteeth, second, twentieth
manualLemma <- subset(manualLemma, manualLemma$newLemma!=0) #drop words without a manual mapping
manualLemma$freq <- rep(0, nrow(manualLemma))       #add log word frequency from SUBTLEXUS corpus
for(f in 1:nrow(manualLemma)){
  manualLemma$freq[f] <- subtlexus$Lg10WF[match(manualLemma$newLemma[f], subtlexus$Word)]
}
manualLemma$val <- rep(0, nrow(manualLemma))       #add valence from Warriner corpus
for(g in 1:nrow(manualLemma)){
  manualLemma$val[g] <- warriner$V.Mean.Sum[match(manualLemma$newLemma[g], warriner$Word)]
}


### SECTION 3: BUILD AND OUTPUT READDAT MATRIX
readDat <- data.frame(matrix(ncol=10, nrow=0))
colnames(readDat) <- c("passage",
                       "switchType",
                       "position",
                       "valence",
                       "lengthSyll",
                       "lengthWord",
                       "avgSyllPerWord",
                       "avgFreq",
                       "avgVal",
                       "questionHalf")

#calculate characteristics per passage half
for(j in 1:length(passages)){
  passage <- passages[j]
  passageDat <- read_xlsx(readAloudStimChar, sheet=passage, skip=1, na="#") #read in passage word list
  scaffDat <- read_xlsx(scaffolds, sheet=passage) #read in passage scaffold

  #extract data from passDat
  switchType <- passDat$switchType[match(passage, passDat$passage)] #identify passage switch type (neg2pos or pos2neg)
  questionVal <- passDat$questionVal[match(passage, passDat$passage)] #identify whether comprehension question came from positive or negative passage half
  preSwitchVal <- substr(switchType, 1, 3) #identify valence of preswitch passage half (pos or neg)
  postSwitchVal <-substr(switchType, 5, 7) #identify valence of postswitch passage half (pos or neg)
  preQuestion <- as.numeric(questionVal==preSwitchVal) #mark as 1 if question came from first passage half, 0 otherwise
  postQuestion <- as.numeric(questionVal==postSwitchVal) #mark as 1 if question came from second passage half, 0 otherwise

  #extract data from switchDat
  switchWord <- switchDat$switchWord[match(passage, switchDat$passage)] #identify passage switch word

  #extract data from scaffDat
  scaffSwitch <- match("switch", scaffDat$wordGroup) #identify index of start of passage switch word in scaffDat
  preLenSyll <- scaffSwitch - 1 #identify number of syllables in first passage half
  postLenSyll <- length(scaffDat$wordGroup) - preLenSyll #identify number of syllables in second passage half
  preLenWord <- sum(scaffDat$wordOnset[1:(scaffSwitch - 1)]) #identify number of words in first passage half
  postLenWord <- sum(scaffDat$wordOnset) - preLenWord #identify number of words in second passage half
  preSyllPerWord <- preLenSyll/preLenWord
  postSyllPerWord <- postLenSyll/postLenWord

  #extract passage word list
  passWords <- passageDat[,1:2] #pull word list
  for(a in 1:length(passWords$stimWord)){        #correct apostrophes (curly to straight)
    string <- passWords$stimWord[a]
    passWords$stimWord[a] <- gsub("’", "'",string)
  }
  passWords$stimWord <- tolower(passWords$stimWord) #shift word list to lowercase to match SUBTLEXUS
  passWords$lemma <- lemmatize_words(passWords$stimWord) #lemmatize word list

  #add frequency data
  passWords$freq <- rep(0, nrow(passWords)) #initialize column to hold frequency data
  for(f in 1:nrow(passWords)){
    if(!is.na(subtlexus$Lg10WF[match(passWords$stimWord[f], subtlexus$Word)])){           #automatic matching of full word to SUBTLEXUS corpus
      passWords$freq[f] <- subtlexus$Lg10WF[match(passWords$stimWord[f], subtlexus$Word)]
    } else if(!is.na(subtlexus$Lg10WF[match(passWords$lemma[f], subtlexus$Word)])){       #automatic matching of lemma to SUBTLEXUS corpus
      passWords$freq[f] <- subtlexus$Lg10WF[match(passWords$lemma[f], subtlexus$Word)]
    } else if (passWords$lemma[f] %in% manualLemma$lemma){                                #check manual table if no auto-match
      passWords$freq[f] <- manualLemma$freq[match(passWords$lemma[f], manualLemma$lemma)]
    } else {passWords$freq[f] <- median(subtlexus$Lg10WF)}                                #impute median value for non-matches
  }

  #add valence data
  passWords$val <- rep(0, nrow(passWords)) #initialize column to hold valence data
  for(v in 1:nrow(passWords)){
    if(!is.na(warriner$V.Mean.Sum[match(passWords$stimWord[v], warriner$Word)])){           #automatic matching of full word to Warriner corpus
      passWords$val[v] <- warriner$V.Mean.Sum[match(passWords$stimWord[v], warriner$Word)]
    } else if(!is.na(warriner$V.Mean.Sum[match(passWords$lemma[v], warriner$Word)])){       #automatic matching of lemma to Warriner corpus
      passWords$val[v] <- warriner$V.Mean.Sum[match(passWords$lemma[v], warriner$Word)]
    } else if (passWords$lemma[v] %in% manualLemma$lemma){                                  #check manual table if no auto-match
      passWords$val[v] <- manualLemma$val[match(passWords$lemma[v], manualLemma$lemma)]
    } else {passWords$val[v] <- median(warriner$V.Mean.Sum)}                                #impute median value for non-matches
  }

  #identify index of passage switch word in passWords matrix
  passSwitch <- match(switchWord, passWords$stimWord)

  #calculate average frequency
  preFreqAvg <- mean(passWords$freq[1:(passSwitch-1)]) #calculate mean frequency for preswitch half
  postFreqAvg <- mean(passWords$freq[passSwitch:length(passWords$freq)]) #calculate mean frequency for postswitch half

  #calculate average valence
  preValAvg <- mean(passWords$val[1:(passSwitch-1)]) #calculate mean valence for preswitch half
  postValAvg <- mean(passWords$val[passSwitch:length(passWords$val)]) #calculate mean valence for postswitch half

  #create vectors for each half and add to readDat
  vectorPre <- c(passage, switchType, "pre", preSwitchVal, preLenSyll, preLenWord, preSyllPerWord, preFreqAvg, preValAvg, preQuestion)
  readDat[nrow(readDat) + 1,] <- c(vectorPre)
  vectorPost <- c(passage, switchType, "post", postSwitchVal, postLenSyll, postLenWord, postSyllPerWord, postFreqAvg, postValAvg, postQuestion)
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
readDat$position <- as.factor(readDat$position)
readDat$switchType <- as.factor(readDat$switchType)
readDat$valence <- as.factor(readDat$valence)
readDat$avgFreq <- as.numeric(readDat$avgFreq)
readDat$avgVal <- as.numeric(readDat$avgVal)
readDat$lengthSyll <- as.numeric(readDat$lengthSyll)
readDat$lengthWord <- as.numeric(readDat$lengthWord)
readDat$avgSyllPerWord <- as.numeric(readDat$avgSyllPerWord)

#output readDat
write.csv(readDat, paste(out_path_readDat, 'analysisStimuli_readDat_', today, '.csv', sep="", collapse=NULL))
out_path_readDat_csv <- paste(out_path_readDat, 'analysisStimuli_readDat_', today, '.csv', sep="", collapse=NULL)


### SECTION 4: CALCULATE FULL PASSAGE LENGTHS, ADD TO PASSDAT, CALCULATE RANGE
for(u in 1:nrow(passDat)){
  passage <- passDat$passage[u]
  passDatTemp <- readDat[which(readDat$passage==passage),]
  lengthSyll <- sum(passDatTemp$lengthSyll)
  lengthWord <- sum(passDatTemp$lengthWord)
  passDat$lengthSyll[u] <- lengthSyll
  passDat$lengthWord[u] <- lengthWord
}
summary(passDat$lengthWord)
summary(passDat$lengthSyll)


### SECTION 5: CONFIRM MATCH/MANIPULATED STIMULI CHARACTERISTICS
#FREQUENCY: matched
ggplot(data=readDat, aes(x=position, y=avgFreq, fill=valence)) + geom_boxplot()
summary(aov(avgFreq ~ position * valence, data=readDat))

#VALENCE: manipulated
ggplot(data=readDat, aes(x=position, y=avgVal, fill=valence)) + geom_boxplot()
summary(aov(avgVal ~ position * valence, data=readDat))
summary(readDat$avgVal[which(readDat$valence=="pos")])
summary(readDat$avgVal[which(readDat$valence=="neg")])

#FLESCH: matched
ggplot(data=readDat, aes(x=position, y=flesch, fill=valence)) + geom_boxplot()
summary(aov(flesch ~ position * valence, data=readDat))

#LENGTH IN WORDS: matched
ggplot(data=readDat, aes(x=position, y=lengthWord, fill=valence)) + geom_boxplot()
summary(aov(lengthWord ~ position * valence, data=readDat))

#LENGTH IN SYLLABLES: matched
ggplot(data=readDat, aes(x=position, y=lengthSyll, fill=valence)) + geom_boxplot()
summary(aov(lengthSyll ~ position * valence, data=readDat))

#AVERAGE SYLLABLES PER WORD: matched
ggplot(data=readDat, aes(x=position, y=avgSyllPerWord, fill=valence)) + geom_boxplot()
summary(aov(avgSyllPerWord ~ position * valence, data=readDat))


### SECTION 6: PASSAGE CHARACTERISTICS PLOTS
readDat$lengthWordPlot <- readDat$lengthWord * c(-1,1) #shift preswitch word length to negative
readDat$avgFreqPlot <- readDat$avgFreq * c(-1,1) #shift preswitch word frequency to negative
readDat$valCenterPlot <- (5.2-readDat$avgVal) * -1 #add distance from median for plot #1 color

#1: valence and length
plot1 <- ggplot(data=readDat, aes(x=passage, y=lengthWordPlot, fill=valCenterPlot, group=position)) + geom_col(width=0.8) +
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
#cvd_grid(plot1) #test colors

#2: frequency
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
#cvd_grid(plot2) #test colors

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
#cvd_grid(comboPlot) #test colors
ggsave(paste(out_path_plots, "products/paper-readAloud/results/figure1_", today, ".png", sep="", collapse=NULL),
       arrangeGrob(comboPlot))
