# Code

### Instructions
This folder contains the code used to create preprocessed derivatives.


### Project Notes
**In progress:** script to transform coded XLSX file, after saving to CSV (see: example_mantis.csv) into preprocessed CSV (see: derivatives/preprocessed/example_mantis-output.csv) with following output variables:

| variable name | description |
|:-- | :-- |
| first_half_length | length of the first "half" of the passage, in syllables |
| second_half_length | length of the second "half" of the passage, in syllables |
| first_half_speed | speed at which the participant read the first "half" of the passage, in syllables/second |
| second_half_speed | speed at which the participant read the second "half" of the passage, in syllables/second |
| first_half_total_error | total number of disfluent syllables produced by the participant during their reading of the first "half" of the passage |
| second_half_total_error | total number of disfluent syllables produced by the participant during their reading of the second "half" of the passage |
| first_half_error_rate | percentage of disfluent syllables produced by the participant during their reading of the first "half" of the passage: number of disfluent syllables produced / number of syllables required to read the text accurately |
| second_half_error_rate | percentage of disfluent syllables produced by the participant during their reading of the second "half" of the passage: number of disfluent syllables produced / number of syllables required to read the text accurately |
| error_hes_first | total number of hesitation errors produced by the participant in their reading of the first "half" of the passage |
| error_mis_first | total number of mispronounced syllables produced by the participant in their reading of the first "half" of the passage |
| error_dup_first | total number of syllables that were duplicated by the participant in their reading of the first "half" of the passage |
| error_drop_first | total number of syllables that were dropped by the participant in their reading of the first "half" of the passage |
| error_hes_second | total number of hesitation errors produced by the participant in their reading of the second "half" of the passage |
| error_mis_second | total number of mispronounced syllables produced by the participant in their reading of the second "half" of the passage |
| error_dup_second | total number of syllables that were duplicated by the participant in their reading of the second "half" of the passage |
| error_drop_second | total number of syllables that were dropped by the participant in their reading of the second "half" of the passage |
| preswitch_length | length of the preswitch group, which comprises the five words preceding the switch group, in syllables |
| switch_length | length of the switch group, which comprises the switch word and two words either either side, in syllables |
| postswitch_length | length of the postswitch group, which comprises the five words following the switch group, in syllables |
| preswitch_total_error | total number of disfluent syllables produced by the participant during their reading of the words comprising the preswitch group |
| switch_total_error | total number of disfluent syllables produced by the participant during their reading of the words comprising the switch group |
| postswitch_total_error |  total number of disfluent syllables produced by the participant during their reading of the words comprising the postswitch group |
| preswitch_error_rate | percentage of disfluent syllables produced by the participant during their reading of the words comprising the preswitch group: number of disfluent syllables produced / number of syllables required to read the text accurately |
| switch_error_rate | percentage of disfluent syllables produced by the participant during their reading of the words comprising the switch group: number of disfluent syllables produced / number of syllables required to read the text accurately |
| postswitch_error_rate | percentage of disfluent syllables produced by the participant during their reading of the words comprising the postswitch group: number of disfluent syllables produced / number of syllables required to read the text accurately |
| error_hes_pre | total number of hesitation errors produced by the participant in their reading of the words comprising the preswitch group |
| error_mis_pre | total number of mispronounced syllables produced by the participant in their reading of the words comprising the preswitch group |
| error_dup_pre | total number of syllables that were duplicated by the participant in their reading of the words comprising the preswitch group |
| error_drop_pre | total number of syllables that were dropped by the participant in their reading of the words comprising the preswitch group |
| error_hes_switch | total number of hesitation errors produced by the participant in their reading of the words comprising the switch group |
| error_mis_switch | total number of mispronounced syllables produced by the participant in their reading of the words comprising the switch group |
| error_dup_switch | total number of syllables that were duplicated by the participant in their reading of the words comprising the switch group |
| error_drop_switch | total number of syllables that were dropped by the participant in their reading of the words comprising the switch group |
| error_hes_post | total number of hesitation errors produced by the participant in their reading of the words comprising the postswitch group |
| error_mis_post | total number of mispronounced syllables produced by the participant in their reading of the words comprising the postswitch group |
| error_dup_post | total number of syllables that were duplicated by the participant in their reading of the words comprising the postswitch group |
| error_drop_post | total number of syllables that were dropped by the participant in their reading of the words comprising the postswitch group |