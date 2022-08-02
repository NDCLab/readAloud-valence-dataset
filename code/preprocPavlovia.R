# readAloud-valence-dataset PsychoPy/Pavlovia Preprocessing
# Author: Jessica M. Alexander
# (DCCS section is based upon a script written by Jessica M. Alexander, George A. Buzzell, Arina Polyanskaya in early 2022)
# Last Updated: 2022-08-02

### SECTION 1: SETTING UP
#set up date for output file naming
today <- Sys.Date()
today <- format(today, "%Y%m%d")

#set up directories for input/output data
#hpc
#input_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/sourcedata/checked/pavlovia/'
#out_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/derivatives/preprocessed/'
#local
input_path <- '/Users/jalexand/github/readAloud-valence-dataset/sourcedata/checked/pavlovia/'
out_path <- '/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/'

#identify participant folders within input dir
sub_folders <- list.files(input_path, pattern = "sub")

#create dataframes for storing output data and define output file names
#readAloud
readAloudSummaryDat <- data.frame(matrix(ncol=2, nrow=0))
colnames(readAloudSummaryDat) <- c("id", "challengeACC")
readAloud_out_subjectLevel <- paste("readAloud_subject-level_summary_", today, ".csv", sep="", collapse=NULL)

readAloudChallengeDat <- data.frame(matrix(ncol=1, nrow=20))
colnames(readAloudChallengeDat) <- c("passage")
readAloudChallengeDat[1,1] <- "A dam is a gateway that is designed to direct the flow of water. The first known dam was built in Jordan over 5000 years ago. An important ambition in the construction of a dam is to provide sufficient water, both for drinking and for cultivating local farmland. In modern history, this water has also been employed for its hydropower capabilities and dams have become a significant generator of electricity. Humans build these structures, but so do beavers. Using tree branches and vegetation to form their quirky lodges, beavers create an infrastructure that contributes positively to local wetlands."
readAloudChallengeDat[2,1] <- "Air travel today is very efficient, carrying jetsetters from one side of the globe to the other in a matter of hours. In the Sixties, however, traveling by airplane was a glamorous affair. Passengers got dressed up, the in-flight hospitality was luxurious, and everyone had lots of legroom. During this Golden Age of flying, champagne flowed freely at the bar and the guests were served lobster. It was like a cocktail party in the sky. With no one puking in the seat next to you or hogging the armrest."
readAloudChallengeDat[3,1] <- "Bats are the only flying mammal. The smallest has a six-inch wingspan; the wings of the largest, the flying foxes, extend over one and a half meters. Microbats send out ultrasonic sounds that produce echoes. The returning echoes allow them to “see” in their nightly quest for food. A different kind of bat, the megabat, eats fruit, which it finds with its senses of smell and vision."
readAloudChallengeDat[4,1] <- "Broccoli is great for heart health. High in fiber and various vitamins, this tasty vegetable has been found to support the immune system with its antioxidant properties. It originated in the northern Mediterranean during the Roman Empire and was brought to North America in the 19th century."
readAloudChallengeDat[5,1] <- "Buying a home is an exciting endeavor. Although it is a major financial commitment, it offers the opportunity to build your credit and grow your equity for the long-term. Selecting the right real estate agent is crucial since this person will advocate on your behalf during the negotiation process. You also want to secure a low interest rate."
readAloudChallengeDat[6,1] <- "Colony collapse disorder has been documented since 1869. Although its cause is still unidentified, its symptoms are manifest: a hive is abandoned by its bees, leaving behind the honey and the queen. It is currently speculated that colony collapse disorder is triggered by the interplay of multiple stressors, such as parasites, pesticides, and an inadequate diet. These rampant fears about colony collapse disorder concern one particular strain of bee that prospers worldwide, on every continent."
readAloudChallengeDat[7,1] <- "Dog shows, also called breed shows, are controversial. Some argue that they are detrimental to the welfare of the breed because, by selecting for shallow characteristics, they weaken genetics and engender abnormalities. This focus on the superficial, they contend, leads to disease, from which many competitors suffer. For example, pugs are bred with shortened skulls for the infamous squashed muzzle. But this distortion of the skull causes respiratory troubles and bulging eyeballs that are prone to injury."
readAloudChallengeDat[8,1] <- "Dolphins are intelligent sea creatures who mostly prefer warmer, tropical waters.  A thick layer of blubber helps with buoyancy and serves to streamline their flexible bodies.  They have excellent hearing, which is adapted for both air and water.  Sociable and playful, dolphins live in pods of up to a dozen individuals.  In Greek mythology, dolphins were esteemed as the helpers of humankind.  Seeing dolphins swimming in the wake of a ship was considered a good omen by the Ancient Greeks and many ancient coins pictured a young man riding on the back of a dolphin."
readAloudChallengeDat[9,1] <- "Even on frozen lakes and rivers, anglers can catch all kinds of interesting and edible fish. Before selecting a desirable location, these intrepid fishermen confirm that the ice is strong enough with a handy rhyme: “Thick and blue, tried and true.” This ensures that the ice is safe to walk on."
readAloudChallengeDat[10,1] <- "Gasoline-engine cars were once loud, dangerous, and expensive. These disadvantages were conquered in the early twentieth century. The noise emitted by the exhaust of an internal combustion engine was suppressed by the muffler. The difficulty of hand-cranking was eliminated with the electric starter. And mass manufacturing by Henry Ford decreased the price. The electric automobile was all but forgotten. But as concerns intensified around pollution and the cost of fuel, the dependence on gasoline no longer struck consumers as such a bargain."
readAloudChallengeDat[11,1] <- "Las Vegas was founded in the early twentieth century, but 1931 was the critical year in its urban development. The fledgling metropolis legalized casino gambling and dropped the minimum residency for divorce to six weeks. That year also marked the start of construction on the nearby Hoover Dam and the influx of laborers enabled Vegas to avoid catastrophe during the Depression. In the Fifties, before testing moved underground, nuclear weapons were detonated only 65 miles from downtown."
readAloudChallengeDat[12,1] <- "Lumens measure light emission. The human eyeball is unable to stare at anything discharging too many lumens, which is why a partial solar eclipse is so hazardous and deceptive. The parts of the Sun not obstructed by the Moon are just as blinding as they are on a typical day. In the blackout, the pupil dilates and each exposed cell on the retina is assaulted by rays of light. This literal “sunburn” causes lesions, inflicting irreversible damage."
readAloudChallengeDat[13,1] <- "Making caramel is a risky undertaking. Particles of sucrose and glucose are heated until they brown, then combined with fat to yield a sticky, elastic substance. The primary dangers are splatter and seizing, both of which threaten the moment that cold fat hits scalding sucrose. If the boiling mixture touches skin, it adheres and burns the flesh. If the mixture seizes, you are left with clumps of hard, useless sugar. If nothing goes wrong, then the consequence of this difficult process is a magical, chewy confection."
readAloudChallengeDat[14,1] <- "Six percent of the Earth’s surface is blanketed in rainforest. From the temperate forests of the Pacific Northwest to the tropical Congo, these evergreen canopies are the longest-living ecosystems on the planet. They are also a refuge of diversity, serving as home to a wealth of plant and animal species."
readAloudChallengeDat[15,1] <- "The first expedition to the South Pole was led by an explorer from the newly independent country of Norway. In the southern hemisphere, springtime occurs in October, so the courageous Norwegian team of five men and 52 dogs set off from their camp in mid-October 1911, hoping to reach the geographic South Pole. Skilled on skis, they traveled for two months and arrived, safe and sound, by mid-December. Victorious, they returned to civilization, pleased to have triumphed over the British expedition. The British team embarked on a similar quest via a different route with a fatal conclusion."
readAloudChallengeDat[16,1] <- "The Great Depression was a severe economic recession that had devastating, worldwide consequences. On October 29 of 1929, dubbed “Black Tuesday,” billions of dollars were lost and some investors were totally bankrupted. In the United States, unemployment shot up to 23%. It was especially hard on farmers in the Great Plains, who suffered a decline in crop prices and a punishing drought that crippled their economy. Herbert Hoover became president just before the crash and was long scorned for his refusal to involve the federal government in relief efforts."
readAloudChallengeDat[17,1] <- "The great horned owl is a nocturnal bird native to the Americas. It is easily recognized by its tufted feather “horns,” called plumicorns, and its large, yellow eyes. A symbol of strength, courage, and beauty, the great horned owl has an unmistakable hoot, four to five syllables in length. Special feathers allow it to fly soundlessly through the twilight as it skillfully seeks its next meal, often a rabbit or a hare. A surprising victim of this formidable predator is the skunk. "
readAloudChallengeDat[18,1] <- "The grizzly is a subspecies of the brown bear, notorious for its aggressive tendencies. Weighing over four hundred pounds, grizzlies use their formidable size to frighten opponents. If size fails to terrify, their long claws and fearsome bite can inflict considerable damage. Their claws are four inches long and the grizzly jaw is strong enough to crack a bowling ball."
readAloudChallengeDat[19,1] <- "The mantis shrimp is a puny but aggressive crustacean who works alone and leaves its solitary burrow merely to hunt. There are two categories of mantis shrimp. “Spearers” have pointy, barbed forelimbs that they use to stab and snag their prey. “Smashers” bludgeon their victims with an oversized, club-like appendage. This terrifying weapon strikes at the same velocity as a gunshot; it is so fast that it makes bubbles in the water around the unfortunate adversary. The mantis shrimp’s poor victim is hit twice: first by the claw and then by the shockwave, either of which is deadly."
readAloudChallengeDat[20,1] <- "Tooth decay and gum disease are infections that can increase your risk for diabetes and heart trouble. This is why regular dental appointments are critical. But some people are terrified of going to the dentist. This fear of drills, needles, and oral pain can cause those who suffer from it to avoid the dentist. Ironically, this only inflates the probability of cavities and other dental problems."

readAloud_out_passageLevel <- paste("readAloud_passage-level_summary_", today, ".csv", sep="", collapse=NULL)

#ldt
ldtSummaryDat <- data.frame(matrix(ncol=11, nrow=0))
colnames(ldtSummaryDat) <- c("id", "ldtACC", "ldtWord_meanACC", "ldtNonce_meanACC", "ldtWordCorr_meanRT", "ldtNonceCorr_meanRT", "ldtWordCorr_logMeanRT", "ldtNonceCorr_logMeanRT", "ldt_costAcc", "ldt_costRT", "ldt_costLogRT")
ldt_out_subjectLevel <- paste("ldt_subject-level_summary_", today, ".csv", sep="", collapse=NULL)
                                     
ldtTrialDat <- data.frame(matrix(ncol = 6, nrow = 0))
colnames(ldtTrialDat) <- c("id", "trial_no", "acc", "rt", "stimString", "wordType")
ldt_out_trialLevel <- paste("ldt_trial-level_summary_", today, ".csv", sep="", collapse=NULL)                             

#dccs
dccsSummaryDat <- data.frame(matrix(ncol=22, nrow=0))
colnames(dccsSummaryDat) <- c("id",
                              "shapePracticePass",
                              "colorPracticePass",
                              "dccsACC",
                              "toShape_meanACC",
                              "toShapePRE_meanACC",
                              "toShapeCorr_meanRT",
                              "toShapePRECorr_meanRT",
                              "toShapeCorr_logMeanRT",
                              "toShapePRECorr_logMeanRT",
                              "toShape_costACC",
                              "toShape_costRT",
                              "toShape_costLogRT",
                              "toColor_meanACC",
                              "toColorPRE_meanACC",
                              "toColorCorr_meanRT",
                              "toColorPRECorr_meanRT",
                              "toColorCorr_logMeanRT",
                              "toColorPRECorr_logMeanRT",
                              "toColor_costACC",
                              "toColor_costRT",
                              "toColor_costLogRT")
dccs_out_subjectLevel <- paste("dccs_subject-level_summary_", today, ".csv", sep="", collapse=NULL)

dccsTrialDat <- data.frame(matrix(ncol = 5, nrow = 0))
colnames(dccsTrialDat) <- c("id", "trial_no", "acc", "rt", "trial_type")
dccs_out_trialLevel <- paste("dccs_trial-level_summary_", today, ".csv", sep="", collapse=NULL)


### SECTION 2: START PARTICIPANT LOOP AND CLEAN INCOMING DATAFRAME
#loop over participants (subfolders)
for(i in 1:length(sub_folders)){
  
  #for this participant, find the dccs csv file
  psychopy_file <- list.files(paste(input_path,sub_folders[i], sep = "", collapse = NULL), pattern = "*.csv")
  
  #logical to make sure there is a dccs file for this participant before loading, else skip to next participant
  if (!identical(psychopy_file, character(0))) {
    print(paste("Woohoo! Processing ", sub_folders[i], "!"))
  
    #read in the data for this participant, establish id, and remove extraneous variables
    psychopyDat <- read.csv(file = paste(input_path,sub_folders[i],'/',psychopy_file, sep = "", collapse = NULL), stringsAsFactors = FALSE, na.strings=c("", "NA"))
    id <- psychopyDat$id[1]
    psychopyDatTrim <- psychopyDat[c("id",
                                     "firstListA",
                                     "secondListA",
                                     "challengeResponse1.corr",
                                     "challengeResponse2.corr",
                                     "ldtPracticeResponse.corr",
                                     "ldtResponse.corr",
                                     "ldtResponse.rt",
                                     "trials_3.thisN",
                                     "ldtStim",
                                     "wordType",
                                     "shapePracticeResponse.corr",
                                     "trials_4.thisN",
                                     "colorPracticeResponse.corr",
                                     "trials_5.thisN",
                                     "dccsResponse.corr",
                                     "dccsResponse.rt",
                                     "cue")]
    
    ### SECTION 3: READALOUD PROCESSING
    #establish dataframe for answers to challenge questions
    readAloudDatA <- psychopyDatTrim[!is.na(psychopyDatTrim$firstListA),]
    readAloudDatA <- readAloudDatA[c("id", "firstListA", "challengeResponse1.corr")]
    colnames(readAloudDatA) <- c("id", "passage", "challengeACC")
    readAloudDatB <- psychopyDatTrim[!is.na(psychopyDatTrim$secondListA),]
    readAloudDatB <- readAloudDatB[c("id", "secondListA", "challengeResponse2.corr")]
    colnames(readAloudDatB) <- c("id", "passage", "challengeACC")
    
    readAloudDat <- rbind(readAloudDatA, readAloudDatB)
    readAloudDat <- readAloudDat[order(readAloudDat$passage),]
    
    #calculate accuracy for individual participant
    challengeACC <- mean(readAloudDat$challengeACC)
    
    #store output data in summary matrices
    readAloudSummaryDat[nrow(readAloudSummaryDat) + 1,] <-c(id,challengeACC)

    newcol <- ncol(readAloudChallengeDat) + 1
    readAloudChallengeDat[newcol] <- readAloudDat$challengeACC
    names(readAloudChallengeDat)[newcol] <- id
    
    
    ### SECTION 4: LDT PREPROCESSING
    #establish dataframe for experimental data
    ldtDat <- psychopyDatTrim[!is.na(psychopyDatTrim$trials_3.thisN),]
    ldtDat <- ldtDat[c("id", "ldtResponse.corr", "ldtResponse.rt", "trials_3.thisN", "ldtStim", "wordType")]
    
    #calculate overall participant accuracy
    ldtACC <- mean(ldtDat$ldtResponse.corr)
    
    #subset the data for word versus nonce trials, create new dataframes for each
    ldtDat_word <- ldtDat[ldtDat$wordType=="word",]
    ldtDat_nonce <- ldtDat[ldtDat$wordType=="nonce",]
    
    #compute mean accuracy for word versus nonce trials
    ldtWord_meanACC <- mean(ldtDat_word$ldtResponse.corr)
    ldtNonce_meanACC <- mean(ldtDat_nonce$ldtResponse.corr)
    
    #subset the data for correct trials only, separately for word versus nonce trials, creating new dataframes for each
    ldtDat_wordCorr <- ldtDat_word[ldtDat_word$ldtResponse.corr==1, ]
    ldtDat_nonceCorr <- ldtDat_nonce[ldtDat_nonce$ldtResponse.corr==1, ]
    
    #for correct trials, for both word and nonce groups, compute mean RT (raw and log-corrected)
    ldtWordCorr_meanRT <- mean(ldtDat_wordCorr$ldtResponse.rt)
    ldtNonceCorr_meanRT <- mean(ldtDat_nonceCorr$ldtResponse.rt)
    
    ldtWordCorr_logMeanRT <- mean(log((1+ldtDat_wordCorr$ldtResponse.rt)))
    ldtNonceCorr_logMeanRT <- mean(log((1+ldtDat_nonceCorr$ldtResponse.rt)))
    
    #compute delta scores for accuracy, RT, log-RT
    ldt_costAcc <-  ldtWord_meanACC - ldtNonce_meanACC
    ldt_costRT <- ldtNonceCorr_meanRT - ldtWordCorr_meanRT
    ldt_costLogRT <- ldtNonceCorr_logMeanRT - ldtWordCorr_logMeanRT
    
    #store output data in summary matrices
    ldtSummaryDat[nrow(dccsSummaryDat) + 1,] <-c(id,
                                                 ldtACC,
                                                 ldtWord_meanACC,
                                                 ldtNonce_meanACC,
                                                 ldtWordCorr_meanRT,
                                                 ldtNonceCorr_meanRT,
                                                 ldtWordCorr_logMeanRT,
                                                 ldtNonceCorr_logMeanRT,
                                                 ldt_costAcc,
                                                 ldt_costRT,
                                                 ldt_costLogRT)
    
    for (j in 1:nrow(ldtDat)){
      trial_no <- j
      acc <- ldtDat$ldtResponse.corr[j]
      rt <- ldtDat$ldtResponse.rt[j]
      stimString <- ldtDat$ldtStim[j]
      wordType <- ldtDat$wordType[j]
      
      ldtTrialDat[nrow(ldtTrialDat) + 1,] <-c(id, trial_no, acc, rt, stimString, wordType)
      }
    
    ### SECTION 5: DCCS PREPROCESSING
    #verify practice trials were completed successfully (up to three rounds of four trials possible, confirm that last four trials yield at least three correct)
    dccsShapePracticeDat <- psychopyDatTrim[!is.na(psychopyDatTrim$trials_4.thisN),]
    dccsShapePracticeDat <- dccsShapePracticeDat[c("id", "shapePracticeResponse.corr","trials_4.thisN")]
    noShapePracticeTrials <- length(dccsShapePracticeDat$trials_4.thisN)
    dccsShapePracticeDat <- dccsShapePracticeDat[(noShapePracticeTrials-3):noShapePracticeTrials,]
    shapePractice_accuracy <- mean(dccsShapePracticeDat$shapePracticeResponse.corr)
    if(shapePractice_accuracy >= 0.75){
      shapePracticePass <- 1
    } else{
      shapePracticePass <- 0
    }
    
    dccsColorPracticeDat <- psychopyDatTrim[!is.na(psychopyDatTrim$trials_5.thisN),]
    dccsColorPracticeDat <- dccsColorPracticeDat[c("id", "colorPracticeResponse.corr","trials_5.thisN")]
    noColorPracticeTrials <- length(dccsColorPracticeDat$trials_5.thisN)
    dccsColorPracticeDat <- dccsColorPracticeDat[(noColorPracticeTrials-3):noColorPracticeTrials,]
    colorPractice_accuracy <- mean(dccsColorPracticeDat$colorPracticeResponse.corr)
    if(colorPractice_accuracy >= 0.75){
      colorPracticePass <- 1
    } else{
      colorPracticePass <- 0
    }
    
    #establish dataframe for experimental data
    dccsDat <- psychopyDatTrim[psychopyDatTrim$cue %in% c("SHAPE", "COLOR"),]
    dccsDat <- dccsDat[c("id",
                         "dccsResponse.corr",
                         "dccsResponse.rt",
                         "cue")]
    
    #calculate overall participant accuracy
    dccsACC <- mean(dccsDat$dccsResponse.corr)
      
    #add new vectors to dataframe to enable pairwise comparisons: prior cue, prior cue accuracy, following cue, and following cue accuracy
    priorCue <- c("HOLD", dccsDat$cue)
    dccsDat$priorCue <- priorCue[1:(length(priorCue)-1)]
    
    priorCueAcc <- c(2, dccsDat$dccsResponse.corr)
    dccsDat$priorCueAcc <- priorCueAcc[1:(length(priorCueAcc)-1)]
    
    nextCue <- c(dccsDat$cue[2:(length(dccsDat$cue))], "HOLD")
    dccsDat$nextCue <- nextCue
    
    nextCueAcc <- c(dccsDat$dccsResponse.corr[2:(length(dccsDat$dccsResponse.corr))], 2)
    dccsDat$nextCueAcc <- nextCueAcc

    #create new vector identifying if either switch and preswitch trial were answered erroneously, TRUE if either switch or preswitch was error
    dccsDat$toShapeSwitchPairErr <- (dccsDat$cue == "COLOR" & dccsDat$nextCue == "SHAPE" & (!dccsDat$dccsResponse.corr | !dccsDat$nextCueAcc)) | 
                                        (dccsDat$cue == "SHAPE" & (!dccsDat$dccsResponse.corr | !dccsDat$priorCueAcc))
    dccsDat$toColorSwitchPairErr <- (dccsDat$cue == "SHAPE" & (!dccsDat$dccsResponse.corr | !dccsDat$nextCueAcc)) | 
                                        (dccsDat$cue == "COLOR" & dccsDat$priorCue == "SHAPE" & (!dccsDat$dccsResponse.corr | !dccsDat$priorCueAcc))
    
    #remove first two trials
    dccsDat <- dccsDat[3:nrow(dccsDat),]
    
    #TOSHAPE: switch defined as switch to the infrequent condition (SHAPE)
    #subset the data for switch and preswitch trials
    dccsDat_toShapePairs <- subset(dccsDat, (dccsDat$cue=="SHAPE" | dccsDat$nextCue=="SHAPE"))
    if(dccsDat_toShapePairs$cue[1]=="SHAPE"){
      dccsDat_toShapePairs <- dccsDat_toShapePairs[2:length(dccsDat_toShapePairs$cue),] #remove first row because no COLOR trial follows final SHAPE trial
    }
      
    dccsDat_toShape <- subset(dccsDat_toShapePairs, dccsDat_toShapePairs$cue == "SHAPE")
    dccsDat_toShapePRE <- subset(dccsDat_toShapePairs, dccsDat_toShapePairs$nextCue == "SHAPE")
    
    #compute mean accuracy for switch versus preswitch trials
    toShape_meanACC <- mean(dccsDat_toShape$dccsResponse.corr)
    toShapePRE_meanACC <- mean(dccsDat_toShapePRE$dccsResponse.corr)
    
    #subset the data for correct trial pairs only, creating new dataframes for each
    dccsDat_toShapeCorr <- dccsDat_toShape[!dccsDat_toShape$toShapeSwitchPairErr, ]
    dccsDat_toShapePRECorr <- dccsDat_toShapePRE[!dccsDat_toShapePRE$toShapeSwitchPairErr, ]
    
    #for correct trials, compute mean RT (raw and log-corrected)
    toShapeCorr_meanRT <- mean(dccsDat_toShapeCorr$dccsResponse.rt)
    toShapePRECorr_meanRT <- mean(dccsDat_toShapePRECorr$dccsResponse.rt)
    
    toShapeCorr_logMeanRT <- mean(log((1+dccsDat_toShapeCorr$dccsResponse.rt)))
    toShapePRECorr_logMeanRT <- mean(log((1+dccsDat_toShapePRECorr$dccsResponse.rt)))

    #compute switch cost scores for accuracy, RT, log-RT
    toShape_costACC <-  toShapePRE_meanACC - toShape_meanACC
    toShape_costRT <- toShapeCorr_meanRT - toShapePRECorr_meanRT
    toShape_costLogRT <- toShapeCorr_logMeanRT - toShapePRECorr_logMeanRT

    #TOCOLOR: switch defined as switch back to the frequent condition (COLOR) from the infrequent condition (SHAPE)
    #subset the data for switch and preswitch trials
    dccsDat_toColorPairs <- dccsDat[dccsDat$cue=="SHAPE" | dccsDat$priorCue=="SHAPE",]
    dccsDat_toColorPairs <- dccsDat_toColorPairs[1:length(dccsDat_toColorPairs$cue)-1,] #remove last row because no COLOR trial follows final SHAPE trial
    
    dccsDat_toColor <- subset(dccsDat_toColorPairs, dccsDat_toColorPairs$priorCue == "SHAPE")
    dccsDat_toColorPRE <- subset(dccsDat_toColorPairs, dccsDat_toColorPairs$cue == "SHAPE")
    
    #compute mean accuracy for switch versus preswitch trials
    toColor_meanACC <- mean(dccsDat_toColor$dccsResponse.corr)
    toColorPRE_meanACC <- mean(dccsDat_toColorPRE$dccsResponse.corr)
    
    #subset the data for correct trial pairs only, creating new dataframes for each
    dccsDat_toColorCorr <- dccsDat_toColor[!dccsDat_toColor$toColorSwitchPairErr, ]
    dccsDat_toColorPRECorr <- dccsDat_toColorPRE[!dccsDat_toColorPRE$toColorSwitchPairErr, ]
    
    #for correct trials, compute mean RT (raw and log-corrected)
    toColorCorr_meanRT <- mean(dccsDat_toColorCorr$dccsResponse.rt)
    toColorPRECorr_meanRT <- mean(dccsDat_toColorPRECorr$dccsResponse.rt)
    
    toColorCorr_logMeanRT <- mean(log((1+dccsDat_toColorCorr$dccsResponse.rt)))
    toColorPRECorr_logMeanRT <- mean(log((1+dccsDat_toColorPRECorr$dccsResponse.rt)))
    
    #compute switch cost scores for accuracy, RT, log-RT
    toColor_costACC <-  toColorPRE_meanACC - toColor_meanACC
    toColor_costRT <- toColorCorr_meanRT - toColorPRECorr_meanRT
    toColor_costLogRT <- toColorCorr_logMeanRT - toColorPRECorr_logMeanRT
    
    #store output data in summary matrices
    dccsSummaryDat[nrow(dccsSummaryDat) + 1,] <-c(id,
                                          shapePracticePass,
                                          colorPracticePass,
                                          dccsACC,
                                          toShape_meanACC,
                                          toShapePRE_meanACC,
                                          toShapeCorr_meanRT,
                                          toShapePRECorr_meanRT,
                                          toShapeCorr_logMeanRT,
                                          toShapePRECorr_logMeanRT,
                                          toShape_costACC,
                                          toShape_costRT,
                                          toShape_costLogRT,
                                          toColor_meanACC,
                                          toColorPRE_meanACC,
                                          toColorCorr_meanRT,
                                          toColorPRECorr_meanRT,
                                          toColorCorr_logMeanRT,
                                          toColorPRECorr_logMeanRT,
                                          toColor_costACC,
                                          toColor_costRT,
                                          toColor_costLogRT)
    
    for (j in 1:nrow(dccsDat)){
      trial_no <- j
      acc <- dccsDat$dccsResponse.corr[j]
      rt <- dccsDat$dccsResponse.rt[j]
      if (dccsDat$cue[j]=="SHAPE"){
        trial_type <- "toShape"
      }
      else if (dccsDat$nextCue[j]=="SHAPE"){
        trial_type <- "toShapePRE"
      }
      else if (dccsDat$priorCue[j]=="SHAPE"){
        trial_type <- "toColor"
      }
      else {
        trial_type <- "otherColor"
      }

      dccsTrialDat[nrow(dccsTrialDat) + 1,] <-c(id, trial_no, acc, rt, trial_type)
    }
  }
  
#if participant did not have a PsychoPy file, skip to next participant
  else {
  print(paste("Booo! Missing file for ", sub_folders[i], "..."))
}
}

### SECTION 6: READALOUD GROUP AVERAGE
#calculate group average for readAloudChallengeDat and append to dataframe
currentNoCols <- ncol(readAloudChallengeDat)
newCol <- currentNoCols + 1
readAloudChallengeDat[newCol] <- rowMeans(readAloudChallengeDat[,2:currentNoCols])
names(readAloudChallengeDat)[newCol] <- c("groupAvg")

### SECTION 7: OUTPUT DATA
#write the extracted summary scores to CSV
write.csv(readAloudChallengeDat,paste(out_path,readAloud_out_passageLevel, sep = "", collapse = NULL), row.names=FALSE)
write.csv(readAloudSummaryDat,paste(out_path,readAloud_out_subjectLevel, sep = "", collapse = NULL), row.names=FALSE)
write.csv(ldtSummaryDat,paste(out_path,ldt_out_subjectLevel, sep = "", collapse = NULL), row.names=FALSE)
write.csv(ldtTrialDat,paste(out_path,ldt_out_trialLevel, sep = "", collapse = NULL), row.names=FALSE)
write.csv(dccsSummaryDat,paste(out_path,dccs_out_subjectLevel, sep = "", collapse = NULL), row.names=FALSE)
write.csv(dccsTrialDat,paste(out_path,dccs_out_trialLevel, sep = "", collapse = NULL), row.names=FALSE)

### SECTION 8: UPDATE CENTRAL TRACKER FOR STUDY
#load central tracker
#track_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/data-monitoring/central-tracker_readAloud-valence.csv'
track_path <- '/Users/jalexand/github/readAloud-valence-dataset/data-monitoring/central-tracker_readAloud-valence.csv'
trackerDat <- read.csv(track_path, header=TRUE, check.names=FALSE)

#readAloudChallenge_s1_r1_e1
for (row in 1:nrow(readAloudSummaryDat)) {
  accuracy <- readAloudSummaryDat[row, "challengeACC"]
  id <- readAloudSummaryDat[row, "id"]
  if (accuracy >= 0.7) {
    trackerDat[trackerDat$id == id, ]$readAloudChallenge_s1_r1_e1 = "1"
  } else {
    trackerDat[trackerDat$id == id, ]$readAloudChallenge_s1_r1_e1 = "0"
  } 
}
print("Updated readAloudChallenge_s1_r1_e1!")

#ldt_s1_r1_e1
for (row in 1:nrow(ldtSummaryDat)) {
  accuracy <- ldtSummaryDat[row, "ldtACC"]
  id <- ldtSummaryDat[row, "id"]
  if (accuracy >= 0.8) {
    trackerDat[trackerDat$id == id, ]$ldt_s1_r1_e1 = "1"
  } else {
    trackerDat[trackerDat$id == id, ]$ldt_s1_r1_e1 = "0"
  } 
}
print("Updated ldt_s1_r1_e1!")

#dccs_s1_r1_e1
for (row in 1:nrow(dccsSummaryDat)) {
  accuracy <- dccsSummaryDat[row, "dccsACC"]
  id <- dccsSummaryDat[row, "id"]
  shapePass <- dccsSummaryDat[row, "shapePracticePass"]
  colorPass <- dccsSummaryDat[row, "colorPracticePass"]
  if (accuracy >= 0.8 && shapePass && colorPass) {
    trackerDat[trackerDat$id == id, ]$dccs_s1_r1_e1 = "1"
  } else {
    trackerDat[trackerDat$id == id, ]$dccs_s1_r1_e1 = "0"
  } 
}
print("Updated dccs_s1_r1_e1!")

#write back to central tracker
write.csv(trackerDat, track_path, row.names = FALSE)