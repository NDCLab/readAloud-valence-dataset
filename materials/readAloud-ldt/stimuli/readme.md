## Overview of the Experimental Stimuli

This folder contains the following:

**ReadAloud Task (readAloud/)**
- 20 txt files, each containing one stimulus passage and the challenge question associated with it
- an Excel workbook containing passage-level and word-level characteristics for the readAloud stimuli 
- elp-transactions/ - For each passage, a CSV file from the English Lexicon Project used to acquire most of the word-level characteristics, along with a CSV file with summary characteristics (ELP transaction number is noted in cell A1 of the associated worksheet).  All characteristics are drawn from the lemma unless the stimulus word itself was available in Warriner et al. (2013).  For characteristics drawn from the English Lexicon Project, the full lexicon was queried. 
- liwc-analysis/ - CSV file with the output from LIWC-22 for each passage half, along with the txt files used as input.  These text files were created by splitting each of the 20 passage files at the switch word, and deleting the challenge question.

**Lexical Decision Task (ldt/)**
- an Excel workbook containing (sub)lexical characteristics for the LDT stimuli words
- a CSV file from the English Lexicon Project used to acquire most such characteristics
- a CSV file from the English Lexicon Project with summary characteristics