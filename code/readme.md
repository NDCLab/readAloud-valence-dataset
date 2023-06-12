# Code

This folder contains three scripts used to create preprocessed derivatives:

| script | input | output |
|:-- | :-- | :-- |
| preprocPavlovia.R | participant-specific records directly from PsychoPy/Pavlovia | six files, two per each of the three tasks within the PsychoPy experiment, one of which is subject-level results and one of which is trial-level results for all subjects |
| preprocTimingAndPitch.py | participant-specific records coded from the task audio recording, based upon the syllable-timestamps-valence protocol | one file with timing and pitch values for each passage for each subject |
| preprocDisfluencies.R | participant-specific records coded from the task audio recording, based upon the error-coding protocols (_in-progress_) | one file with disfluency values for all participants across each passage |

This folder also contains the following three scripts:

| script | input | output |
|:-- | :-- | :-- |
| analysisStimuli.R | stimuli characteristics | readDat, which contains stimuli characteristics per passage half; also includes output within the script (boxplots and t-tests), as well as figures used for the products in readAloud-valence-alpha |
| iccValenceTiming.R | input files to preprocTimingAndPitch.py from two timestamp coders and 20% cross-coding by JMA | output solely within the script (interclass correlations and Bland-Altman plots) |
| raterReliability_by-passage.R | input files to preprocDisfluencies.R (_in-progress_) | one file with kappa/fleiss values, by participant and passage, comparing the output of independent error coders |

In addition, this folder contains a "scaffolds" file that is used by several of the scripts and provides, for each passage, an architecture to the relation between words and syllables.
