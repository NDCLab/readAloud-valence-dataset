# readAloud-valence-dataset Inter-Rater Reliability for Error Coding
# Authors: Jessica M. Alexander, George A. Buzzell, Lucas Sahar
# Last Updated: 2022-11-14

### SECTION 1: SETTING UP
library(readxl)
library(irr)

#set up date for output file naming
today <- Sys.Date()
today <- format(today, "%Y%m%d")

#set up directories for input/output data
#hpc
#scaffolds <- '/home/data/NDClab/datasets/readAloud-valence-dataset/code/scaffolds.xlsx'
#input_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/derivatives/preprocessed/error-coding/'
#out_path <- '/home/data/NDClab/datasets/readAloud-valence-dataset/derivatives/preprocessed/'
#local
scaffolds <- '/Users/jalexand/github/readAloud-valence-dataset/code/scaffolds.xlsx'
input_path <- '/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/error-coding/testing-new-protocol/'
out_path <- '/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/'

#create vectors of passage names
valencePassages <- c("antarctica",
                    "bats",
                    "bees",
                    "broccoli",
                    "caramel",
                    "cars",
                    "congo",
                    "dams",
                    "dentist",
                    "depression",
                    "dogshow",
                    "dolphins",
                    "flying",
                    "grizzly",
                    "icefishing",
                    "mantis",
                    "realty",
                    "skunkowl",
                    "sun",
                    "vegas")

#identify participant folders within input dir
sub_folders <- list.files(input_path)

#create dataframe for storing output data and define output file name
kappaSummaryDat <- data.frame(matrix(ncol=14, nrow=0))
colnames(kappaSummaryDat) <- c("id", "passageName",
                               "kappaMispron_adls", "kappaMispron_adbr", "kappaMispron_lsbr",
                               "kappaElong_adls", "kappaElong_adbr", "kappaElong_lsbr",
                               "kappaHes_adls", "kappaHes_adbr", "kappaHes_lsbr",
                               "fleissMispron", "fleissElong", "fleissHes")
kappa_out <- paste("interrater-reliability-by-passage_", today, ".csv", sep="", collapse=NULL)


### SECTION 2: START PARTICIPANT LOOP
#loop over participants (subfolders)
for(i in 1:length(sub_folders)){
    
  #identify participant id
  id <- strsplit(sub_folders[i], "-")[[1]][2]
  print(paste("Starting loop for sub-", id, sep="", collapse=NULL))

  
  ### SECTION 3: VALENCE CODER LOOP
  allValence <- list.files(paste(input_path,sub_folders[i], sep = "", collapse = NULL))
  
  #prime matrices for study team set of coders
  ad <- data.frame(matrix(ncol=9, nrow=0))
  br <- data.frame(matrix(ncol=9, nrow=0))
  ls <- data.frame(matrix(ncol=9, nrow=0))
  
  #loop over coders (subfolders)
  for(p in 1:length(allValence)){
    
    #identify coder
    coder <- strsplit(allValence[p], "_")[[1]][2]
    
    #identify list of passages
    allPassageFiles <- list.files(paste(input_path, sub_folders[i], "/", allValence[p], sep = "", collapse = NULL))
    
    ### SECTION 4: VALENCE PASSAGE LOOP
    #loop over coded passages (subfiles)
    for(q in 1:length(valencePassages)){
      passageName <- valencePassages[q]
      passageNameXLSX <- paste(passageName, ".xlsx", sep="", collapse=NULL)
      passageIdx <- match(passageNameXLSX, allPassageFiles)
      passageFile <- paste(input_path, sub_folders[i], "/", allValence[p], "/", allPassageFiles[passageIdx], sep = "", collapse = NULL)
      
      passageScaffold <- read_xlsx(scaffolds, sheet=passageName)
      
      #read in coded file for passage
      errorData <- read_xlsx(passageFile, sheet=NULL, range=anchored("B2", dim=c(8, length(passageScaffold$syllable_id)), col_names=FALSE))
      errorDataT <- t(errorData) #transpose matrix
      colnames(errorDataT) <- c("mispron", "insert", "omit", "wordstress", "filledp", "hesitation", "elongation")
      errorDataT <- data.frame(errorDataT) #convert matrix to dataframe
      
      #add passage name as new column for future subsetting
      errorDataT$passage <- rep(passageName, nrow(errorDataT))
      errorDataT$sub <- rep(as.numeric(id), nrow(errorDataT)) #add subject id for visual inspection during debugging
      
      #bind coded data to matrix for specific coder
      if(coder=="ad"){
        ad <- rbind(ad, errorDataT)
        ad[, 1:7] <- as.numeric(as.matrix(ad[, 1:7]))
      } else if(coder=="ls"){
        ls <- rbind(ls, errorDataT)
        ls[, 1:7] <- as.numeric(as.matrix(ls[, 1:7]))
      } else if(coder=="br"){
        br <- rbind(br, errorDataT)
        br[, 1:7] <- as.numeric(as.matrix(br[, 1:7]))
      } else{
        print("Oops. Couldn't find that coder.")
      }
    }
  }    
  
  ### SECTION 5: RE-LOOP VALENCE PASSAGES TO CALCULATE COHEN'S D
  for(r in 1:length(valencePassages)){
    passageName <- valencePassages[r]
    
    #trim coder dataframes down to specific passage
    adTrim <- ad[ad$passage==passageName,]
    lsTrim <- ls[ls$passage==passageName,]
    brTrim <- br[br$passage==passageName,]
    
    #create arrays for each error type across coders for this particular passage
    mispron <- cbind(adTrim$mispron, lsTrim$mispron, brTrim$mispron)
    elongation <- cbind(adTrim$elongation, lsTrim$elongation, brTrim$elongation)
    hesitation <- cbind(adTrim$hesitation, lsTrim$hesitation, brTrim$hesitation)
    
    #calculate kappas
    kappaMispron_adls <- kappa2(mispron[, c(1,2)])$value
    kappaMispron_adbr <- kappa2(mispron[, c(1,3)])$value    
    kappaMispron_lsbr <- kappa2(mispron[, c(2,3)])$value
    
    kappaElong_adls <- kappa2(elongation[, c(1,2)])$value
    kappaElong_adbr <- kappa2(elongation[, c(1,3)])$value
    kappaElong_lsbr <- kappa2(elongation[, c(2,3)])$value
    
    kappaHes_adls <- kappa2(hesitation[, c(1,2)])$value
    kappaHes_adbr <- kappa2(hesitation[, c(1,3)])$value
    kappaHes_lsbr <- kappa2(hesitation[, c(2,3)])$value
    
    fleissMispron <- kappam.fleiss(mispron)$value
    fleissElong <- kappam.fleiss(elongation)$value
    fleissHes <- kappam.fleiss(hesitation)$value
    
    kappaSummaryDat[nrow(kappaSummaryDat) + 1,] <-c(id, passageName, kappaMispron_adls, kappaMispron_adbr, kappaMispron_lsbr,
                                                    kappaElong_adls, kappaElong_adbr, kappaElong_lsbr,
                                                    kappaHes_adls, kappaHes_adbr, kappaHes_lsbr,
                                                    fleissMispron, fleissElong, fleissHes)
  }
}  

### SECTION 9: OUTPUT DATA
write.csv(kappaSummaryDat,paste(out_path, kappa_out, sep = "", collapse = NULL), row.names=FALSE)