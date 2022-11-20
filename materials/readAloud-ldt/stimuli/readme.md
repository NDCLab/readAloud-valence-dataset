## Overview of the Experimental Stimuli

This folder contains the following:

**ReadAloud Task (readAloud/)**
- 20 txt files, each containing one stimulus passage and the challenge question associated with it
- an Excel workbook containing passage-level and word-level characteristics for the readAloud stimuli 
- elp-transactions/ - For each passage, a CSV file from the English Lexicon Project used to acquire most of the word-level characteristics, along with a CSV file with summary characteristics (ELP transaction number is noted in cell A1 of the associated worksheet).  All characteristics are drawn from the lemma unless the stimulus word itself was available in Warriner et al. (2013).  For characteristics drawn from the English Lexicon Project, the full lexicon was queried. 
- liwc-analysis/ - CSV file with the output from LIWC-22 for each passage half, along with the txt files used as input.  These text files were created by splitting each of the 20 passage files at the switch word, and deleting the challenge question.

**Lexical Decision Task (ldt/)**
- a copy of the full stimulus list (identical to the PsychoPy resource file)
- an Excel workbook containing (sub)lexical characteristics for the LDT stimuli words
- a CSV file from the English Lexicon Project used to acquire most such characteristics
- a CSV file from the English Lexicon Project with summary characteristics

**Additional Resources (resources/)**
- a diagram of the readAloud task (figure2.pptx)
- a CSV file containing the LDT stimuli and categories from [Kousta et al., 2009](https://doi.org/10.1016/j.cognition.2009.06.007)
- an export of the SUBTLEXus corpus from [Ghent University](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus), downloaded on 06/13/2022
- an export of the [Warriner dataset](https://link.springer.com/article/10.3758/s13428-012-0314-x), downloaded on 08/08/2021