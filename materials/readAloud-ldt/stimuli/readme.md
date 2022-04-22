## Overview of the Experimental Stimuli

This folder contains the following:

**ReadAloud Task (readAloud/)**
- 20 txt files, each containing one stimulus passage and the challenge question associated with it
- an Excel workbook containing passage-level and word-level characteristics for the readAloud stimuli 
- elp-transactions/ For each passage, a CSV file from the English Lexicon Project used to acquire most of the word-level characteristics, along with a CSV file with summary characteristics (ELP transaction number is noted in cell A1 of the associated worksheet)
- liwc-analysis/ CSV file with the output from LIWC-22 for each passage half, along with the txt files used as input.  These text files were created by splitting each of the 20 passage files at the switch word, and deleting the challenge question.

**Lexical Decision Task (ldt/)**
- an Excel workbook containing (sub)lexical characteristics for the LDT stimuli words
- a CSV file from the English Lexicon Project used to acquire most such characteristics
- a CSV file from the English Lexicon Project with summary characteristics