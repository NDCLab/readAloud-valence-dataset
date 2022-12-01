## ReadAloud Stimuli

This folder contains:

- 20 txt files, each containing one stimulus passage and the challenge question associated with it
- an Excel workbook containing passage-level and word-level characteristics for the readAloud stimuli 
- elp-transactions/ - For each passage, a CSV file from the English Lexicon Project used to acquire word-level characteristics, along with a CSV file with summary characteristics (ELP transaction number is noted in cell A1 of the associated worksheet; full lexicon was queried).  All characteristics are drawn from the lemma unless the stimulus word itself was available in the supplementary materials of [Warriner et al., 2013](https://doi.org/10.3758/s13428-012-0314-x), which is included as the "warriner" tab.
- liwc-analysis/ - CSV file with the output from LIWC-22 for each passage half, along with the txt files used as input.  These text files were created by splitting each of the 20 passage files at the switch word, and deleting the challenge question.

Note: The final sentence in the "broccoli" passage contains a typographical error.  The bracketed word is missing:
> Today, the widespread availability of iodized table [salt] counteracts iodine deficiencies.

Future uses of these stimuli should correct this error.  If using data from this dataset, please think carefully about whether this error will adversely affect your analyses.  In the [initial analyses from our lab](https://github.com/NDCLab/readAloud-valence-alpha), we chose to exclude the "broccoli" passage altogether, for all participants.