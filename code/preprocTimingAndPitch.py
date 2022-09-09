# readAloud-valence-dataset Timing and Pitch Preprocessing
# Author: Jessica M. Alexander
# Last Updated: 2022-09-06

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
    if np.isnan(readStart) & np.isnan(readEnd):
      continue #cannot calculate any passage data if missing timestamp for both start and finish
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
  subzoom = os.listdir(zoompath + subject) #list of all files in subject's zoom folder
  audiopath = zoompath + subject + "/" + subzoom[0]
  audio = parselmouth.Sound(audiopath) #feed .wav file to Parselmouth
  df = pd.read_excel(coded_filepath, header=0)
  npdf = df.to_numpy()
  pitch = audio.to_pitch_ac() #extract Parselmouth pitch object
  
  newdf = create_newdf(npdf) #create subject scaffold df
  
  dfout = extract_parselmouth(sub_id, pitch, df, newdf) #extract all sub data points from audio file with Parselmouth

  dfmain = np.vstack((dfmain, dfout)) #output array and append to dfmain
  
  return dfmain

### SECTION 2: FILE PATHS AND INITIALIZATION
#capture list of coded files
timestamps_ja = "/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/valence-timing/coders/ja/"
timestamps_lg = "/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/valence-timing/coders/lg/"
timestamps_mr = "/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/valence-timing/coders/mr/"
zoompath = "/Users/jalexand/github/readAloud-valence-dataset/sourcedata/checked/zoom/"
outpath = "/Users/jalexand/github/readAloud-valence-dataset/derivatives/preprocessed/valence-timing/"

filelist_ja = os.listdir(timestamps_ja)
filelist_lg = os.listdir(timestamps_lg)
filelist_mr = os.listdir(timestamps_mr)

#initialize empty array
dfmain = np.empty((0,11))

### SECTION 3: RUN THREE PARTICIPANT LOOPS (one for each coder)
#loop over subjects to read in coded timestamps and extract reading times and pitch information
for sub in range(len(filelist_ja)):
  dfmain = run_sub(sub, filelist_ja, zoompath, timestamps_ja, dfmain)
  
for sub in range(len(filelist_lg)):
  dfmain = run_sub(sub, filelist_lg, zoompath, timestamps_lg, dfmain)
  
for sub in range(len(filelist_mr)):
  dfmain = run_sub(sub, filelist_mr, zoompath, timestamps_mr, dfmain)

### SECTION 4: OUTPUT DATA
columns = ['id', 'readStart','switchWord','readEnd', 'timeFirst', 'timeSecond', 'pitchMeanFirst', 'pitchSdFirst', 'pitchMeanSecond', 'pitchSdSecond', 'passage']
combodf = pd.DataFrame(dfmain, columns=columns)
combodf['id'] = combodf['id'].astype(int)
combodf.to_csv(outpath + "timingpitch_subject-by-passage_" + today_formatted + ".csv", index=False)
