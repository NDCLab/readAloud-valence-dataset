#set up libraries
library(readxl)

#READ IN THE PASSAGE STRUCTURE FILES TO SCAFFOLD OUTPUT
path <- '/Users/jessraissouni/Desktop/readAloud-valence/'
filename <- 'mantis_structure'
ext <- '.xlsx'
passage = 'neg-pos_mantis'
mantis_str <- data.frame(read_excel(paste(path,filename,ext, sep = "", collapse = NULL),
                            sheet = passage))

#####HAVEN'T TOUCHED FROM HERE YET
#READ IN THE CODED FILE AND ESTABLISH TWO DATAFRAMES, ERRORS AND TIMING
path <- '/Users/jessraissouni/github/readAloud-valence-dataset/materials/readAloud-ldt/stimuli/readAloud/'
subject <- 190001
filename <- paste("sub-", subject, sep = "", collapse = NULL)
ext <- '.xlsx'
passage = "mantis"
df <- data.frame(read_excel(paste(path,filename,ext, sep = "", collapse = NULL),
                            sheet = passage, range="b2:zz8"))
colnames(df) 

unlist(df[,1])