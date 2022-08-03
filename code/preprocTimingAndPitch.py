# readAloud-valence-dataset Timing and Pitch Preprocessing
# Author: Jessica M. Alexander
# Last Updated: 2022-08-03

### SECTION 1: SETTING UP
import numpy as np
import os
import pandas as pd
import parselmouth
import re
from datetime import date

today = date.today()
today_formatted = today.strftime("%Y-%m-%d")

#function to create working df for each subject and prefill with coded timestamps
def create_newdf(npdf):
  newdf = np.full((20,9), fill_value=np.NaN)
  
  for row in range(npdf.shape[0]):
    newdf[row, 0:3] = npdf[row, 1:4]
  
  return newdf

#function to extract data from praat using parselmouth
def extract_parselmouth(sub_id, pitch, df, newdf):
  for row in range(newdf.shape[0]):
    readStart = newdf[row,0]
    switchWord = newdf[row,1]
    readEnd = newdf[row,2]
    
    if np.isnan(switchWord):
      continue #cannot calculate any passage data if missing timestamp for switchWord
    elif np.isnan(readEnd):
      newdf[row, 3] = switchWord - readStart #first half reading time
      newdf[row, 5] = parselmouth.praat.call(pitch, "Get mean", readStart, switchWord, "Hertz") #first half mean pitch
      newdf[row, 6] = parselmouth.praat.call(pitch, "Get standard deviation", readStart, switchWord, "Hertz") #first half pitch sd
    elif np.isnan(readStart):  
      newdf[row, 4] = readEnd - switchWord #second half reading time
      newdf[row, 7] = parselmouth.praat.call(pitch, "Get mean", switchWord, readEnd, "Hertz") #second half mean pitch
      newdf[row, 8] = parselmouth.praat.call(pitch, "Get standard deviation", switchWord, readEnd, "Hertz") #second half pitch sd
    else:
      newdf[row, 3] = switchWord - readStart #first half reading time
      newdf[row, 5] = parselmouth.praat.call(pitch, "Get mean", readStart, switchWord, "Hertz") #first half mean pitch
      newdf[row, 6] = parselmouth.praat.call(pitch, "Get standard deviation", readStart, switchWord, "Hertz") #first half pitch sd
      newdf[row, 4] = readEnd - switchWord #second half reading time
      newdf[row, 7] = parselmouth.praat.call(pitch, "Get mean", switchWord, readEnd, "Hertz") #second half mean pitch
      newdf[row, 8] = parselmouth.praat.call(pitch, "Get standard deviation", switchWord, readEnd, "Hertz") #second half pitch sd

  sublist = [sub_id] * newdf.shape[0]
  newdfplus = np.vstack((sublist, np.transpose(newdf)))
  dfout = np.transpose(np.vstack((newdfplus, df.iloc[:,0])))
  
  return dfout

#function to run each participant
def run_sub(sub, filelist, zoompath, timestamps, dfmain):
  filename = filelist[sub]
  coded_filepath = timestamps + filename
  subject = filename.split("_")[0]
  sub_id = int(subject.split("-")[1])
  subzoom = os.listdir(zoompath + subject)
  r = re.compile(".*wav")
  subwav = list(filter(r.match, subzoom))[0]
  audio = parselmouth.Sound(zoompath + subject + "/" + subwav)
  df = pd.read_excel(coded_filepath, header=0)
  npdf = df.to_numpy()
  pitch = audio.to_pitch_ac()
  
  newdf = create_newdf(npdf)
  
  dfout = extract_parselmouth(sub_id, pitch, df, newdf)

  dfmain = np.vstack((dfmain, dfout)) #output array and append to dfmain
  
  return dfmain

### SECTION 2: FILE PATHS AND INITIALIZATION
#capture list of coded files
timestamps = "/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/valence-timing/coders/"
zoompath = "/Users/jalexand/github/readAloud-valence-dataset/sourcedata/checked/zoom/"
filelist = os.listdir(timestamps)
outpath = "/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/valence-timing/"

#initialize empty array
dfmain = np.empty((0,11))

### SECTION 3: START PARTICIPANT LOOP
#loop over subjects to read in coded timestamps and extract reading times and pitch information
for sub in range(len(filelist)):
  dfmain = run_sub(sub, filelist, zoompath, timestamps, dfmain)

### SECTION 4: OUTPUT DATA
columns = ['id', 'readStart','switchWord','readEnd', 'timeFirst', 'timeSecond', 'pitchMeanFirst', 'pitchSdFirst', 'pitchMeanSecond', 'pitchSdSecond', 'passage']
combodf = pd.DataFrame(dfmain, columns=columns)
combodf['id'] = combodf['id'].astype(int)
combodf.to_csv(outpath + "timingpitch_subject-by-passage" + today_formatted + ".csv", index=False)

### SECTION 5: UPDATE CENTRAL TRACKER FOR STUDY
#load central tracker
#track_path = '/home/data/NDClab/datasets/readAloud-valence-dataset/data-monitoring/central-tracker_readAloud-valence.csv'
track_path = '/Users/jalexand/github/readAloud-valence-dataset/data-monitoring/central-tracker_readAloud-valence.csv'
trackerDat = pd.read_csv(track_path, header=0)

#readAloudTiming_s1_r1_e1
for i in range(len(trackerDat['id'])):
  subid = trackerDat.iloc[i, 0]
  rowno = int(np.where(trackerDat["id"] == subid)[0])
  colno = trackerDat.columns.get_loc('readAloudTiming_s1_r1_e1')
  if subid in np.unique(combodf['id']):
    trackerDat.iloc[rowno, colno] = 1
  else:
    trackerDat.iloc[rowno, colno] = 0
print("Updated readAloudTiming_s1_r1_e1!")

#readAloudPitch_s1_r1_e1
for i in range(len(trackerDat['id'])):
  subid = trackerDat.iloc[i, 0]
  rowno = int(np.where(trackerDat["id"] == subid)[0])
  colno = trackerDat.columns.get_loc('readAloudPitch_s1_r1_e1')
  if subid in np.unique(combodf['id']):
    trackerDat.iloc[rowno, colno] = 1
  else:
    trackerDat.iloc[rowno, colno] = 0
print("Updated readAloudPitch_s1_r1_e1!")

#write back to central tracker
trackerDat.to_csv(track_path, index=False)
