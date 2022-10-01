# readAloud-valence-dataset Valence Timestamp Coder Correlation
# Author: Jessica M. Alexander
# Last Updated: 2022-09-09

### SECTION 1: SETTING UP
library(readxl) #read_xlsx function
library(irr) # icc function
library(ggplot2) #plotting

#set up directories for data
#set up directories for input/output data
main_dataset <- '/Users/jalexand/github/readAloud-valence-dataset/'
out_path <- '/Users/jalexand/github/readAloud-valence-alpha/derivatives/'

code_path <- paste(main_dataset, 'derivatives/preprocessed/valence-timing/', sep="", collapse=NULL)


### SECTION 2: CREATE CROSS-CODED DF
cross_df <- data.frame(matrix(ncol=6, nrow=0))
colnames(cross_df) <- c("passage", "readStart", "switchWordStart", "readEnd", "notes", "id")

crossList <- list.files(paste(code_path, 'crosscode', sep="", collapse=NULL))

for(i in 1:length(crossList)){
  subject <- as.numeric(substr(crossList[i], 5, 10))
  crossFile <- read_xlsx(paste(code_path, 'crosscode/', crossList[i], sep="", collapse=NULL))
  crossFile <- crossFile[!is.na(crossFile$readStart),] #limit selection to passages coded by expert
  crossFile$id <- rep(subject, nrow(crossFile))
  cross_df <- rbind(cross_df, crossFile)
}

cross_df$label <- paste(cross_df$Passage, cross_df$id, sep="-", collapse=NULL) #create label of passage+subject


### SECTION 3: CREATE CODER DFs
#lg
lg_df <- data.frame(matrix(ncol=6, nrow=0))
colnames(lg_df) <- c("passage", "readStart", "switchWordStart", "readEnd", "notes", "id")

lgList <- list.files(paste(code_path, 'coders/lg', sep="", collapse=NULL))

for(lg in 1:length(lgList)){
  subject <- as.numeric(substr(lgList[lg], 5, 10))
  lgFile <- read_xlsx(paste(code_path, 'coders/lg/', lgList[lg], sep="", collapse=NULL))
  lgFile$id <- rep(subject, nrow(lgFile))
  lg_df <- rbind(lg_df, lgFile)
}

lg_df$label <- paste(lg_df$Passage, lg_df$id, sep="-", collapse=NULL) #create label of passage+subject
lg_df_trim <- lg_df[which(lg_df$label %in% cross_df$label),] #limit to passages cross-coded by expert
lg_df_trim <- subset(lg_df_trim, select=-c(Passage, Notes, id, label)) #drop columns to create numerical array

cross_df_lg <- cross_df[which(cross_df$label %in% lg_df$label),] #limit cross_df to passages coded by this coder
cross_df_lg <- subset(cross_df_lg, select=-c(Passage, Notes, id, label)) #drop columns to create numerical array

#mr
mr_df <- data.frame(matrix(ncol=6, nrow=0))
colnames(mr_df) <- c("passage", "readStart", "switchWordStart", "readEnd", "notes", "id")

mrList <- list.files(paste(code_path, 'coders/mr', sep="", collapse=NULL))

for(mr in 1:length(mrList)){
  subject <- as.numeric(substr(mrList[mr], 5, 10))
  mrFile <- read_xlsx(paste(code_path, 'coders/mr/', mrList[mr], sep="", collapse=NULL))
  mrFile$id <- rep(subject, nrow(mrFile))
  mr_df <- rbind(mr_df, mrFile)
}

mr_df$label <- paste(mr_df$Passage, mr_df$id, sep="-", collapse=NULL) #create label of passage+subject
mr_df_trim <- mr_df[which(mr_df$label %in% cross_df$label),] #limit to passages cross-coded by expert
mr_df_trim <- subset(mr_df_trim, select=-c(Passage, Notes, id, label)) #drop columns to create numerical array

cross_df_mr <- cross_df[which(cross_df$label %in% mr_df$label),] #limit cross_df to passages coded by this coder
cross_df_mr <- subset(cross_df_mr, select=-c(Passage, Notes, id, label)) #drop columns to create numerical array

### SECTION 4: CREATE VECTORS IN MILLISECONDS
cross_lg_vector <- as.vector(unlist(cross_df_lg))*1000
lg_vector <- as.vector(unlist(lg_df_trim))*1000
lg_for_icc <- cbind(cross_lg_vector, lg_vector) #combine expert and coder (lg) data

cross_mr_vector <- as.vector(unlist(cross_df_mr))*1000
cross_mr_vector[249] <- 0 #imputing value for missing datapoint that is consistent between coder and cross-coder
mr_vector <- as.vector(unlist(mr_df_trim))*1000
mr_vector[249] <- 0 #imputing value for missing datapoint that is consistent between coder and cross-coder
mr_for_icc <- cbind(cross_mr_vector, mr_vector) #combine expert and coder (mr) data


### SECTION 4: CALCULATE MEAN AND SD OF 
#lg
delta_lg <- cross_lg_vector - lg_vector
mean_delta_lg <- mean(delta_lg)
mean_sd_lg <- sd(delta_lg)

lower_conf_lg <- mean_delta_lg - (1.96 * mean_sd_lg)
upper_conf_lg <- mean_delta_lg + (1.96 * mean_sd_lg)

#mr
delta_mr <- cross_mr_vector - mr_vector
mean_delta_mr <- mean(delta_mr)
mean_sd_mr <- sd(delta_mr)

lower_conf_mr <- mean_delta_mr - (1.96 * mean_sd_mr)
upper_conf_mr <- mean_delta_mr + (1.96 * mean_sd_mr)


### SECTION 5: PLOT BLAND-ALTMAN, 95% LIMITS OF AGREEMENT
#lg
lg_for_bland_altman <- data.frame(lg_for_icc)
colnames(lg_for_bland_altman) <- c('expert', 'coder')
lg_for_bland_altman$avg <- rowMeans(lg_for_bland_altman)
lg_for_bland_altman$delta <- lg_for_bland_altman$expert - lg_for_bland_altman$coder

ggplot(lg_for_bland_altman, aes(x=avg, y=delta)) +
  geom_point(size=2) +
  xlim(-100, 1250010) +
  ylim(-60000, 12500) +
  geom_hline(yintercept=mean_delta_lg) +
  geom_hline(yintercept=lower_conf_lg, color='red', linetype='dashed') +
  annotate('text', x=1160000, y=(lower_conf_lg-2000), color='red', size=3, label='AVG - 1.96*SD') +
  geom_hline(yintercept=upper_conf_lg, color='red', linetype='dashed') +
  annotate('text', x=1160000, y=(upper_conf_lg+2000), color='red', size=3, label='AVG + 1.96*SD') +
  ggtitle('Bland-Altman Plot (LG)') +
  ylab('Delta Between Expert and Coder (ms)') +
  xlab('Average Timestamp (ms)')

#mr
mr_for_bland_altman <- data.frame(mr_for_icc)
colnames(mr_for_bland_altman) <- c('expert', 'coder')
mr_for_bland_altman$avg <- rowMeans(mr_for_bland_altman)
mr_for_bland_altman$delta <- mr_for_bland_altman$expert - mr_for_bland_altman$coder

ggplot(mr_for_bland_altman, aes(x=avg, y=delta)) +
  geom_point(size=2) +
  xlim(-100, 1500010) +
  geom_hline(yintercept=mean_delta_mr) +
  geom_hline(yintercept=lower_conf_mr, color='red', linetype='dashed') +
  annotate('text', x=1400000, y=(lower_conf_mr-75), color='red', size=3, label='AVG - 1.96*SD') +
  geom_hline(yintercept=upper_conf_mr, color='red', linetype='dashed') +
  annotate('text', x=1400000, y=(upper_conf_mr+75), color='red', size=3, label='AVG + 1.96*SD') +
  ggtitle('Bland-Altman Plot (MR)') +
  ylab('Delta Between Expert and Coder (ms)') +
  xlab('Average Timestamp (ms)')


### SECTION 6: RUN CORRELATIONS
icc(lg_for_icc, 'twoway', 'agreement', 'single')
icc(mr_for_icc, 'twoway', 'agreement', 'single')