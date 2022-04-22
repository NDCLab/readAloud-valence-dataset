# Code

This folder contains the three scripts used to create preprocessed derivatives:

| script | input | output |
|:-- | :-- | :-- |
| preprocPavlovia | participant-specific records directly from PsychoPy/Pavlovia | six files, two per each of the three tasks within the PsychoPy experiment, one of which is subject-level results and one of which is trial-level results for all subjects |
| preprocTimingAndPitch | participant-specific records coded from the task audio recording, based upon the Timing and Pitch protocol | two files, each with passage-level results for all participants, one for timing values and one for pitch values |
| preprocDisfluencies | participant-specific records coded from the task audio recording, based upon the Error Coding protocol | one file with disfluency values for all participants across each passage |

In addition, this folder contains a "scaffold" file that provides, for each passage, an architecture to the relation between words and syllables, in particular with regard to the prePREswitch group, preswitch group, switch group, postswitch group, and the switch word itself.
