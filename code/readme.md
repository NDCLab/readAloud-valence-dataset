# Code

This folder contains the three scripts used to create preprocessed derivatives:

| script | input | output |
|:-- | :-- | :-- |
| preprocPavlovia.R | participant-specific records directly from PsychoPy/Pavlovia | six files, two per each of the three tasks within the PsychoPy experiment, one of which is subject-level results and one of which is trial-level results for all subjects |
| preprocTimingAndPitch.py | participant-specific records coded from the task audio recording, based upon the syllable-timestamps-valence protocol | one file with for timing and pitch values for each passage for each subject |
| preprocDisfluencies.R | participant-specific records coded from the task audio recording, based upon the error-coding protocols | one file with disfluency values for all participants across each passage |

In addition, this folder contains a "scaffolds" file that provides, for each passage, an architecture to the relation between words and syllables.

The "_archive" folder includes an older version of preprocTimingAndPitch that was discarded prior to use.


This folder also contains a script that extracts lexical frequency information from the readAloud stimuli passages:

| script | input | output |
|:-- | :-- | :-- |
| stimFreq.R | stimuli characteristics from the readAloud passages | no output files |