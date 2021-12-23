#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Thu Dec 23 14:53:49 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'read-aloud-o_s1_r2_e1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jalexand/github/readAloud-valence-dataset/materials/readAloud-ldt/read-aloud-val-o_s1_r1_e1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 960], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0.6549,0.6549,0.6549], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='cm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
headerWelcome = visual.TextStim(win=win, name='headerWelcome',
    text='Hello!',
    font='Open Sans',
    pos=(0, 8), height=2.0, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcomeText = visual.TextStim(win=win, name='welcomeText',
    text='You will complete three activities today.\n\nThe first is a reading task.\nThis task takes about 40 minutes.\n\nThe second is a word decision game.\nThis game takes about 15 minutes.\n\nThe third is a color and shape matching game.\nThis game takes about xx minutes.\n\nAfter you complete all tasks, you need to return (briefly!) to the questionnaires.',
    font='Open Sans',
    pos=(0, -2), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructContinue3 = visual.TextStim(win=win, name='instructContinue3',
    text='- — -\n\nPress the space key to continue.',
    font='Open Sans',
    pos=(0, -10), height=0.55, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_00 = keyboard.Keyboard()
participant_id = expInfo['participant']
passageCount = 0

# Initialize components for Routine "introReading"
introReadingClock = core.Clock()
welcomeReading = visual.TextStim(win=win, name='welcomeReading',
    text='In this task, you will be presented with a series of text passages that you should read aloud.\n\nPlease try to read clearly, at a normal volume, as if you were reading a story to another person.\n\nThere are a total of 20 passages to read. Each passage should take about 1-2 minutes. After each passage, you will be asked a question based on the text.\n\nYou may take a short break (less than a minute) between each passage if you like, or you can continue to the next passage right away.',
    font='Open Sans',
    pos=(0, -2), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_01 = keyboard.Keyboard()
headerReading = visual.TextStim(win=win, name='headerReading',
    text='Welcome to the reading task!',
    font='Open Sans',
    pos=(0, 8), height=2.0, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
instructContinue2 = visual.TextStim(win=win, name='instructContinue2',
    text='- — -\n\nPress the space key to continue.',
    font='Open Sans',
    pos=(0, -10), height=0.55, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instructCalibration"
instructCalibrationClock = core.Clock()
explainCalib = visual.TextStim(win=win, name='explainCalib',
    text='Before we begin, a short period of silence is needed to calibrate the task audio.\n\nThe calibration period will last 5 seconds. During the calibration, please do not speak, but it is OK for there to be background noise.\n\nAudio calibration will begin when you press the space key.',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructContinue4 = visual.TextStim(win=win, name='instructContinue4',
    text='- — -\n\nPress the space key to begin calibration.',
    font='Open Sans',
    pos=(0, -10), height=0.55, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_02 = keyboard.Keyboard()

# Initialize components for Routine "calibration"
calibrationClock = core.Clock()
calibText = visual.TextStim(win=win, name='calibText',
    text='Audio calibrating…\n\nPlease remain silent for 5 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
calibTimer = visual.TextStim(win=win, name='calibTimer',
    text='',
    font='Open Sans',
    pos=(5, 5), height=0.5, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instruct"
instructClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='The audio calibration is complete.\n\nWhen a passage comes on-screen, begin reading aloud immediately. Do not “pre-read” the passage. Just dive in!\n\nRemember to read clearly, at your normal volume and reading speed. When you finish reading a passage, press the space key to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructContinue5 = visual.TextStim(win=win, name='instructContinue5',
    text='- — -\n\nPress the space key to proceed to the first passage.',
    font='Open Sans',
    pos=(0, -10), height=0.55, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_03 = keyboard.Keyboard()

# Initialize components for Routine "passage1"
passage1Clock = core.Clock()
passageText1 = visual.TextStim(win=win, name='passageText1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructContinue1 = visual.TextStim(win=win, name='instructContinue1',
    text='- — -\n\nPress the space key to continue.',
    font='Open Sans',
    pos=(0, -10), height=0.55, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_04 = keyboard.Keyboard()

# Initialize components for Routine "challenge1"
challenge1Clock = core.Clock()
challengeText1 = visual.TextStim(win=win, name='challengeText1',
    text='',
    font='Open Sans',
    pos=(0, 2), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
challengeResponse1 = keyboard.Keyboard()
challengeOptions1 = visual.TextStim(win=win, name='challengeOptions1',
    text='',
    font='Open Sans',
    pos=(0, -2), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
answerInstruct1 = visual.TextStim(win=win, name='answerInstruct1',
    text='- — -\n\nSelect your answer by pressing the corresponding letter on the keyboard.',
    font='Open Sans',
    pos=(0, -10), height=0.55, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
counterText1 = visual.TextStim(win=win, name='counterText1',
    text='',
    font='Open Sans',
    pos=(7, 7), height=0.5, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "readyScreen1"
readyScreen1Clock = core.Clock()
readingBreak1 = visual.TextStim(win=win, name='readingBreak1',
    text='If you need a break, please take a short break now (less than a minute).\n\nYou can skip this break and proceed to the next passage by pressing the space key.',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_05 = keyboard.Keyboard()
timer1 = visual.TextStim(win=win, name='timer1',
    text='',
    font='Open Sans',
    pos=(7, 7), height=0.5, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "passage2"
passage2Clock = core.Clock()
passageText2 = visual.TextStim(win=win, name='passageText2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructContinue2_2 = visual.TextStim(win=win, name='instructContinue2_2',
    text='- — -\n\nPress the space key to continue.',
    font='Open Sans',
    pos=(0, -10), height=0.55, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "challenge2"
challenge2Clock = core.Clock()
challengeText2 = visual.TextStim(win=win, name='challengeText2',
    text='',
    font='Open Sans',
    pos=(0, 2), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
challengeResponse2 = keyboard.Keyboard()
challengeOptions2 = visual.TextStim(win=win, name='challengeOptions2',
    text='',
    font='Open Sans',
    pos=(0, -2), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
answerInstruct2 = visual.TextStim(win=win, name='answerInstruct2',
    text='- — -\n\nSelect your answer by pressing the corresponding letter on the keyboard.',
    font='Open Sans',
    pos=(0, -10), height=0.55, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
counterText2 = visual.TextStim(win=win, name='counterText2',
    text='',
    font='Open Sans',
    pos=(7, 7), height=0.5, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "readyScreen2"
readyScreen2Clock = core.Clock()
readingBreak2 = visual.TextStim(win=win, name='readingBreak2',
    text='If you need a break, please take a short break now (less than a minute).\n\nYou can skip this break and proceed to the next passage by pressing the space key.',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()
timer2 = visual.TextStim(win=win, name='timer2',
    text='',
    font='Open Sans',
    pos=(7, 7), height=0.5, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "readComplete"
readCompleteClock = core.Clock()
readCompleteintroLDT = visual.TextStim(win=win, name='readCompleteintroLDT',
    text='You have completed the reading task!\n\nNext, you will play the word decision game.',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_06 = keyboard.Keyboard()
instructContinue6 = visual.TextStim(win=win, name='instructContinue6',
    text='- — -\n\nPress the space key to continue.',
    font='Open Sans',
    pos=(0, -10), height=0.55, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "introLDT"
introLDTClock = core.Clock()
welcomeLDT = visual.TextStim(win=win, name='welcomeLDT',
    text='In this task, you will be presented with a word.\n\nYou must decide if this is a real word or not. You will press the letter "J" if the word on screen is a real word. You will press the letter "F" if the word on screen is NOT a real word.\n\nTry to answer as quickly but as accurately as possible.\n\nPress either "F" or "J" to continue.',
    font='Open Sans',
    pos=(0, -2), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
headerLDT = visual.TextStim(win=win, name='headerLDT',
    text='Welcome to the word decision game!',
    font='Open Sans',
    pos=(0, 8), height=2.0, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_07 = keyboard.Keyboard()
ldtWelcomeResponseF = visual.TextStim(win=win, name='ldtWelcomeResponseF',
    text='F\n\nnot a word',
    font='Open Sans',
    pos=(-9, -9), height=0.65, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ldtWelcomeResponseJ = visual.TextStim(win=win, name='ldtWelcomeResponseJ',
    text='J\n\nis a word',
    font='Open Sans',
    pos=(9, -9), height=0.65, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "introPractice"
introPracticeClock = core.Clock()
introPracticeText = visual.TextStim(win=win, name='introPracticeText',
    text='First, we will do a short practice session.\n\nPlace your left index finger on the “F” key.\n\nPlace your right index finger on the “J” key.\n\nPress either "F" or "J" to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_08 = keyboard.Keyboard()
ldtIntroResponseF = visual.TextStim(win=win, name='ldtIntroResponseF',
    text='F\n\nnot a word',
    font='Open Sans',
    pos=(-9, -9), height=0.65, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ldtIntroResponseJ = visual.TextStim(win=win, name='ldtIntroResponseJ',
    text='J\n\nis a word',
    font='Open Sans',
    pos=(9, -9), height=0.65, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "introPractice2"
introPractice2Clock = core.Clock()
introPracticeText2 = visual.TextStim(win=win, name='introPracticeText2',
    text='When the letter string appears, you need to make a decision as fast as possible whether the string is a word in English or not.\n\nFor example: "pretty/preft".\n\nIf you think the string forms a word, press the "J" button on the keyboard.\n\nIf you think the string is not a word, press the "F" button on the keyboard.\n\nFor this practice session, we will tell you if you got the right answer.\n\nRemember to rest your fingers back on the “F” and “J” keys after each response.\n\nPress either "F" or "J" to start the practice session.',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_24 = keyboard.Keyboard()
ldtIntroResponseF2 = visual.TextStim(win=win, name='ldtIntroResponseF2',
    text='F\n\nnot a word',
    font='Open Sans',
    pos=(-9, -9), height=0.65, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ldtIntroResponseJ2 = visual.TextStim(win=win, name='ldtIntroResponseJ2',
    text='J\n\nis a word',
    font='Open Sans',
    pos=(9, -9), height=0.65, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "fixPractice"
fixPracticeClock = core.Clock()
fixPracticecross = visual.TextStim(win=win, name='fixPracticecross',
    text='+',
    font='Open Sans',
    pos=(0, 1), height=2.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ldtPractice"
ldtPracticeClock = core.Clock()
ldtPracticeWord = visual.TextStim(win=win, name='ldtPracticeWord',
    text='',
    font='Open Sans',
    pos=(0, 1), height=1.5, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practiceResponse = keyboard.Keyboard()
ldtPracticeResponseF = visual.TextStim(win=win, name='ldtPracticeResponseF',
    text='F\n\nnot a word',
    font='Open Sans',
    pos=(-9, -9), height=0.65, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ldtPracticeResponseJ = visual.TextStim(win=win, name='ldtPracticeResponseJ',
    text='J\n\nis a word',
    font='Open Sans',
    pos=(9, -9), height=0.65, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedbackMessage = visual.TextStim(win=win, name='feedbackMessage',
    text='',
    font='Open Sans',
    pos=(0, 1), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "moreInstruct"
moreInstructClock = core.Clock()
finalRemind = visual.TextStim(win=win, name='finalRemind',
    text='Great job on the practice round!\n\nOn the next screen, you will begin the real game. It is just like the practice, but we won’t tell you if each answer is right or not.\n\nThis game does not have any breaks, but it will only last about 12 minutes.\n\nRemember to rest your fingers back on the “F” and “J” keys after each response.\n\nThe word decision game will start when you press the space key.',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_09 = keyboard.Keyboard()
instructContinue7 = visual.TextStim(win=win, name='instructContinue7',
    text='- — -\n\nPress the space key to start the game.',
    font='Open Sans',
    pos=(0, -10), height=0.55, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fixLdtTask"
fixLdtTaskClock = core.Clock()
fixLdtTaskCross = visual.TextStim(win=win, name='fixLdtTaskCross',
    text='+',
    font='Open Sans',
    pos=(0, 1), height=2.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ldtTask"
ldtTaskClock = core.Clock()
ldtStimulus = visual.TextStim(win=win, name='ldtStimulus',
    text='',
    font='Open Sans',
    pos=(0, 1), height=1.5, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ldtResponse = keyboard.Keyboard()
ldtResponseF = visual.TextStim(win=win, name='ldtResponseF',
    text='F\n\nnot a word',
    font='Open Sans',
    pos=(-9, -9), height=0.65, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ldtResponseJ = visual.TextStim(win=win, name='ldtResponseJ',
    text='J\n\nis a word',
    font='Open Sans',
    pos=(9, -9), height=0.65, wrapWidth=25.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "interTrial"
interTrialClock = core.Clock()
blank_interTrial = visual.TextStim(win=win, name='blank_interTrial',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ldtComplete"
ldtCompleteClock = core.Clock()
ldtCompleteintroDCCS = visual.TextStim(win=win, name='ldtCompleteintroDCCS',
    text='You have completed the word decision game!\n\nFinally, you will play the matching game.',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_25 = keyboard.Keyboard()
instructContinue8 = visual.TextStim(win=win, name='instructContinue8',
    text='- — -\n\nPress the space key to continue.',
    font='Open Sans',
    pos=(0, -10), height=0.55, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "introDCCSPractice"
introDCCSPracticeClock = core.Clock()
headerDCCS = visual.TextStim(win=win, name='headerDCCS',
    text='Welcome to the matching game!',
    font='Open Sans',
    pos=(0, 8), height=2.0, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcomeDCCS = visual.TextStim(win=win, name='welcomeDCCS',
    text='We’re going to play a matching game with COLORS and SHAPES.\n\nJust like the last game, you will use the “F” and “J” keys to respond.\n\nTurn your sound on to hear feedback during the practice rounds.\n\nPress either "F" or "J" to continue.',
    font='Open Sans',
    pos=(0, -2), height=1.0, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "shapeBoatEx"
shapeBoatExClock = core.Clock()
textBoat = visual.TextStim(win=win, name='textBoat',
    text='We’ll play the SHAPE game first.\n\nIn the SHAPE game, choose the picture that’s the same SHAPE as the picture in the middle of the screen.\n\nIf it’s a BOAT, choose the BOAT picture by pressing “J”.',
    font='Open Sans',
    pos=(0, 7), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_1 = visual.ImageStim(
    win=win,
    name='image_1', 
    image='resources/dccs/RedBoat.png', mask=None,
    ori=0.0, pos=(0, 1), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='resources/dccs/RedRabbitWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='resources/dccs/BlueBoatWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-3.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='resources/dccs/BlueBoatRed.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-4.0)
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='resources/dccs/BlueBoatWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-5.0)
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='resources/dccs/BlueBoatRed.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-6.0)
key_resp_10 = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press “J” to continue.',
    font='Open Sans',
    pos=(0, -8), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "shapeRabbitEx"
shapeRabbitExClock = core.Clock()
textRabbit = visual.TextStim(win=win, name='textRabbit',
    text='If it’s a RABBIT,\nchoose the RABBIT picture by pressing “F”.',
    font='Open Sans',
    pos=(0, 7), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='resources/dccs/BlueRabbit.png', mask=None,
    ori=0.0, pos=(0, 1), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='resources/dccs/BlueBoatWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='resources/dccs/RedRabbitWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-3.0)
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='resources/dccs/RedRabbitRed.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-4.0)
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='resources/dccs/RedRabbitWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-5.0)
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='resources/dccs/RedRabbitRed.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-6.0)
key_resp_11 = keyboard.Keyboard()
text_11 = visual.TextStim(win=win, name='text_11',
    text='Press “F” to continue.',
    font='Open Sans',
    pos=(0, -8), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "instructShape"
instructShapeClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Now you try.',
    font='Open Sans',
    pos=(0, 6), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='Keep your eyes on the star.',
    font='Open Sans',
    pos=(0, 4), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
star_1 = visual.ImageStim(
    win=win,
    name='star_1', 
    image='resources/dccs/star.png', mask=None,
    ori=0.0, pos=(0, 1), size=(0.83, 0.89),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
text_14 = visual.TextStim(win=win, name='text_14',
    text='Answer as fast as you can without making mistakes.',
    font='Open Sans',
    pos=(0, -2), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='If you make a mistake, just keep going!',
    font='Open Sans',
    pos=(0, -4), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='Press either “F” or “J” to continue.',
    font='Open Sans',
    pos=(0, -8), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "interTrialShape"
interTrialShapeClock = core.Clock()
leftImageWait = visual.ImageStim(
    win=win,
    name='leftImageWait', 
    image='resources/dccs/RedRabbitWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
rightImageWait = visual.ImageStim(
    win=win,
    name='rightImageWait', 
    image='resources/dccs/BlueBoatWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "ISICodeShape"
ISICodeShapeClock = core.Clock()

# Initialize components for Routine "fixationShape"
fixationShapeClock = core.Clock()
star_2 = visual.ImageStim(
    win=win,
    name='star_2', 
    image='resources/dccs/star.png', mask=None,
    ori=0.0, pos=(0, 1), size=(0.83, 0.89),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
leftImageFixation = visual.ImageStim(
    win=win,
    name='leftImageFixation', 
    image='resources/dccs/RedRabbitWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
rightImageFixation = visual.ImageStim(
    win=win,
    name='rightImageFixation', 
    image='resources/dccs/BlueBoatWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "cueShape"
cueShapeClock = core.Clock()
textCueShape = visual.TextStim(win=win, name='textCueShape',
    text='SHAPE',
    font='Open Sans',
    pos=(0, 1), height=1.5, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
leftImageCue = visual.ImageStim(
    win=win,
    name='leftImageCue', 
    image='resources/dccs/RedRabbitWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
rightImageCue = visual.ImageStim(
    win=win,
    name='rightImageCue', 
    image='resources/dccs/BlueBoatWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "stimShape"
stimShapeClock = core.Clock()
stimImageShape = visual.ImageStim(
    win=win,
    name='stimImageShape', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 1), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
leftImageShape = visual.ImageStim(
    win=win,
    name='leftImageShape', 
    image='sin', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
rightImageShape = visual.ImageStim(
    win=win,
    name='rightImageShape', 
    image='sin', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "feedbackShape"
feedbackShapeClock = core.Clock()
leftImageFeedback = visual.ImageStim(
    win=win,
    name='leftImageFeedback', 
    image='sin', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
middleImageFeedback = visual.ImageStim(
    win=win,
    name='middleImageFeedback', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 1), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
rightImageFeedback = visual.ImageStim(
    win=win,
    name='rightImageFeedback', 
    image='sin', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-3.0)
textFeedbackShape = visual.TextStim(win=win, name='textFeedbackShape',
    text='',
    font='Open Sans',
    pos=(0, 7), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "clearShape"
clearShapeClock = core.Clock()
counterOne = 0
counterTwo = 0

# Initialize components for Routine "continueShape"
continueShapeClock = core.Clock()
isForward = 0
textContinueStatus = visual.TextStim(win=win, name='textContinueStatus',
    text='',
    font='Open Sans',
    pos=(0, 1), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_14 = keyboard.Keyboard()

# Initialize components for Routine "colorRedEx"
colorRedExClock = core.Clock()
textRed = visual.TextStim(win=win, name='textRed',
    text='We can also match by COLOR.\n\nIn the COLOR game, chose the picture that’s the same COLOR as the picture in the middle of the screen. \n\nIf it’s RED, choose the RED picture by pressing “J”.',
    font='Open Sans',
    pos=(0, 7), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='resources/dccs/RedBoat.png', mask=None,
    ori=0.0, pos=(0, 1), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='resources/dccs/BlueBoatWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='resources/dccs/RedRabbitWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-3.0)
image_16 = visual.ImageStim(
    win=win,
    name='image_16', 
    image='resources/dccs/RedRabbitRed.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-4.0)
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='resources/dccs/RedRabbitWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-5.0)
image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='resources/dccs/RedRabbitRed.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-6.0)
key_resp_15 = keyboard.Keyboard()
text_18 = visual.TextStim(win=win, name='text_18',
    text='Press “J” to continue.',
    font='Open Sans',
    pos=(0, -8), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "colorBlueEx"
colorBlueExClock = core.Clock()
textBlue = visual.TextStim(win=win, name='textBlue',
    text='If it’s BLUE,\nchoose the BLUE picture by pressing “F”.',
    font='Open Sans',
    pos=(0, 7), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_19 = visual.ImageStim(
    win=win,
    name='image_19', 
    image='resources/dccs/BlueRabbit.png', mask=None,
    ori=0.0, pos=(0, 1), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
image_20 = visual.ImageStim(
    win=win,
    name='image_20', 
    image='resources/dccs/RedRabbitWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
image_21 = visual.ImageStim(
    win=win,
    name='image_21', 
    image='resources/dccs/BlueBoatWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-3.0)
image_22 = visual.ImageStim(
    win=win,
    name='image_22', 
    image='resources/dccs/BlueBoatRed.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-4.0)
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image='resources/dccs/BlueBoatWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-5.0)
image_24 = visual.ImageStim(
    win=win,
    name='image_24', 
    image='resources/dccs/BlueBoatRed.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-6.0)
key_resp_16 = keyboard.Keyboard()
text_19 = visual.TextStim(win=win, name='text_19',
    text='Press “F” to continue.',
    font='Open Sans',
    pos=(0, -8), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "instructColor"
instructColorClock = core.Clock()
text_20 = visual.TextStim(win=win, name='text_20',
    text='Now you try.',
    font='Open Sans',
    pos=(0, 6), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='Keep your eyes on the star.',
    font='Open Sans',
    pos=(0, 4), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
star_3 = visual.ImageStim(
    win=win,
    name='star_3', 
    image='resources/dccs/star.png', mask=None,
    ori=0.0, pos=(0, 1), size=(0.83, 0.89),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
text_22 = visual.TextStim(win=win, name='text_22',
    text='Answer as fast as you can without making mistakes.',
    font='Open Sans',
    pos=(0, -2), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_23 = visual.TextStim(win=win, name='text_23',
    text='If you make a mistake, just keep going!',
    font='Open Sans',
    pos=(0, -4), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_24 = visual.TextStim(win=win, name='text_24',
    text='Press either “F” or “J” to continue.',
    font='Open Sans',
    pos=(0, -8), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
key_resp_17 = keyboard.Keyboard()

# Initialize components for Routine "interTrialColor"
interTrialColorClock = core.Clock()
leftImageWait2 = visual.ImageStim(
    win=win,
    name='leftImageWait2', 
    image='resources/dccs/RedRabbitWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
rightImageWait2 = visual.ImageStim(
    win=win,
    name='rightImageWait2', 
    image='resources/dccs/BlueBoatWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "ISICodeColor"
ISICodeColorClock = core.Clock()

# Initialize components for Routine "fixationColor"
fixationColorClock = core.Clock()
star_4 = visual.ImageStim(
    win=win,
    name='star_4', 
    image='resources/dccs/star.png', mask=None,
    ori=0.0, pos=(0, 1), size=(0.83, 0.89),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
leftImageFixation2 = visual.ImageStim(
    win=win,
    name='leftImageFixation2', 
    image='resources/dccs/RedRabbitWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
rightImageFixation2 = visual.ImageStim(
    win=win,
    name='rightImageFixation2', 
    image='resources/dccs/BlueBoatWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "cueColor"
cueColorClock = core.Clock()
textCueColor = visual.TextStim(win=win, name='textCueColor',
    text='COLOR',
    font='Open Sans',
    pos=(0, 1), height=1.5, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
leftImageCue2 = visual.ImageStim(
    win=win,
    name='leftImageCue2', 
    image='resources/dccs/RedRabbitWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
rightImageCue2 = visual.ImageStim(
    win=win,
    name='rightImageCue2', 
    image='resources/dccs/BlueBoatWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "stimColor"
stimColorClock = core.Clock()
stimImageColor = visual.ImageStim(
    win=win,
    name='stimImageColor', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 1), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
leftImageColor = visual.ImageStim(
    win=win,
    name='leftImageColor', 
    image='sin', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
rightImageColor = visual.ImageStim(
    win=win,
    name='rightImageColor', 
    image='sin', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
key_resp_18 = keyboard.Keyboard()

# Initialize components for Routine "feedbackColor"
feedbackColorClock = core.Clock()
leftImageFeedback2 = visual.ImageStim(
    win=win,
    name='leftImageFeedback2', 
    image='sin', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
middleImageFeedback2 = visual.ImageStim(
    win=win,
    name='middleImageFeedback2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 1), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
rightImageFeedback2 = visual.ImageStim(
    win=win,
    name='rightImageFeedback2', 
    image='sin', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-3.0)
textFeedbackColor = visual.TextStim(win=win, name='textFeedbackColor',
    text='',
    font='Open Sans',
    pos=(0, 7), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "clearColor"
clearColorClock = core.Clock()
counterOne = 0
counterTwo = 0

# Initialize components for Routine "continueColor"
continueColorClock = core.Clock()
isForward = 0
textContinueStatus2 = visual.TextStim(win=win, name='textContinueStatus2',
    text='',
    font='Open Sans',
    pos=(0, 1), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_19 = keyboard.Keyboard()

# Initialize components for Routine "introDCCS"
introDCCSClock = core.Clock()
textIntroDCCS = visual.TextStim(win=win, name='textIntroDCCS',
    text='Now we’re going to play both games together.\n\nRemember, if you see the word SHAPE, choose the picture that is the same SHAPE as the picture in the middle of the screen. If you see the word COLOR, choose the picture that is the same COLOR as the picture in the middle of the screen.\n\nRest your fingers back on the letter “F” and the letter “J” after you answer.\n\nPress the space key to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_20 = keyboard.Keyboard()

# Initialize components for Routine "instructCombo"
instructComboClock = core.Clock()
text_25 = visual.TextStim(win=win, name='text_25',
    text='Let’s play the game.',
    font='Open Sans',
    pos=(0, 6), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_26 = visual.TextStim(win=win, name='text_26',
    text='Keep your eyes on the star.',
    font='Open Sans',
    pos=(0, 4), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
star_5 = visual.ImageStim(
    win=win,
    name='star_5', 
    image='resources/dccs/star.png', mask=None,
    ori=0.0, pos=(0, 1), size=(0.83, 0.89),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
text_27 = visual.TextStim(win=win, name='text_27',
    text='Answer as fast as you can without making mistakes.',
    font='Open Sans',
    pos=(0, -2), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_28 = visual.TextStim(win=win, name='text_28',
    text='If you make a mistake, just keep going!',
    font='Open Sans',
    pos=(0, -4), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_29 = visual.TextStim(win=win, name='text_29',
    text='Remember to rest your fingers back on the letter “F” and the letter “J” after each answer. \n\nPress the space key to start the game.',
    font='Open Sans',
    pos=(0, -8), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
key_resp_21 = keyboard.Keyboard()

# Initialize components for Routine "countReset"
countResetClock = core.Clock()

# Initialize components for Routine "interTrialCombo"
interTrialComboClock = core.Clock()
image_25 = visual.ImageStim(
    win=win,
    name='image_25', 
    image='resources/dccs/BlueBallWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
image_26 = visual.ImageStim(
    win=win,
    name='image_26', 
    image='resources/dccs/YellowTruckWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "ISICodeCombo"
ISICodeComboClock = core.Clock()

# Initialize components for Routine "fixationCombo"
fixationComboClock = core.Clock()
star_6 = visual.ImageStim(
    win=win,
    name='star_6', 
    image='resources/dccs/star.png', mask=None,
    ori=0.0, pos=(0, 1), size=(0.83, 0.89),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
leftImageFixation3 = visual.ImageStim(
    win=win,
    name='leftImageFixation3', 
    image='resources/dccs/BlueBallWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
rightImageFixation3 = visual.ImageStim(
    win=win,
    name='rightImageFixation3', 
    image='resources/dccs/YellowTruckWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "cueCombo"
cueComboClock = core.Clock()
textCueCombo = visual.TextStim(win=win, name='textCueCombo',
    text='',
    font='Open Sans',
    pos=(0, 1), height=1.5, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
leftImageCue3 = visual.ImageStim(
    win=win,
    name='leftImageCue3', 
    image='resources/dccs/BlueBallWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
rightImageCue3 = visual.ImageStim(
    win=win,
    name='rightImageCue3', 
    image='resources/dccs/YellowTruckWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "stimCombo"
stimComboClock = core.Clock()
stimImageCombo = visual.ImageStim(
    win=win,
    name='stimImageCombo', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 1), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
leftImageCombo = visual.ImageStim(
    win=win,
    name='leftImageCombo', 
    image='sin', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
rightImageCombo = visual.ImageStim(
    win=win,
    name='rightImageCombo', 
    image='sin', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
key_resp_22 = keyboard.Keyboard()

# Initialize components for Routine "stopColorLoop"
stopColorLoopClock = core.Clock()

# Initialize components for Routine "interTrialCombo"
interTrialComboClock = core.Clock()
image_25 = visual.ImageStim(
    win=win,
    name='image_25', 
    image='resources/dccs/BlueBallWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
image_26 = visual.ImageStim(
    win=win,
    name='image_26', 
    image='resources/dccs/YellowTruckWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "ISICodeCombo"
ISICodeComboClock = core.Clock()

# Initialize components for Routine "fixationCombo"
fixationComboClock = core.Clock()
star_6 = visual.ImageStim(
    win=win,
    name='star_6', 
    image='resources/dccs/star.png', mask=None,
    ori=0.0, pos=(0, 1), size=(0.83, 0.89),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
leftImageFixation3 = visual.ImageStim(
    win=win,
    name='leftImageFixation3', 
    image='resources/dccs/BlueBallWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
rightImageFixation3 = visual.ImageStim(
    win=win,
    name='rightImageFixation3', 
    image='resources/dccs/YellowTruckWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "cueCombo"
cueComboClock = core.Clock()
textCueCombo = visual.TextStim(win=win, name='textCueCombo',
    text='',
    font='Open Sans',
    pos=(0, 1), height=1.5, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
leftImageCue3 = visual.ImageStim(
    win=win,
    name='leftImageCue3', 
    image='resources/dccs/BlueBallWhite.png', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
rightImageCue3 = visual.ImageStim(
    win=win,
    name='rightImageCue3', 
    image='resources/dccs/YellowTruckWhite.png', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "stimCombo"
stimComboClock = core.Clock()
stimImageCombo = visual.ImageStim(
    win=win,
    name='stimImageCombo', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 1), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
leftImageCombo = visual.ImageStim(
    win=win,
    name='leftImageCombo', 
    image='sin', mask=None,
    ori=0.0, pos=(-8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)
rightImageCombo = visual.ImageStim(
    win=win,
    name='rightImageCombo', 
    image='sin', mask=None,
    ori=0.0, pos=(8, -5), size=(5, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-2.0)
key_resp_22 = keyboard.Keyboard()

# Initialize components for Routine "stopShapeLoop"
stopShapeLoopClock = core.Clock()

# Initialize components for Routine "goodbye"
goodbyeClock = core.Clock()
headerGoodbye = visual.TextStim(win=win, name='headerGoodbye',
    text='Almost done! Just a few questions, please!',
    font='Open Sans',
    pos=(0, 6), height=2.0, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
messageGoodbye = visual.TextStim(win=win, name='messageGoodbye',
    text='Thank you for playing these games!\n\nThe study is ALMOST complete. We just have a few more questions for you over on REDCap. Please return to that tab of your browser and answer the final questions to complete the study.\n\nPress the space key to exit this window.',
    font='Open Sans',
    pos=(0, -2), height=1.0, wrapWidth=20.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_23 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_00.keys = []
key_resp_00.rt = []
_key_resp_00_allKeys = []
# keep track of which components have finished
welcomeComponents = [headerWelcome, welcomeText, instructContinue3, key_resp_00]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *headerWelcome* updates
    if headerWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        headerWelcome.frameNStart = frameN  # exact frame index
        headerWelcome.tStart = t  # local t and not account for scr refresh
        headerWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(headerWelcome, 'tStartRefresh')  # time at next scr refresh
        headerWelcome.setAutoDraw(True)
    
    # *welcomeText* updates
    if welcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeText.frameNStart = frameN  # exact frame index
        welcomeText.tStart = t  # local t and not account for scr refresh
        welcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeText, 'tStartRefresh')  # time at next scr refresh
        welcomeText.setAutoDraw(True)
    
    # *instructContinue3* updates
    if instructContinue3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructContinue3.frameNStart = frameN  # exact frame index
        instructContinue3.tStart = t  # local t and not account for scr refresh
        instructContinue3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructContinue3, 'tStartRefresh')  # time at next scr refresh
        instructContinue3.setAutoDraw(True)
    
    # *key_resp_00* updates
    waitOnFlip = False
    if key_resp_00.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_00.frameNStart = frameN  # exact frame index
        key_resp_00.tStart = t  # local t and not account for scr refresh
        key_resp_00.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_00, 'tStartRefresh')  # time at next scr refresh
        key_resp_00.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_00.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_00.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_00.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_00.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_00_allKeys.extend(theseKeys)
        if len(_key_resp_00_allKeys):
            key_resp_00.keys = _key_resp_00_allKeys[-1].name  # just the last key pressed
            key_resp_00.rt = _key_resp_00_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('headerWelcome.started', headerWelcome.tStartRefresh)
thisExp.addData('headerWelcome.stopped', headerWelcome.tStopRefresh)
thisExp.addData('welcomeText.started', welcomeText.tStartRefresh)
thisExp.addData('welcomeText.stopped', welcomeText.tStopRefresh)
thisExp.addData('instructContinue3.started', instructContinue3.tStartRefresh)
thisExp.addData('instructContinue3.stopped', instructContinue3.tStopRefresh)
# check responses
if key_resp_00.keys in ['', [], None]:  # No response was made
    key_resp_00.keys = None
thisExp.addData('key_resp_00.keys',key_resp_00.keys)
if key_resp_00.keys != None:  # we had a response
    thisExp.addData('key_resp_00.rt', key_resp_00.rt)
thisExp.addData('key_resp_00.started', key_resp_00.tStartRefresh)
thisExp.addData('key_resp_00.stopped', key_resp_00.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introReading"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_01.keys = []
key_resp_01.rt = []
_key_resp_01_allKeys = []
# keep track of which components have finished
introReadingComponents = [welcomeReading, key_resp_01, headerReading, instructContinue2]
for thisComponent in introReadingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introReadingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introReading"-------
while continueRoutine:
    # get current time
    t = introReadingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introReadingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeReading* updates
    if welcomeReading.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeReading.frameNStart = frameN  # exact frame index
        welcomeReading.tStart = t  # local t and not account for scr refresh
        welcomeReading.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeReading, 'tStartRefresh')  # time at next scr refresh
        welcomeReading.setAutoDraw(True)
    
    # *key_resp_01* updates
    waitOnFlip = False
    if key_resp_01.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_01.frameNStart = frameN  # exact frame index
        key_resp_01.tStart = t  # local t and not account for scr refresh
        key_resp_01.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_01, 'tStartRefresh')  # time at next scr refresh
        key_resp_01.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_01.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_01.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_01.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_01.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_01_allKeys.extend(theseKeys)
        if len(_key_resp_01_allKeys):
            key_resp_01.keys = _key_resp_01_allKeys[-1].name  # just the last key pressed
            key_resp_01.rt = _key_resp_01_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *headerReading* updates
    if headerReading.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        headerReading.frameNStart = frameN  # exact frame index
        headerReading.tStart = t  # local t and not account for scr refresh
        headerReading.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(headerReading, 'tStartRefresh')  # time at next scr refresh
        headerReading.setAutoDraw(True)
    
    # *instructContinue2* updates
    if instructContinue2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructContinue2.frameNStart = frameN  # exact frame index
        instructContinue2.tStart = t  # local t and not account for scr refresh
        instructContinue2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructContinue2, 'tStartRefresh')  # time at next scr refresh
        instructContinue2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introReadingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introReading"-------
for thisComponent in introReadingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcomeReading.started', welcomeReading.tStartRefresh)
thisExp.addData('welcomeReading.stopped', welcomeReading.tStopRefresh)
# check responses
if key_resp_01.keys in ['', [], None]:  # No response was made
    key_resp_01.keys = None
thisExp.addData('key_resp_01.keys',key_resp_01.keys)
if key_resp_01.keys != None:  # we had a response
    thisExp.addData('key_resp_01.rt', key_resp_01.rt)
thisExp.addData('key_resp_01.started', key_resp_01.tStartRefresh)
thisExp.addData('key_resp_01.stopped', key_resp_01.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('headerReading.started', headerReading.tStartRefresh)
thisExp.addData('headerReading.stopped', headerReading.tStopRefresh)
thisExp.addData('instructContinue2.started', instructContinue2.tStartRefresh)
thisExp.addData('instructContinue2.stopped', instructContinue2.tStopRefresh)
# the Routine "introReading" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructCalibration"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_02.keys = []
key_resp_02.rt = []
_key_resp_02_allKeys = []
# keep track of which components have finished
instructCalibrationComponents = [explainCalib, instructContinue4, key_resp_02]
for thisComponent in instructCalibrationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructCalibrationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructCalibration"-------
while continueRoutine:
    # get current time
    t = instructCalibrationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructCalibrationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *explainCalib* updates
    if explainCalib.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        explainCalib.frameNStart = frameN  # exact frame index
        explainCalib.tStart = t  # local t and not account for scr refresh
        explainCalib.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(explainCalib, 'tStartRefresh')  # time at next scr refresh
        explainCalib.setAutoDraw(True)
    
    # *instructContinue4* updates
    if instructContinue4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructContinue4.frameNStart = frameN  # exact frame index
        instructContinue4.tStart = t  # local t and not account for scr refresh
        instructContinue4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructContinue4, 'tStartRefresh')  # time at next scr refresh
        instructContinue4.setAutoDraw(True)
    
    # *key_resp_02* updates
    waitOnFlip = False
    if key_resp_02.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_02.frameNStart = frameN  # exact frame index
        key_resp_02.tStart = t  # local t and not account for scr refresh
        key_resp_02.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_02, 'tStartRefresh')  # time at next scr refresh
        key_resp_02.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_02.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_02.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_02.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_02.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_02_allKeys.extend(theseKeys)
        if len(_key_resp_02_allKeys):
            key_resp_02.keys = _key_resp_02_allKeys[-1].name  # just the last key pressed
            key_resp_02.rt = _key_resp_02_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructCalibrationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructCalibration"-------
for thisComponent in instructCalibrationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('explainCalib.started', explainCalib.tStartRefresh)
thisExp.addData('explainCalib.stopped', explainCalib.tStopRefresh)
thisExp.addData('instructContinue4.started', instructContinue4.tStartRefresh)
thisExp.addData('instructContinue4.stopped', instructContinue4.tStopRefresh)
# check responses
if key_resp_02.keys in ['', [], None]:  # No response was made
    key_resp_02.keys = None
thisExp.addData('key_resp_02.keys',key_resp_02.keys)
if key_resp_02.keys != None:  # we had a response
    thisExp.addData('key_resp_02.rt', key_resp_02.rt)
thisExp.addData('key_resp_02.started', key_resp_02.tStartRefresh)
thisExp.addData('key_resp_02.stopped', key_resp_02.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructCalibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "calibration"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
calibrationComponents = [calibText, calibTimer]
for thisComponent in calibrationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
calibrationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "calibration"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = calibrationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=calibrationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *calibText* updates
    if calibText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calibText.frameNStart = frameN  # exact frame index
        calibText.tStart = t  # local t and not account for scr refresh
        calibText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calibText, 'tStartRefresh')  # time at next scr refresh
        calibText.setAutoDraw(True)
    if calibText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > calibText.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            calibText.tStop = t  # not accounting for scr refresh
            calibText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(calibText, 'tStopRefresh')  # time at next scr refresh
            calibText.setAutoDraw(False)
    
    # *calibTimer* updates
    if calibTimer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calibTimer.frameNStart = frameN  # exact frame index
        calibTimer.tStart = t  # local t and not account for scr refresh
        calibTimer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calibTimer, 'tStartRefresh')  # time at next scr refresh
        calibTimer.setAutoDraw(True)
    if calibTimer.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > calibTimer.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            calibTimer.tStop = t  # not accounting for scr refresh
            calibTimer.frameNStop = frameN  # exact frame index
            win.timeOnFlip(calibTimer, 'tStopRefresh')  # time at next scr refresh
            calibTimer.setAutoDraw(False)
    if calibTimer.status == STARTED:  # only update if drawing
        calibTimer.setText(round(5 - t), log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in calibrationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "calibration"-------
for thisComponent in calibrationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('calibText.started', calibText.tStartRefresh)
thisExp.addData('calibText.stopped', calibText.tStopRefresh)
thisExp.addData('calibTimer.started', calibTimer.tStartRefresh)
thisExp.addData('calibTimer.stopped', calibTimer.tStopRefresh)

# ------Prepare to start Routine "instruct"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_03.keys = []
key_resp_03.rt = []
_key_resp_03_allKeys = []
# keep track of which components have finished
instructComponents = [text_3, instructContinue5, key_resp_03]
for thisComponent in instructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruct"-------
while continueRoutine:
    # get current time
    t = instructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *instructContinue5* updates
    if instructContinue5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructContinue5.frameNStart = frameN  # exact frame index
        instructContinue5.tStart = t  # local t and not account for scr refresh
        instructContinue5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructContinue5, 'tStartRefresh')  # time at next scr refresh
        instructContinue5.setAutoDraw(True)
    
    # *key_resp_03* updates
    waitOnFlip = False
    if key_resp_03.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_03.frameNStart = frameN  # exact frame index
        key_resp_03.tStart = t  # local t and not account for scr refresh
        key_resp_03.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_03, 'tStartRefresh')  # time at next scr refresh
        key_resp_03.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_03.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_03.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_03.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_03.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_03_allKeys.extend(theseKeys)
        if len(_key_resp_03_allKeys):
            key_resp_03.keys = _key_resp_03_allKeys[-1].name  # just the last key pressed
            key_resp_03.rt = _key_resp_03_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('instructContinue5.started', instructContinue5.tStartRefresh)
thisExp.addData('instructContinue5.stopped', instructContinue5.tStopRefresh)
# check responses
if key_resp_03.keys in ['', [], None]:  # No response was made
    key_resp_03.keys = None
thisExp.addData('key_resp_03.keys',key_resp_03.keys)
if key_resp_03.keys != None:  # we had a response
    thisExp.addData('key_resp_03.rt', key_resp_03.rt)
thisExp.addData('key_resp_03.started', key_resp_03.tStartRefresh)
thisExp.addData('key_resp_03.stopped', key_resp_03.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
counterbalance = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('resources/counterbalance/choose_' + participant_id[-1] + '.csv' ),
    seed=None, name='counterbalance')
thisExp.addLoop(counterbalance)  # add the loop to the experiment
thisCounterbalance = counterbalance.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCounterbalance.rgb)
if thisCounterbalance != None:
    for paramName in thisCounterbalance:
        exec('{} = thisCounterbalance[paramName]'.format(paramName))

for thisCounterbalance in counterbalance:
    currentLoop = counterbalance
    # abbreviate parameter names if possible (e.g. rgb = thisCounterbalance.rgb)
    if thisCounterbalance != None:
        for paramName in thisCounterbalance:
            exec('{} = thisCounterbalance[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(whichList),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "passage1"-------
        continueRoutine = True
        # update component parameters for each repeat
        passageText1.setText(firstList)
        key_resp_04.keys = []
        key_resp_04.rt = []
        _key_resp_04_allKeys = []
        # keep track of which components have finished
        passage1Components = [passageText1, instructContinue1, key_resp_04]
        for thisComponent in passage1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        passage1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "passage1"-------
        while continueRoutine:
            # get current time
            t = passage1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=passage1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *passageText1* updates
            if passageText1.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                passageText1.frameNStart = frameN  # exact frame index
                passageText1.tStart = t  # local t and not account for scr refresh
                passageText1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(passageText1, 'tStartRefresh')  # time at next scr refresh
                passageText1.setAutoDraw(True)
            
            # *instructContinue1* updates
            if instructContinue1.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                instructContinue1.frameNStart = frameN  # exact frame index
                instructContinue1.tStart = t  # local t and not account for scr refresh
                instructContinue1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructContinue1, 'tStartRefresh')  # time at next scr refresh
                instructContinue1.setAutoDraw(True)
            
            # *key_resp_04* updates
            waitOnFlip = False
            if key_resp_04.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                key_resp_04.frameNStart = frameN  # exact frame index
                key_resp_04.tStart = t  # local t and not account for scr refresh
                key_resp_04.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_04, 'tStartRefresh')  # time at next scr refresh
                key_resp_04.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_04.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_04.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_04.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_04.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_04_allKeys.extend(theseKeys)
                if len(_key_resp_04_allKeys):
                    key_resp_04.keys = _key_resp_04_allKeys[-1].name  # just the last key pressed
                    key_resp_04.rt = _key_resp_04_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in passage1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "passage1"-------
        for thisComponent in passage1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        passageCount += 1
        trials.addData('passageText1.started', passageText1.tStartRefresh)
        trials.addData('passageText1.stopped', passageText1.tStopRefresh)
        trials.addData('instructContinue1.started', instructContinue1.tStartRefresh)
        trials.addData('instructContinue1.stopped', instructContinue1.tStopRefresh)
        # check responses
        if key_resp_04.keys in ['', [], None]:  # No response was made
            key_resp_04.keys = None
        trials.addData('key_resp_04.keys',key_resp_04.keys)
        if key_resp_04.keys != None:  # we had a response
            trials.addData('key_resp_04.rt', key_resp_04.rt)
        trials.addData('key_resp_04.started', key_resp_04.tStartRefresh)
        trials.addData('key_resp_04.stopped', key_resp_04.tStopRefresh)
        # the Routine "passage1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "challenge1"-------
        continueRoutine = True
        # update component parameters for each repeat
        challengeText1.setText(firstchallengeQuestion)
        challengeResponse1.keys = []
        challengeResponse1.rt = []
        _challengeResponse1_allKeys = []
        challengeOptions1.setText(firstletterA + str(firstchoiceA) + '\n' + firstletterB + str(firstchoiceB) + '\n' + firstletterC + str(firstchoiceC) + '\n' + firstletterD + str(firstchoiceD))
        counterText1.setText(str(passageCount) + ' of 20')
        # keep track of which components have finished
        challenge1Components = [challengeText1, challengeResponse1, challengeOptions1, answerInstruct1, counterText1]
        for thisComponent in challenge1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        challenge1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "challenge1"-------
        while continueRoutine:
            # get current time
            t = challenge1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=challenge1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *challengeText1* updates
            if challengeText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                challengeText1.frameNStart = frameN  # exact frame index
                challengeText1.tStart = t  # local t and not account for scr refresh
                challengeText1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(challengeText1, 'tStartRefresh')  # time at next scr refresh
                challengeText1.setAutoDraw(True)
            
            # *challengeResponse1* updates
            waitOnFlip = False
            if challengeResponse1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                challengeResponse1.frameNStart = frameN  # exact frame index
                challengeResponse1.tStart = t  # local t and not account for scr refresh
                challengeResponse1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(challengeResponse1, 'tStartRefresh')  # time at next scr refresh
                challengeResponse1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(challengeResponse1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(challengeResponse1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if challengeResponse1.status == STARTED and not waitOnFlip:
                theseKeys = challengeResponse1.getKeys(keyList=['a', 'b', 'c', 'd'], waitRelease=False)
                _challengeResponse1_allKeys.extend(theseKeys)
                if len(_challengeResponse1_allKeys):
                    challengeResponse1.keys = _challengeResponse1_allKeys[-1].name  # just the last key pressed
                    challengeResponse1.rt = _challengeResponse1_allKeys[-1].rt
                    # was this correct?
                    if (challengeResponse1.keys == str(firstcorrectAnswer)) or (challengeResponse1.keys == firstcorrectAnswer):
                        challengeResponse1.corr = 1
                    else:
                        challengeResponse1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *challengeOptions1* updates
            if challengeOptions1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                challengeOptions1.frameNStart = frameN  # exact frame index
                challengeOptions1.tStart = t  # local t and not account for scr refresh
                challengeOptions1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(challengeOptions1, 'tStartRefresh')  # time at next scr refresh
                challengeOptions1.setAutoDraw(True)
            
            # *answerInstruct1* updates
            if answerInstruct1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                answerInstruct1.frameNStart = frameN  # exact frame index
                answerInstruct1.tStart = t  # local t and not account for scr refresh
                answerInstruct1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(answerInstruct1, 'tStartRefresh')  # time at next scr refresh
                answerInstruct1.setAutoDraw(True)
            
            # *counterText1* updates
            if counterText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                counterText1.frameNStart = frameN  # exact frame index
                counterText1.tStart = t  # local t and not account for scr refresh
                counterText1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(counterText1, 'tStartRefresh')  # time at next scr refresh
                counterText1.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in challenge1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "challenge1"-------
        for thisComponent in challenge1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('challengeText1.started', challengeText1.tStartRefresh)
        trials.addData('challengeText1.stopped', challengeText1.tStopRefresh)
        # check responses
        if challengeResponse1.keys in ['', [], None]:  # No response was made
            challengeResponse1.keys = None
            # was no response the correct answer?!
            if str(firstcorrectAnswer).lower() == 'none':
               challengeResponse1.corr = 1;  # correct non-response
            else:
               challengeResponse1.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('challengeResponse1.keys',challengeResponse1.keys)
        trials.addData('challengeResponse1.corr', challengeResponse1.corr)
        if challengeResponse1.keys != None:  # we had a response
            trials.addData('challengeResponse1.rt', challengeResponse1.rt)
        trials.addData('challengeResponse1.started', challengeResponse1.tStartRefresh)
        trials.addData('challengeResponse1.stopped', challengeResponse1.tStopRefresh)
        trials.addData('challengeOptions1.started', challengeOptions1.tStartRefresh)
        trials.addData('challengeOptions1.stopped', challengeOptions1.tStopRefresh)
        trials.addData('answerInstruct1.started', answerInstruct1.tStartRefresh)
        trials.addData('answerInstruct1.stopped', answerInstruct1.tStopRefresh)
        trials.addData('counterText1.started', counterText1.tStartRefresh)
        trials.addData('counterText1.stopped', counterText1.tStopRefresh)
        # the Routine "challenge1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "readyScreen1"-------
        continueRoutine = True
        routineTimer.add(60.000000)
        # update component parameters for each repeat
        key_resp_05.keys = []
        key_resp_05.rt = []
        _key_resp_05_allKeys = []
        # keep track of which components have finished
        readyScreen1Components = [readingBreak1, key_resp_05, timer1]
        for thisComponent in readyScreen1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        readyScreen1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "readyScreen1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = readyScreen1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=readyScreen1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *readingBreak1* updates
            if readingBreak1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                readingBreak1.frameNStart = frameN  # exact frame index
                readingBreak1.tStart = t  # local t and not account for scr refresh
                readingBreak1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(readingBreak1, 'tStartRefresh')  # time at next scr refresh
                readingBreak1.setAutoDraw(True)
            if readingBreak1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > readingBreak1.tStartRefresh + 60.0-frameTolerance:
                    # keep track of stop time/frame for later
                    readingBreak1.tStop = t  # not accounting for scr refresh
                    readingBreak1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(readingBreak1, 'tStopRefresh')  # time at next scr refresh
                    readingBreak1.setAutoDraw(False)
            
            # *key_resp_05* updates
            waitOnFlip = False
            if key_resp_05.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_05.frameNStart = frameN  # exact frame index
                key_resp_05.tStart = t  # local t and not account for scr refresh
                key_resp_05.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_05, 'tStartRefresh')  # time at next scr refresh
                key_resp_05.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_05.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_05.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_05.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_05.tStartRefresh + 60.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_05.tStop = t  # not accounting for scr refresh
                    key_resp_05.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_05, 'tStopRefresh')  # time at next scr refresh
                    key_resp_05.status = FINISHED
            if key_resp_05.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_05.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_05_allKeys.extend(theseKeys)
                if len(_key_resp_05_allKeys):
                    key_resp_05.keys = _key_resp_05_allKeys[-1].name  # just the last key pressed
                    key_resp_05.rt = _key_resp_05_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *timer1* updates
            if timer1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timer1.frameNStart = frameN  # exact frame index
                timer1.tStart = t  # local t and not account for scr refresh
                timer1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer1, 'tStartRefresh')  # time at next scr refresh
                timer1.setAutoDraw(True)
            if timer1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > timer1.tStartRefresh + 60.0-frameTolerance:
                    # keep track of stop time/frame for later
                    timer1.tStop = t  # not accounting for scr refresh
                    timer1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(timer1, 'tStopRefresh')  # time at next scr refresh
                    timer1.setAutoDraw(False)
            if timer1.status == STARTED:  # only update if drawing
                timer1.setText(round(60 - t), log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in readyScreen1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "readyScreen1"-------
        for thisComponent in readyScreen1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('readingBreak1.started', readingBreak1.tStartRefresh)
        trials.addData('readingBreak1.stopped', readingBreak1.tStopRefresh)
        # check responses
        if key_resp_05.keys in ['', [], None]:  # No response was made
            key_resp_05.keys = None
        trials.addData('key_resp_05.keys',key_resp_05.keys)
        if key_resp_05.keys != None:  # we had a response
            trials.addData('key_resp_05.rt', key_resp_05.rt)
        trials.addData('key_resp_05.started', key_resp_05.tStartRefresh)
        trials.addData('key_resp_05.stopped', key_resp_05.tStopRefresh)
        trials.addData('timer1.started', timer1.tStartRefresh)
        trials.addData('timer1.stopped', timer1.tStopRefresh)
        
        # ------Prepare to start Routine "passage2"-------
        continueRoutine = True
        # update component parameters for each repeat
        passageText2.setText(secondList)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        passage2Components = [passageText2, instructContinue2_2, key_resp]
        for thisComponent in passage2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        passage2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "passage2"-------
        while continueRoutine:
            # get current time
            t = passage2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=passage2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *passageText2* updates
            if passageText2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                passageText2.frameNStart = frameN  # exact frame index
                passageText2.tStart = t  # local t and not account for scr refresh
                passageText2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(passageText2, 'tStartRefresh')  # time at next scr refresh
                passageText2.setAutoDraw(True)
            
            # *instructContinue2_2* updates
            if instructContinue2_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                instructContinue2_2.frameNStart = frameN  # exact frame index
                instructContinue2_2.tStart = t  # local t and not account for scr refresh
                instructContinue2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructContinue2_2, 'tStartRefresh')  # time at next scr refresh
                instructContinue2_2.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in passage2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "passage2"-------
        for thisComponent in passage2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        passageCount += 1
        trials.addData('passageText2.started', passageText2.tStartRefresh)
        trials.addData('passageText2.stopped', passageText2.tStopRefresh)
        trials.addData('instructContinue2_2.started', instructContinue2_2.tStartRefresh)
        trials.addData('instructContinue2_2.stopped', instructContinue2_2.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        trials.addData('key_resp.started', key_resp.tStartRefresh)
        trials.addData('key_resp.stopped', key_resp.tStopRefresh)
        # the Routine "passage2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "challenge2"-------
        continueRoutine = True
        # update component parameters for each repeat
        challengeText2.setText(secondchallengeQuestion)
        challengeResponse2.keys = []
        challengeResponse2.rt = []
        _challengeResponse2_allKeys = []
        challengeOptions2.setText(secondletterA + str(secondchoiceA) + '\n' + secondletterB + str(secondchoiceB) + '\n' + secondletterC + str(secondchoiceC) + '\n' + secondletterD + str(secondchoiceD))
        counterText2.setText(str(passageCount) + ' of 20')
        # keep track of which components have finished
        challenge2Components = [challengeText2, challengeResponse2, challengeOptions2, answerInstruct2, counterText2]
        for thisComponent in challenge2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        challenge2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "challenge2"-------
        while continueRoutine:
            # get current time
            t = challenge2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=challenge2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *challengeText2* updates
            if challengeText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                challengeText2.frameNStart = frameN  # exact frame index
                challengeText2.tStart = t  # local t and not account for scr refresh
                challengeText2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(challengeText2, 'tStartRefresh')  # time at next scr refresh
                challengeText2.setAutoDraw(True)
            
            # *challengeResponse2* updates
            waitOnFlip = False
            if challengeResponse2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                challengeResponse2.frameNStart = frameN  # exact frame index
                challengeResponse2.tStart = t  # local t and not account for scr refresh
                challengeResponse2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(challengeResponse2, 'tStartRefresh')  # time at next scr refresh
                challengeResponse2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(challengeResponse2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(challengeResponse2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if challengeResponse2.status == STARTED and not waitOnFlip:
                theseKeys = challengeResponse2.getKeys(keyList=['a', 'b', 'c', 'd'], waitRelease=False)
                _challengeResponse2_allKeys.extend(theseKeys)
                if len(_challengeResponse2_allKeys):
                    challengeResponse2.keys = _challengeResponse2_allKeys[-1].name  # just the last key pressed
                    challengeResponse2.rt = _challengeResponse2_allKeys[-1].rt
                    # was this correct?
                    if (challengeResponse2.keys == str(secondcorrectAnswer)) or (challengeResponse2.keys == secondcorrectAnswer):
                        challengeResponse2.corr = 1
                    else:
                        challengeResponse2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *challengeOptions2* updates
            if challengeOptions2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                challengeOptions2.frameNStart = frameN  # exact frame index
                challengeOptions2.tStart = t  # local t and not account for scr refresh
                challengeOptions2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(challengeOptions2, 'tStartRefresh')  # time at next scr refresh
                challengeOptions2.setAutoDraw(True)
            
            # *answerInstruct2* updates
            if answerInstruct2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                answerInstruct2.frameNStart = frameN  # exact frame index
                answerInstruct2.tStart = t  # local t and not account for scr refresh
                answerInstruct2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(answerInstruct2, 'tStartRefresh')  # time at next scr refresh
                answerInstruct2.setAutoDraw(True)
            
            # *counterText2* updates
            if counterText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                counterText2.frameNStart = frameN  # exact frame index
                counterText2.tStart = t  # local t and not account for scr refresh
                counterText2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(counterText2, 'tStartRefresh')  # time at next scr refresh
                counterText2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in challenge2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "challenge2"-------
        for thisComponent in challenge2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('challengeText2.started', challengeText2.tStartRefresh)
        trials.addData('challengeText2.stopped', challengeText2.tStopRefresh)
        # check responses
        if challengeResponse2.keys in ['', [], None]:  # No response was made
            challengeResponse2.keys = None
            # was no response the correct answer?!
            if str(secondcorrectAnswer).lower() == 'none':
               challengeResponse2.corr = 1;  # correct non-response
            else:
               challengeResponse2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('challengeResponse2.keys',challengeResponse2.keys)
        trials.addData('challengeResponse2.corr', challengeResponse2.corr)
        if challengeResponse2.keys != None:  # we had a response
            trials.addData('challengeResponse2.rt', challengeResponse2.rt)
        trials.addData('challengeResponse2.started', challengeResponse2.tStartRefresh)
        trials.addData('challengeResponse2.stopped', challengeResponse2.tStopRefresh)
        trials.addData('challengeOptions2.started', challengeOptions2.tStartRefresh)
        trials.addData('challengeOptions2.stopped', challengeOptions2.tStopRefresh)
        trials.addData('answerInstruct2.started', answerInstruct2.tStartRefresh)
        trials.addData('answerInstruct2.stopped', answerInstruct2.tStopRefresh)
        trials.addData('counterText2.started', counterText2.tStartRefresh)
        trials.addData('counterText2.stopped', counterText2.tStopRefresh)
        # the Routine "challenge2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "readyScreen2"-------
        continueRoutine = True
        routineTimer.add(60.000000)
        # update component parameters for each repeat
        if passageCount == 4:
            continueRoutine = False
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        readyScreen2Components = [readingBreak2, key_resp_2, timer2]
        for thisComponent in readyScreen2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        readyScreen2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "readyScreen2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = readyScreen2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=readyScreen2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *readingBreak2* updates
            if readingBreak2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                readingBreak2.frameNStart = frameN  # exact frame index
                readingBreak2.tStart = t  # local t and not account for scr refresh
                readingBreak2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(readingBreak2, 'tStartRefresh')  # time at next scr refresh
                readingBreak2.setAutoDraw(True)
            if readingBreak2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > readingBreak2.tStartRefresh + 60.0-frameTolerance:
                    # keep track of stop time/frame for later
                    readingBreak2.tStop = t  # not accounting for scr refresh
                    readingBreak2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(readingBreak2, 'tStopRefresh')  # time at next scr refresh
                    readingBreak2.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 60.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *timer2* updates
            if timer2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timer2.frameNStart = frameN  # exact frame index
                timer2.tStart = t  # local t and not account for scr refresh
                timer2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer2, 'tStartRefresh')  # time at next scr refresh
                timer2.setAutoDraw(True)
            if timer2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > timer2.tStartRefresh + 60.0-frameTolerance:
                    # keep track of stop time/frame for later
                    timer2.tStop = t  # not accounting for scr refresh
                    timer2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(timer2, 'tStopRefresh')  # time at next scr refresh
                    timer2.setAutoDraw(False)
            if timer2.status == STARTED:  # only update if drawing
                timer2.setText(round(60 - t), log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in readyScreen2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "readyScreen2"-------
        for thisComponent in readyScreen2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('readingBreak2.started', readingBreak2.tStartRefresh)
        trials.addData('readingBreak2.stopped', readingBreak2.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        trials.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials.addData('key_resp_2.rt', key_resp_2.rt)
        trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        trials.addData('timer2.started', timer2.tStartRefresh)
        trials.addData('timer2.stopped', timer2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'counterbalance'


# ------Prepare to start Routine "readComplete"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_06.keys = []
key_resp_06.rt = []
_key_resp_06_allKeys = []
# keep track of which components have finished
readCompleteComponents = [readCompleteintroLDT, key_resp_06, instructContinue6]
for thisComponent in readCompleteComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
readCompleteClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "readComplete"-------
while continueRoutine:
    # get current time
    t = readCompleteClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=readCompleteClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *readCompleteintroLDT* updates
    if readCompleteintroLDT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        readCompleteintroLDT.frameNStart = frameN  # exact frame index
        readCompleteintroLDT.tStart = t  # local t and not account for scr refresh
        readCompleteintroLDT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(readCompleteintroLDT, 'tStartRefresh')  # time at next scr refresh
        readCompleteintroLDT.setAutoDraw(True)
    
    # *key_resp_06* updates
    waitOnFlip = False
    if key_resp_06.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_06.frameNStart = frameN  # exact frame index
        key_resp_06.tStart = t  # local t and not account for scr refresh
        key_resp_06.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_06, 'tStartRefresh')  # time at next scr refresh
        key_resp_06.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_06.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_06.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_06.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_06.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_06_allKeys.extend(theseKeys)
        if len(_key_resp_06_allKeys):
            key_resp_06.keys = _key_resp_06_allKeys[-1].name  # just the last key pressed
            key_resp_06.rt = _key_resp_06_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructContinue6* updates
    if instructContinue6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructContinue6.frameNStart = frameN  # exact frame index
        instructContinue6.tStart = t  # local t and not account for scr refresh
        instructContinue6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructContinue6, 'tStartRefresh')  # time at next scr refresh
        instructContinue6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readCompleteComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "readComplete"-------
for thisComponent in readCompleteComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('readCompleteintroLDT.started', readCompleteintroLDT.tStartRefresh)
thisExp.addData('readCompleteintroLDT.stopped', readCompleteintroLDT.tStopRefresh)
# check responses
if key_resp_06.keys in ['', [], None]:  # No response was made
    key_resp_06.keys = None
thisExp.addData('key_resp_06.keys',key_resp_06.keys)
if key_resp_06.keys != None:  # we had a response
    thisExp.addData('key_resp_06.rt', key_resp_06.rt)
thisExp.addData('key_resp_06.started', key_resp_06.tStartRefresh)
thisExp.addData('key_resp_06.stopped', key_resp_06.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instructContinue6.started', instructContinue6.tStartRefresh)
thisExp.addData('instructContinue6.stopped', instructContinue6.tStopRefresh)
# the Routine "readComplete" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introLDT"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_07.keys = []
key_resp_07.rt = []
_key_resp_07_allKeys = []
# keep track of which components have finished
introLDTComponents = [welcomeLDT, headerLDT, key_resp_07, ldtWelcomeResponseF, ldtWelcomeResponseJ]
for thisComponent in introLDTComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introLDTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introLDT"-------
while continueRoutine:
    # get current time
    t = introLDTClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introLDTClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeLDT* updates
    if welcomeLDT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeLDT.frameNStart = frameN  # exact frame index
        welcomeLDT.tStart = t  # local t and not account for scr refresh
        welcomeLDT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeLDT, 'tStartRefresh')  # time at next scr refresh
        welcomeLDT.setAutoDraw(True)
    
    # *headerLDT* updates
    if headerLDT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        headerLDT.frameNStart = frameN  # exact frame index
        headerLDT.tStart = t  # local t and not account for scr refresh
        headerLDT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(headerLDT, 'tStartRefresh')  # time at next scr refresh
        headerLDT.setAutoDraw(True)
    
    # *key_resp_07* updates
    waitOnFlip = False
    if key_resp_07.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_07.frameNStart = frameN  # exact frame index
        key_resp_07.tStart = t  # local t and not account for scr refresh
        key_resp_07.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_07, 'tStartRefresh')  # time at next scr refresh
        key_resp_07.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_07.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_07.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_07.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_07.getKeys(keyList=['f', 'j'], waitRelease=False)
        _key_resp_07_allKeys.extend(theseKeys)
        if len(_key_resp_07_allKeys):
            key_resp_07.keys = _key_resp_07_allKeys[-1].name  # just the last key pressed
            key_resp_07.rt = _key_resp_07_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ldtWelcomeResponseF* updates
    if ldtWelcomeResponseF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ldtWelcomeResponseF.frameNStart = frameN  # exact frame index
        ldtWelcomeResponseF.tStart = t  # local t and not account for scr refresh
        ldtWelcomeResponseF.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ldtWelcomeResponseF, 'tStartRefresh')  # time at next scr refresh
        ldtWelcomeResponseF.setAutoDraw(True)
    
    # *ldtWelcomeResponseJ* updates
    if ldtWelcomeResponseJ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ldtWelcomeResponseJ.frameNStart = frameN  # exact frame index
        ldtWelcomeResponseJ.tStart = t  # local t and not account for scr refresh
        ldtWelcomeResponseJ.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ldtWelcomeResponseJ, 'tStartRefresh')  # time at next scr refresh
        ldtWelcomeResponseJ.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introLDTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introLDT"-------
for thisComponent in introLDTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcomeLDT.started', welcomeLDT.tStartRefresh)
thisExp.addData('welcomeLDT.stopped', welcomeLDT.tStopRefresh)
thisExp.addData('headerLDT.started', headerLDT.tStartRefresh)
thisExp.addData('headerLDT.stopped', headerLDT.tStopRefresh)
# check responses
if key_resp_07.keys in ['', [], None]:  # No response was made
    key_resp_07.keys = None
thisExp.addData('key_resp_07.keys',key_resp_07.keys)
if key_resp_07.keys != None:  # we had a response
    thisExp.addData('key_resp_07.rt', key_resp_07.rt)
thisExp.addData('key_resp_07.started', key_resp_07.tStartRefresh)
thisExp.addData('key_resp_07.stopped', key_resp_07.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('ldtWelcomeResponseF.started', ldtWelcomeResponseF.tStartRefresh)
thisExp.addData('ldtWelcomeResponseF.stopped', ldtWelcomeResponseF.tStopRefresh)
thisExp.addData('ldtWelcomeResponseJ.started', ldtWelcomeResponseJ.tStartRefresh)
thisExp.addData('ldtWelcomeResponseJ.stopped', ldtWelcomeResponseJ.tStopRefresh)
# the Routine "introLDT" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introPractice"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_08.keys = []
key_resp_08.rt = []
_key_resp_08_allKeys = []
# keep track of which components have finished
introPracticeComponents = [introPracticeText, key_resp_08, ldtIntroResponseF, ldtIntroResponseJ]
for thisComponent in introPracticeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introPractice"-------
while continueRoutine:
    # get current time
    t = introPracticeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introPracticeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introPracticeText* updates
    if introPracticeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introPracticeText.frameNStart = frameN  # exact frame index
        introPracticeText.tStart = t  # local t and not account for scr refresh
        introPracticeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introPracticeText, 'tStartRefresh')  # time at next scr refresh
        introPracticeText.setAutoDraw(True)
    
    # *key_resp_08* updates
    waitOnFlip = False
    if key_resp_08.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_08.frameNStart = frameN  # exact frame index
        key_resp_08.tStart = t  # local t and not account for scr refresh
        key_resp_08.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_08, 'tStartRefresh')  # time at next scr refresh
        key_resp_08.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_08.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_08.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_08.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_08.getKeys(keyList=['f', 'j'], waitRelease=False)
        _key_resp_08_allKeys.extend(theseKeys)
        if len(_key_resp_08_allKeys):
            key_resp_08.keys = _key_resp_08_allKeys[-1].name  # just the last key pressed
            key_resp_08.rt = _key_resp_08_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ldtIntroResponseF* updates
    if ldtIntroResponseF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ldtIntroResponseF.frameNStart = frameN  # exact frame index
        ldtIntroResponseF.tStart = t  # local t and not account for scr refresh
        ldtIntroResponseF.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ldtIntroResponseF, 'tStartRefresh')  # time at next scr refresh
        ldtIntroResponseF.setAutoDraw(True)
    
    # *ldtIntroResponseJ* updates
    if ldtIntroResponseJ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ldtIntroResponseJ.frameNStart = frameN  # exact frame index
        ldtIntroResponseJ.tStart = t  # local t and not account for scr refresh
        ldtIntroResponseJ.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ldtIntroResponseJ, 'tStartRefresh')  # time at next scr refresh
        ldtIntroResponseJ.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introPractice"-------
for thisComponent in introPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introPracticeText.started', introPracticeText.tStartRefresh)
thisExp.addData('introPracticeText.stopped', introPracticeText.tStopRefresh)
# check responses
if key_resp_08.keys in ['', [], None]:  # No response was made
    key_resp_08.keys = None
thisExp.addData('key_resp_08.keys',key_resp_08.keys)
if key_resp_08.keys != None:  # we had a response
    thisExp.addData('key_resp_08.rt', key_resp_08.rt)
thisExp.addData('key_resp_08.started', key_resp_08.tStartRefresh)
thisExp.addData('key_resp_08.stopped', key_resp_08.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('ldtIntroResponseF.started', ldtIntroResponseF.tStartRefresh)
thisExp.addData('ldtIntroResponseF.stopped', ldtIntroResponseF.tStopRefresh)
thisExp.addData('ldtIntroResponseJ.started', ldtIntroResponseJ.tStartRefresh)
thisExp.addData('ldtIntroResponseJ.stopped', ldtIntroResponseJ.tStopRefresh)
# the Routine "introPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introPractice2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
introPractice2Components = [introPracticeText2, key_resp_24, ldtIntroResponseF2, ldtIntroResponseJ2]
for thisComponent in introPractice2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introPractice2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introPractice2"-------
while continueRoutine:
    # get current time
    t = introPractice2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introPractice2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introPracticeText2* updates
    if introPracticeText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introPracticeText2.frameNStart = frameN  # exact frame index
        introPracticeText2.tStart = t  # local t and not account for scr refresh
        introPracticeText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introPracticeText2, 'tStartRefresh')  # time at next scr refresh
        introPracticeText2.setAutoDraw(True)
    
    # *key_resp_24* updates
    waitOnFlip = False
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['f', 'j'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ldtIntroResponseF2* updates
    if ldtIntroResponseF2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ldtIntroResponseF2.frameNStart = frameN  # exact frame index
        ldtIntroResponseF2.tStart = t  # local t and not account for scr refresh
        ldtIntroResponseF2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ldtIntroResponseF2, 'tStartRefresh')  # time at next scr refresh
        ldtIntroResponseF2.setAutoDraw(True)
    
    # *ldtIntroResponseJ2* updates
    if ldtIntroResponseJ2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ldtIntroResponseJ2.frameNStart = frameN  # exact frame index
        ldtIntroResponseJ2.tStart = t  # local t and not account for scr refresh
        ldtIntroResponseJ2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ldtIntroResponseJ2, 'tStartRefresh')  # time at next scr refresh
        ldtIntroResponseJ2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introPractice2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introPractice2"-------
for thisComponent in introPractice2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introPracticeText2.started', introPracticeText2.tStartRefresh)
thisExp.addData('introPracticeText2.stopped', introPracticeText2.tStopRefresh)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
thisExp.addData('key_resp_24.started', key_resp_24.tStartRefresh)
thisExp.addData('key_resp_24.stopped', key_resp_24.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('ldtIntroResponseF2.started', ldtIntroResponseF2.tStartRefresh)
thisExp.addData('ldtIntroResponseF2.stopped', ldtIntroResponseF2.tStopRefresh)
thisExp.addData('ldtIntroResponseJ2.started', ldtIntroResponseJ2.tStartRefresh)
thisExp.addData('ldtIntroResponseJ2.stopped', ldtIntroResponseJ2.tStopRefresh)
# the Routine "introPractice2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('resources/ldt_practice.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixPractice"-------
    continueRoutine = True
    routineTimer.add(0.400000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixPracticeComponents = [fixPracticecross]
    for thisComponent in fixPracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixPractice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixPracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixPracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixPracticecross* updates
        if fixPracticecross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixPracticecross.frameNStart = frameN  # exact frame index
            fixPracticecross.tStart = t  # local t and not account for scr refresh
            fixPracticecross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixPracticecross, 'tStartRefresh')  # time at next scr refresh
            fixPracticecross.setAutoDraw(True)
        if fixPracticecross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixPracticecross.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                fixPracticecross.tStop = t  # not accounting for scr refresh
                fixPracticecross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixPracticecross, 'tStopRefresh')  # time at next scr refresh
                fixPracticecross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixPractice"-------
    for thisComponent in fixPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('fixPracticecross.started', fixPracticecross.tStartRefresh)
    trials_2.addData('fixPracticecross.stopped', fixPracticecross.tStopRefresh)
    
    # ------Prepare to start Routine "ldtPractice"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    ldtPracticeWord.setText(ldtPractice)
    practiceResponse.keys = []
    practiceResponse.rt = []
    _practiceResponse_allKeys = []
    # keep track of which components have finished
    ldtPracticeComponents = [ldtPracticeWord, practiceResponse, ldtPracticeResponseF, ldtPracticeResponseJ]
    for thisComponent in ldtPracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ldtPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ldtPractice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ldtPracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ldtPracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ldtPracticeWord* updates
        if ldtPracticeWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ldtPracticeWord.frameNStart = frameN  # exact frame index
            ldtPracticeWord.tStart = t  # local t and not account for scr refresh
            ldtPracticeWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ldtPracticeWord, 'tStartRefresh')  # time at next scr refresh
            ldtPracticeWord.setAutoDraw(True)
        if ldtPracticeWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ldtPracticeWord.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                ldtPracticeWord.tStop = t  # not accounting for scr refresh
                ldtPracticeWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ldtPracticeWord, 'tStopRefresh')  # time at next scr refresh
                ldtPracticeWord.setAutoDraw(False)
        
        # *practiceResponse* updates
        waitOnFlip = False
        if practiceResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practiceResponse.frameNStart = frameN  # exact frame index
            practiceResponse.tStart = t  # local t and not account for scr refresh
            practiceResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceResponse, 'tStartRefresh')  # time at next scr refresh
            practiceResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(practiceResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(practiceResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practiceResponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practiceResponse.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                practiceResponse.tStop = t  # not accounting for scr refresh
                practiceResponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practiceResponse, 'tStopRefresh')  # time at next scr refresh
                practiceResponse.status = FINISHED
        if practiceResponse.status == STARTED and not waitOnFlip:
            theseKeys = practiceResponse.getKeys(keyList=['f', 'j'], waitRelease=False)
            _practiceResponse_allKeys.extend(theseKeys)
            if len(_practiceResponse_allKeys):
                practiceResponse.keys = _practiceResponse_allKeys[-1].name  # just the last key pressed
                practiceResponse.rt = _practiceResponse_allKeys[-1].rt
                # was this correct?
                if (practiceResponse.keys == str(correctAnswer)) or (practiceResponse.keys == correctAnswer):
                    practiceResponse.corr = 1
                else:
                    practiceResponse.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *ldtPracticeResponseF* updates
        if ldtPracticeResponseF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ldtPracticeResponseF.frameNStart = frameN  # exact frame index
            ldtPracticeResponseF.tStart = t  # local t and not account for scr refresh
            ldtPracticeResponseF.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ldtPracticeResponseF, 'tStartRefresh')  # time at next scr refresh
            ldtPracticeResponseF.setAutoDraw(True)
        if ldtPracticeResponseF.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ldtPracticeResponseF.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                ldtPracticeResponseF.tStop = t  # not accounting for scr refresh
                ldtPracticeResponseF.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ldtPracticeResponseF, 'tStopRefresh')  # time at next scr refresh
                ldtPracticeResponseF.setAutoDraw(False)
        
        # *ldtPracticeResponseJ* updates
        if ldtPracticeResponseJ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ldtPracticeResponseJ.frameNStart = frameN  # exact frame index
            ldtPracticeResponseJ.tStart = t  # local t and not account for scr refresh
            ldtPracticeResponseJ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ldtPracticeResponseJ, 'tStartRefresh')  # time at next scr refresh
            ldtPracticeResponseJ.setAutoDraw(True)
        if ldtPracticeResponseJ.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ldtPracticeResponseJ.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                ldtPracticeResponseJ.tStop = t  # not accounting for scr refresh
                ldtPracticeResponseJ.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ldtPracticeResponseJ, 'tStopRefresh')  # time at next scr refresh
                ldtPracticeResponseJ.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ldtPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ldtPractice"-------
    for thisComponent in ldtPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('ldtPracticeWord.started', ldtPracticeWord.tStartRefresh)
    trials_2.addData('ldtPracticeWord.stopped', ldtPracticeWord.tStopRefresh)
    # check responses
    if practiceResponse.keys in ['', [], None]:  # No response was made
        practiceResponse.keys = None
        # was no response the correct answer?!
        if str(correctAnswer).lower() == 'none':
           practiceResponse.corr = 1;  # correct non-response
        else:
           practiceResponse.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('practiceResponse.keys',practiceResponse.keys)
    trials_2.addData('practiceResponse.corr', practiceResponse.corr)
    if practiceResponse.keys != None:  # we had a response
        trials_2.addData('practiceResponse.rt', practiceResponse.rt)
    trials_2.addData('practiceResponse.started', practiceResponse.tStartRefresh)
    trials_2.addData('practiceResponse.stopped', practiceResponse.tStopRefresh)
    trials_2.addData('ldtPracticeResponseF.started', ldtPracticeResponseF.tStartRefresh)
    trials_2.addData('ldtPracticeResponseF.stopped', ldtPracticeResponseF.tStopRefresh)
    trials_2.addData('ldtPracticeResponseJ.started', ldtPracticeResponseJ.tStartRefresh)
    trials_2.addData('ldtPracticeResponseJ.stopped', ldtPracticeResponseJ.tStopRefresh)
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if not practiceResponse.keys :
        msg="Sorry, too slow."
    elif practiceResponse.corr:
        msg="Correct!"
    else:
        msg="Oops! That was wrong."
    feedbackMessage.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedbackMessage]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackMessage* updates
        if feedbackMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackMessage.frameNStart = frameN  # exact frame index
            feedbackMessage.tStart = t  # local t and not account for scr refresh
            feedbackMessage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackMessage, 'tStartRefresh')  # time at next scr refresh
            feedbackMessage.setAutoDraw(True)
        if feedbackMessage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackMessage.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedbackMessage.tStop = t  # not accounting for scr refresh
                feedbackMessage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackMessage, 'tStopRefresh')  # time at next scr refresh
                feedbackMessage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('feedbackMessage.started', feedbackMessage.tStartRefresh)
    trials_2.addData('feedbackMessage.stopped', feedbackMessage.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# ------Prepare to start Routine "moreInstruct"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_09.keys = []
key_resp_09.rt = []
_key_resp_09_allKeys = []
# keep track of which components have finished
moreInstructComponents = [finalRemind, key_resp_09, instructContinue7]
for thisComponent in moreInstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
moreInstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "moreInstruct"-------
while continueRoutine:
    # get current time
    t = moreInstructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=moreInstructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finalRemind* updates
    if finalRemind.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finalRemind.frameNStart = frameN  # exact frame index
        finalRemind.tStart = t  # local t and not account for scr refresh
        finalRemind.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finalRemind, 'tStartRefresh')  # time at next scr refresh
        finalRemind.setAutoDraw(True)
    
    # *key_resp_09* updates
    waitOnFlip = False
    if key_resp_09.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_09.frameNStart = frameN  # exact frame index
        key_resp_09.tStart = t  # local t and not account for scr refresh
        key_resp_09.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_09, 'tStartRefresh')  # time at next scr refresh
        key_resp_09.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_09.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_09.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_09.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_09.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_09_allKeys.extend(theseKeys)
        if len(_key_resp_09_allKeys):
            key_resp_09.keys = _key_resp_09_allKeys[-1].name  # just the last key pressed
            key_resp_09.rt = _key_resp_09_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructContinue7* updates
    if instructContinue7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructContinue7.frameNStart = frameN  # exact frame index
        instructContinue7.tStart = t  # local t and not account for scr refresh
        instructContinue7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructContinue7, 'tStartRefresh')  # time at next scr refresh
        instructContinue7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in moreInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "moreInstruct"-------
for thisComponent in moreInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('finalRemind.started', finalRemind.tStartRefresh)
thisExp.addData('finalRemind.stopped', finalRemind.tStopRefresh)
# check responses
if key_resp_09.keys in ['', [], None]:  # No response was made
    key_resp_09.keys = None
thisExp.addData('key_resp_09.keys',key_resp_09.keys)
if key_resp_09.keys != None:  # we had a response
    thisExp.addData('key_resp_09.rt', key_resp_09.rt)
thisExp.addData('key_resp_09.started', key_resp_09.tStartRefresh)
thisExp.addData('key_resp_09.stopped', key_resp_09.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instructContinue7.started', instructContinue7.tStartRefresh)
thisExp.addData('instructContinue7.stopped', instructContinue7.tStopRefresh)
# the Routine "moreInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('resources/ldt_wordList.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixLdtTask"-------
    continueRoutine = True
    routineTimer.add(0.400000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixLdtTaskComponents = [fixLdtTaskCross]
    for thisComponent in fixLdtTaskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixLdtTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixLdtTask"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixLdtTaskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixLdtTaskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixLdtTaskCross* updates
        if fixLdtTaskCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixLdtTaskCross.frameNStart = frameN  # exact frame index
            fixLdtTaskCross.tStart = t  # local t and not account for scr refresh
            fixLdtTaskCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixLdtTaskCross, 'tStartRefresh')  # time at next scr refresh
            fixLdtTaskCross.setAutoDraw(True)
        if fixLdtTaskCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixLdtTaskCross.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                fixLdtTaskCross.tStop = t  # not accounting for scr refresh
                fixLdtTaskCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixLdtTaskCross, 'tStopRefresh')  # time at next scr refresh
                fixLdtTaskCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixLdtTaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixLdtTask"-------
    for thisComponent in fixLdtTaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('fixLdtTaskCross.started', fixLdtTaskCross.tStartRefresh)
    trials_3.addData('fixLdtTaskCross.stopped', fixLdtTaskCross.tStopRefresh)
    
    # ------Prepare to start Routine "ldtTask"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    ldtStimulus.setText(ldtStim)
    ldtResponse.keys = []
    ldtResponse.rt = []
    _ldtResponse_allKeys = []
    # keep track of which components have finished
    ldtTaskComponents = [ldtStimulus, ldtResponse, ldtResponseF, ldtResponseJ]
    for thisComponent in ldtTaskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ldtTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ldtTask"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ldtTaskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ldtTaskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ldtStimulus* updates
        if ldtStimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ldtStimulus.frameNStart = frameN  # exact frame index
            ldtStimulus.tStart = t  # local t and not account for scr refresh
            ldtStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ldtStimulus, 'tStartRefresh')  # time at next scr refresh
            ldtStimulus.setAutoDraw(True)
        if ldtStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ldtStimulus.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                ldtStimulus.tStop = t  # not accounting for scr refresh
                ldtStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ldtStimulus, 'tStopRefresh')  # time at next scr refresh
                ldtStimulus.setAutoDraw(False)
        
        # *ldtResponse* updates
        waitOnFlip = False
        if ldtResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ldtResponse.frameNStart = frameN  # exact frame index
            ldtResponse.tStart = t  # local t and not account for scr refresh
            ldtResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ldtResponse, 'tStartRefresh')  # time at next scr refresh
            ldtResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ldtResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ldtResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ldtResponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ldtResponse.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                ldtResponse.tStop = t  # not accounting for scr refresh
                ldtResponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ldtResponse, 'tStopRefresh')  # time at next scr refresh
                ldtResponse.status = FINISHED
        if ldtResponse.status == STARTED and not waitOnFlip:
            theseKeys = ldtResponse.getKeys(keyList=['f', 'j'], waitRelease=False)
            _ldtResponse_allKeys.extend(theseKeys)
            if len(_ldtResponse_allKeys):
                ldtResponse.keys = _ldtResponse_allKeys[-1].name  # just the last key pressed
                ldtResponse.rt = _ldtResponse_allKeys[-1].rt
                # was this correct?
                if (ldtResponse.keys == str('')) or (ldtResponse.keys == ''):
                    ldtResponse.corr = 1
                else:
                    ldtResponse.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *ldtResponseF* updates
        if ldtResponseF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ldtResponseF.frameNStart = frameN  # exact frame index
            ldtResponseF.tStart = t  # local t and not account for scr refresh
            ldtResponseF.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ldtResponseF, 'tStartRefresh')  # time at next scr refresh
            ldtResponseF.setAutoDraw(True)
        if ldtResponseF.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ldtResponseF.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                ldtResponseF.tStop = t  # not accounting for scr refresh
                ldtResponseF.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ldtResponseF, 'tStopRefresh')  # time at next scr refresh
                ldtResponseF.setAutoDraw(False)
        
        # *ldtResponseJ* updates
        if ldtResponseJ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ldtResponseJ.frameNStart = frameN  # exact frame index
            ldtResponseJ.tStart = t  # local t and not account for scr refresh
            ldtResponseJ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ldtResponseJ, 'tStartRefresh')  # time at next scr refresh
            ldtResponseJ.setAutoDraw(True)
        if ldtResponseJ.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ldtResponseJ.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                ldtResponseJ.tStop = t  # not accounting for scr refresh
                ldtResponseJ.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ldtResponseJ, 'tStopRefresh')  # time at next scr refresh
                ldtResponseJ.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ldtTaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ldtTask"-------
    for thisComponent in ldtTaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('ldtStimulus.started', ldtStimulus.tStartRefresh)
    trials_3.addData('ldtStimulus.stopped', ldtStimulus.tStopRefresh)
    # check responses
    if ldtResponse.keys in ['', [], None]:  # No response was made
        ldtResponse.keys = None
        # was no response the correct answer?!
        if str('').lower() == 'none':
           ldtResponse.corr = 1;  # correct non-response
        else:
           ldtResponse.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('ldtResponse.keys',ldtResponse.keys)
    trials_3.addData('ldtResponse.corr', ldtResponse.corr)
    if ldtResponse.keys != None:  # we had a response
        trials_3.addData('ldtResponse.rt', ldtResponse.rt)
    trials_3.addData('ldtResponse.started', ldtResponse.tStartRefresh)
    trials_3.addData('ldtResponse.stopped', ldtResponse.tStopRefresh)
    trials_3.addData('ldtResponseF.started', ldtResponseF.tStartRefresh)
    trials_3.addData('ldtResponseF.stopped', ldtResponseF.tStopRefresh)
    trials_3.addData('ldtResponseJ.started', ldtResponseJ.tStartRefresh)
    trials_3.addData('ldtResponseJ.stopped', ldtResponseJ.tStopRefresh)
    
    # ------Prepare to start Routine "interTrial"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    interTrialComponents = [blank_interTrial]
    for thisComponent in interTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    interTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "interTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = interTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=interTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_interTrial* updates
        if blank_interTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_interTrial.frameNStart = frameN  # exact frame index
            blank_interTrial.tStart = t  # local t and not account for scr refresh
            blank_interTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_interTrial, 'tStartRefresh')  # time at next scr refresh
            blank_interTrial.setAutoDraw(True)
        if blank_interTrial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_interTrial.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                blank_interTrial.tStop = t  # not accounting for scr refresh
                blank_interTrial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_interTrial, 'tStopRefresh')  # time at next scr refresh
                blank_interTrial.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in interTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "interTrial"-------
    for thisComponent in interTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('blank_interTrial.started', blank_interTrial.tStartRefresh)
    trials_3.addData('blank_interTrial.stopped', blank_interTrial.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# ------Prepare to start Routine "ldtComplete"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_25.keys = []
key_resp_25.rt = []
_key_resp_25_allKeys = []
# keep track of which components have finished
ldtCompleteComponents = [ldtCompleteintroDCCS, key_resp_25, instructContinue8]
for thisComponent in ldtCompleteComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ldtCompleteClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ldtComplete"-------
while continueRoutine:
    # get current time
    t = ldtCompleteClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ldtCompleteClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ldtCompleteintroDCCS* updates
    if ldtCompleteintroDCCS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ldtCompleteintroDCCS.frameNStart = frameN  # exact frame index
        ldtCompleteintroDCCS.tStart = t  # local t and not account for scr refresh
        ldtCompleteintroDCCS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ldtCompleteintroDCCS, 'tStartRefresh')  # time at next scr refresh
        ldtCompleteintroDCCS.setAutoDraw(True)
    
    # *key_resp_25* updates
    waitOnFlip = False
    if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_25.frameNStart = frameN  # exact frame index
        key_resp_25.tStart = t  # local t and not account for scr refresh
        key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
        key_resp_25.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_25.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_25.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_25_allKeys.extend(theseKeys)
        if len(_key_resp_25_allKeys):
            key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
            key_resp_25.rt = _key_resp_25_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructContinue8* updates
    if instructContinue8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructContinue8.frameNStart = frameN  # exact frame index
        instructContinue8.tStart = t  # local t and not account for scr refresh
        instructContinue8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructContinue8, 'tStartRefresh')  # time at next scr refresh
        instructContinue8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ldtCompleteComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ldtComplete"-------
for thisComponent in ldtCompleteComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ldtCompleteintroDCCS.started', ldtCompleteintroDCCS.tStartRefresh)
thisExp.addData('ldtCompleteintroDCCS.stopped', ldtCompleteintroDCCS.tStopRefresh)
# check responses
if key_resp_25.keys in ['', [], None]:  # No response was made
    key_resp_25.keys = None
thisExp.addData('key_resp_25.keys',key_resp_25.keys)
if key_resp_25.keys != None:  # we had a response
    thisExp.addData('key_resp_25.rt', key_resp_25.rt)
thisExp.addData('key_resp_25.started', key_resp_25.tStartRefresh)
thisExp.addData('key_resp_25.stopped', key_resp_25.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instructContinue8.started', instructContinue8.tStartRefresh)
thisExp.addData('instructContinue8.stopped', instructContinue8.tStopRefresh)
# the Routine "ldtComplete" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introDCCSPractice"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
introDCCSPracticeComponents = [headerDCCS, welcomeDCCS, key_resp_3]
for thisComponent in introDCCSPracticeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introDCCSPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introDCCSPractice"-------
while continueRoutine:
    # get current time
    t = introDCCSPracticeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introDCCSPracticeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *headerDCCS* updates
    if headerDCCS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        headerDCCS.frameNStart = frameN  # exact frame index
        headerDCCS.tStart = t  # local t and not account for scr refresh
        headerDCCS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(headerDCCS, 'tStartRefresh')  # time at next scr refresh
        headerDCCS.setAutoDraw(True)
    
    # *welcomeDCCS* updates
    if welcomeDCCS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeDCCS.frameNStart = frameN  # exact frame index
        welcomeDCCS.tStart = t  # local t and not account for scr refresh
        welcomeDCCS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeDCCS, 'tStartRefresh')  # time at next scr refresh
        welcomeDCCS.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['f', 'j'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introDCCSPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introDCCSPractice"-------
for thisComponent in introDCCSPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('headerDCCS.started', headerDCCS.tStartRefresh)
thisExp.addData('headerDCCS.stopped', headerDCCS.tStopRefresh)
thisExp.addData('welcomeDCCS.started', welcomeDCCS.tStartRefresh)
thisExp.addData('welcomeDCCS.stopped', welcomeDCCS.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "introDCCSPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "shapeBoatEx"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
shapeBoatExComponents = [textBoat, image_1, image_2, image_3, image_4, image_5, image_6, key_resp_10, text_2]
for thisComponent in shapeBoatExComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
shapeBoatExClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "shapeBoatEx"-------
while continueRoutine:
    # get current time
    t = shapeBoatExClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=shapeBoatExClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBoat* updates
    if textBoat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBoat.frameNStart = frameN  # exact frame index
        textBoat.tStart = t  # local t and not account for scr refresh
        textBoat.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBoat, 'tStartRefresh')  # time at next scr refresh
        textBoat.setAutoDraw(True)
    
    # *image_1* updates
    if image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_1.frameNStart = frameN  # exact frame index
        image_1.tStart = t  # local t and not account for scr refresh
        image_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_1, 'tStartRefresh')  # time at next scr refresh
        image_1.setAutoDraw(True)
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    if image_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_3.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            image_3.tStop = t  # not accounting for scr refresh
            image_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
            image_3.setAutoDraw(False)
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    if image_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_4.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_4.tStop = t  # not accounting for scr refresh
            image_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
            image_4.setAutoDraw(False)
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    if image_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_5.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_5.tStop = t  # not accounting for scr refresh
            image_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
            image_5.setAutoDraw(False)
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['j'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in shapeBoatExComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "shapeBoatEx"-------
for thisComponent in shapeBoatExComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textBoat.started', textBoat.tStartRefresh)
thisExp.addData('textBoat.stopped', textBoat.tStopRefresh)
thisExp.addData('image_1.started', image_1.tStartRefresh)
thisExp.addData('image_1.stopped', image_1.tStopRefresh)
thisExp.addData('image_2.started', image_2.tStartRefresh)
thisExp.addData('image_2.stopped', image_2.tStopRefresh)
thisExp.addData('image_3.started', image_3.tStartRefresh)
thisExp.addData('image_3.stopped', image_3.tStopRefresh)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)
thisExp.addData('image_5.started', image_5.tStartRefresh)
thisExp.addData('image_5.stopped', image_5.tStopRefresh)
thisExp.addData('image_6.started', image_6.tStartRefresh)
thisExp.addData('image_6.stopped', image_6.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "shapeBoatEx" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "shapeRabbitEx"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
shapeRabbitExComponents = [textRabbit, image_7, image_8, image_9, image_10, image_11, image_12, key_resp_11, text_11]
for thisComponent in shapeRabbitExComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
shapeRabbitExClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "shapeRabbitEx"-------
while continueRoutine:
    # get current time
    t = shapeRabbitExClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=shapeRabbitExClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textRabbit* updates
    if textRabbit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textRabbit.frameNStart = frameN  # exact frame index
        textRabbit.tStart = t  # local t and not account for scr refresh
        textRabbit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textRabbit, 'tStartRefresh')  # time at next scr refresh
        textRabbit.setAutoDraw(True)
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        image_7.setAutoDraw(True)
    
    # *image_8* updates
    if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_8.frameNStart = frameN  # exact frame index
        image_8.tStart = t  # local t and not account for scr refresh
        image_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
        image_8.setAutoDraw(True)
    
    # *image_9* updates
    if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_9.frameNStart = frameN  # exact frame index
        image_9.tStart = t  # local t and not account for scr refresh
        image_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
        image_9.setAutoDraw(True)
    if image_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_9.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            image_9.tStop = t  # not accounting for scr refresh
            image_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_9, 'tStopRefresh')  # time at next scr refresh
            image_9.setAutoDraw(False)
    
    # *image_10* updates
    if image_10.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        image_10.frameNStart = frameN  # exact frame index
        image_10.tStart = t  # local t and not account for scr refresh
        image_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
        image_10.setAutoDraw(True)
    if image_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_10.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_10.tStop = t  # not accounting for scr refresh
            image_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_10, 'tStopRefresh')  # time at next scr refresh
            image_10.setAutoDraw(False)
    
    # *image_11* updates
    if image_11.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        image_11.frameNStart = frameN  # exact frame index
        image_11.tStart = t  # local t and not account for scr refresh
        image_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
        image_11.setAutoDraw(True)
    if image_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_11.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_11.tStop = t  # not accounting for scr refresh
            image_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_11, 'tStopRefresh')  # time at next scr refresh
            image_11.setAutoDraw(False)
    
    # *image_12* updates
    if image_12.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
        # keep track of start time/frame for later
        image_12.frameNStart = frameN  # exact frame index
        image_12.tStart = t  # local t and not account for scr refresh
        image_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
        image_12.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['f'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in shapeRabbitExComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "shapeRabbitEx"-------
for thisComponent in shapeRabbitExComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textRabbit.started', textRabbit.tStartRefresh)
thisExp.addData('textRabbit.stopped', textRabbit.tStopRefresh)
thisExp.addData('image_7.started', image_7.tStartRefresh)
thisExp.addData('image_7.stopped', image_7.tStopRefresh)
thisExp.addData('image_8.started', image_8.tStartRefresh)
thisExp.addData('image_8.stopped', image_8.tStopRefresh)
thisExp.addData('image_9.started', image_9.tStartRefresh)
thisExp.addData('image_9.stopped', image_9.tStopRefresh)
thisExp.addData('image_10.started', image_10.tStartRefresh)
thisExp.addData('image_10.stopped', image_10.tStopRefresh)
thisExp.addData('image_11.started', image_11.tStartRefresh)
thisExp.addData('image_11.stopped', image_11.tStopRefresh)
thisExp.addData('image_12.started', image_12.tStartRefresh)
thisExp.addData('image_12.stopped', image_12.tStopRefresh)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
# the Routine "shapeRabbitEx" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructShape"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_12.keys = []
    key_resp_12.rt = []
    _key_resp_12_allKeys = []
    # keep track of which components have finished
    instructShapeComponents = [text_12, text_13, star_1, text_14, text_15, text_16, key_resp_12]
    for thisComponent in instructShapeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructShapeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructShape"-------
    while continueRoutine:
        # get current time
        t = instructShapeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructShapeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_12* updates
        if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            text_12.setAutoDraw(True)
        
        # *text_13* updates
        if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            text_13.setAutoDraw(True)
        
        # *star_1* updates
        if star_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            star_1.frameNStart = frameN  # exact frame index
            star_1.tStart = t  # local t and not account for scr refresh
            star_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(star_1, 'tStartRefresh')  # time at next scr refresh
            star_1.setAutoDraw(True)
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        
        # *text_15* updates
        if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_15.frameNStart = frameN  # exact frame index
            text_15.tStart = t  # local t and not account for scr refresh
            text_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
            text_15.setAutoDraw(True)
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        
        # *key_resp_12* updates
        waitOnFlip = False
        if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_12.frameNStart = frameN  # exact frame index
            key_resp_12.tStart = t  # local t and not account for scr refresh
            key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
            key_resp_12.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_12.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_12.getKeys(keyList=['f', 'j'], waitRelease=False)
            _key_resp_12_allKeys.extend(theseKeys)
            if len(_key_resp_12_allKeys):
                key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructShapeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructShape"-------
    for thisComponent in instructShapeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('text_12.started', text_12.tStartRefresh)
    block.addData('text_12.stopped', text_12.tStopRefresh)
    block.addData('text_13.started', text_13.tStartRefresh)
    block.addData('text_13.stopped', text_13.tStopRefresh)
    block.addData('star_1.started', star_1.tStartRefresh)
    block.addData('star_1.stopped', star_1.tStopRefresh)
    block.addData('text_14.started', text_14.tStartRefresh)
    block.addData('text_14.stopped', text_14.tStopRefresh)
    block.addData('text_15.started', text_15.tStartRefresh)
    block.addData('text_15.stopped', text_15.tStopRefresh)
    block.addData('text_16.started', text_16.tStartRefresh)
    block.addData('text_16.stopped', text_16.tStopRefresh)
    # check responses
    if key_resp_12.keys in ['', [], None]:  # No response was made
        key_resp_12.keys = None
    block.addData('key_resp_12.keys',key_resp_12.keys)
    if key_resp_12.keys != None:  # we had a response
        block.addData('key_resp_12.rt', key_resp_12.rt)
    block.addData('key_resp_12.started', key_resp_12.tStartRefresh)
    block.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
    # the Routine "instructShape" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('resources/ShapePractTrial.csv'),
        seed=None, name='trials_4')
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    for thisTrial_4 in trials_4:
        currentLoop = trials_4
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "interTrialShape"-------
        continueRoutine = True
        routineTimer.add(0.800000)
        # update component parameters for each repeat
        # keep track of which components have finished
        interTrialShapeComponents = [leftImageWait, rightImageWait]
        for thisComponent in interTrialShapeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        interTrialShapeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "interTrialShape"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = interTrialShapeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=interTrialShapeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *leftImageWait* updates
            if leftImageWait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageWait.frameNStart = frameN  # exact frame index
                leftImageWait.tStart = t  # local t and not account for scr refresh
                leftImageWait.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageWait, 'tStartRefresh')  # time at next scr refresh
                leftImageWait.setAutoDraw(True)
            if leftImageWait.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageWait.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageWait.tStop = t  # not accounting for scr refresh
                    leftImageWait.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageWait, 'tStopRefresh')  # time at next scr refresh
                    leftImageWait.setAutoDraw(False)
            
            # *rightImageWait* updates
            if rightImageWait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageWait.frameNStart = frameN  # exact frame index
                rightImageWait.tStart = t  # local t and not account for scr refresh
                rightImageWait.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageWait, 'tStartRefresh')  # time at next scr refresh
                rightImageWait.setAutoDraw(True)
            if rightImageWait.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageWait.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageWait.tStop = t  # not accounting for scr refresh
                    rightImageWait.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageWait, 'tStopRefresh')  # time at next scr refresh
                    rightImageWait.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in interTrialShapeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "interTrialShape"-------
        for thisComponent in interTrialShapeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_4.addData('leftImageWait.started', leftImageWait.tStartRefresh)
        trials_4.addData('leftImageWait.stopped', leftImageWait.tStopRefresh)
        trials_4.addData('rightImageWait.started', rightImageWait.tStartRefresh)
        trials_4.addData('rightImageWait.stopped', rightImageWait.tStopRefresh)
        
        # ------Prepare to start Routine "ISICodeShape"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ISICodeShapeComponents = []
        for thisComponent in ISICodeShapeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISICodeShapeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISICodeShape"-------
        while continueRoutine:
            # get current time
            t = ISICodeShapeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISICodeShapeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISICodeShapeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISICodeShape"-------
        for thisComponent in ISICodeShapeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # pick the ISI for the next routine
        # this code component is set to 'both' because we need to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(1000, 1500, 500)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # show in console for debugging
        print('thisISI: ', thisISI)
        
        # save this ISI to our output file
        trials_4.addData('ISI', thisISI)
        # the Routine "ISICodeShape" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fixationShape"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationShapeComponents = [star_2, leftImageFixation, rightImageFixation]
        for thisComponent in fixationShapeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationShapeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixationShape"-------
        while continueRoutine:
            # get current time
            t = fixationShapeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationShapeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *star_2* updates
            if star_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                star_2.frameNStart = frameN  # exact frame index
                star_2.tStart = t  # local t and not account for scr refresh
                star_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star_2, 'tStartRefresh')  # time at next scr refresh
                star_2.setAutoDraw(True)
            if star_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > star_2.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    star_2.tStop = t  # not accounting for scr refresh
                    star_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(star_2, 'tStopRefresh')  # time at next scr refresh
                    star_2.setAutoDraw(False)
            
            # *leftImageFixation* updates
            if leftImageFixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageFixation.frameNStart = frameN  # exact frame index
                leftImageFixation.tStart = t  # local t and not account for scr refresh
                leftImageFixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageFixation, 'tStartRefresh')  # time at next scr refresh
                leftImageFixation.setAutoDraw(True)
            if leftImageFixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageFixation.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageFixation.tStop = t  # not accounting for scr refresh
                    leftImageFixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageFixation, 'tStopRefresh')  # time at next scr refresh
                    leftImageFixation.setAutoDraw(False)
            
            # *rightImageFixation* updates
            if rightImageFixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageFixation.frameNStart = frameN  # exact frame index
                rightImageFixation.tStart = t  # local t and not account for scr refresh
                rightImageFixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageFixation, 'tStartRefresh')  # time at next scr refresh
                rightImageFixation.setAutoDraw(True)
            if rightImageFixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageFixation.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageFixation.tStop = t  # not accounting for scr refresh
                    rightImageFixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageFixation, 'tStopRefresh')  # time at next scr refresh
                    rightImageFixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationShapeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixationShape"-------
        for thisComponent in fixationShapeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_4.addData('star_2.started', star_2.tStartRefresh)
        trials_4.addData('star_2.stopped', star_2.tStopRefresh)
        trials_4.addData('leftImageFixation.started', leftImageFixation.tStartRefresh)
        trials_4.addData('leftImageFixation.stopped', leftImageFixation.tStopRefresh)
        trials_4.addData('rightImageFixation.started', rightImageFixation.tStartRefresh)
        trials_4.addData('rightImageFixation.stopped', rightImageFixation.tStopRefresh)
        # the Routine "fixationShape" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "cueShape"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        cueShapeComponents = [textCueShape, leftImageCue, rightImageCue]
        for thisComponent in cueShapeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cueShapeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "cueShape"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cueShapeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cueShapeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textCueShape* updates
            if textCueShape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textCueShape.frameNStart = frameN  # exact frame index
                textCueShape.tStart = t  # local t and not account for scr refresh
                textCueShape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textCueShape, 'tStartRefresh')  # time at next scr refresh
                textCueShape.setAutoDraw(True)
            if textCueShape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textCueShape.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textCueShape.tStop = t  # not accounting for scr refresh
                    textCueShape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textCueShape, 'tStopRefresh')  # time at next scr refresh
                    textCueShape.setAutoDraw(False)
            
            # *leftImageCue* updates
            if leftImageCue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageCue.frameNStart = frameN  # exact frame index
                leftImageCue.tStart = t  # local t and not account for scr refresh
                leftImageCue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageCue, 'tStartRefresh')  # time at next scr refresh
                leftImageCue.setAutoDraw(True)
            if leftImageCue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageCue.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageCue.tStop = t  # not accounting for scr refresh
                    leftImageCue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageCue, 'tStopRefresh')  # time at next scr refresh
                    leftImageCue.setAutoDraw(False)
            
            # *rightImageCue* updates
            if rightImageCue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageCue.frameNStart = frameN  # exact frame index
                rightImageCue.tStart = t  # local t and not account for scr refresh
                rightImageCue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageCue, 'tStartRefresh')  # time at next scr refresh
                rightImageCue.setAutoDraw(True)
            if rightImageCue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageCue.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageCue.tStop = t  # not accounting for scr refresh
                    rightImageCue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageCue, 'tStopRefresh')  # time at next scr refresh
                    rightImageCue.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cueShapeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cueShape"-------
        for thisComponent in cueShapeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_4.addData('textCueShape.started', textCueShape.tStartRefresh)
        trials_4.addData('textCueShape.stopped', textCueShape.tStopRefresh)
        trials_4.addData('leftImageCue.started', leftImageCue.tStartRefresh)
        trials_4.addData('leftImageCue.stopped', leftImageCue.tStopRefresh)
        trials_4.addData('rightImageCue.started', rightImageCue.tStartRefresh)
        trials_4.addData('rightImageCue.stopped', rightImageCue.tStopRefresh)
        
        # ------Prepare to start Routine "stimShape"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        stimImageShape.setImage(middle)
        leftImageShape.setImage(left)
        rightImageShape.setImage(right)
        key_resp_13.keys = []
        key_resp_13.rt = []
        _key_resp_13_allKeys = []
        # keep track of which components have finished
        stimShapeComponents = [stimImageShape, leftImageShape, rightImageShape, key_resp_13]
        for thisComponent in stimShapeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stimShapeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stimShape"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimShapeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stimShapeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimImageShape* updates
            if stimImageShape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimImageShape.frameNStart = frameN  # exact frame index
                stimImageShape.tStart = t  # local t and not account for scr refresh
                stimImageShape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimImageShape, 'tStartRefresh')  # time at next scr refresh
                stimImageShape.setAutoDraw(True)
            if stimImageShape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimImageShape.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    stimImageShape.tStop = t  # not accounting for scr refresh
                    stimImageShape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimImageShape, 'tStopRefresh')  # time at next scr refresh
                    stimImageShape.setAutoDraw(False)
            
            # *leftImageShape* updates
            if leftImageShape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageShape.frameNStart = frameN  # exact frame index
                leftImageShape.tStart = t  # local t and not account for scr refresh
                leftImageShape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageShape, 'tStartRefresh')  # time at next scr refresh
                leftImageShape.setAutoDraw(True)
            if leftImageShape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageShape.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageShape.tStop = t  # not accounting for scr refresh
                    leftImageShape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageShape, 'tStopRefresh')  # time at next scr refresh
                    leftImageShape.setAutoDraw(False)
            
            # *rightImageShape* updates
            if rightImageShape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageShape.frameNStart = frameN  # exact frame index
                rightImageShape.tStart = t  # local t and not account for scr refresh
                rightImageShape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageShape, 'tStartRefresh')  # time at next scr refresh
                rightImageShape.setAutoDraw(True)
            if rightImageShape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageShape.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageShape.tStop = t  # not accounting for scr refresh
                    rightImageShape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageShape, 'tStopRefresh')  # time at next scr refresh
                    rightImageShape.setAutoDraw(False)
            
            # *key_resp_13* updates
            waitOnFlip = False
            if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_13.frameNStart = frameN  # exact frame index
                key_resp_13.tStart = t  # local t and not account for scr refresh
                key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
                key_resp_13.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_13.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_13.tStop = t  # not accounting for scr refresh
                    key_resp_13.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_13, 'tStopRefresh')  # time at next scr refresh
                    key_resp_13.status = FINISHED
            if key_resp_13.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_13.getKeys(keyList=['f', 'j'], waitRelease=False)
                _key_resp_13_allKeys.extend(theseKeys)
                if len(_key_resp_13_allKeys):
                    key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                    key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_13.keys == str(corrAns)) or (key_resp_13.keys == corrAns):
                        key_resp_13.corr = 1
                    else:
                        key_resp_13.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimShapeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stimShape"-------
        for thisComponent in stimShapeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_4.addData('stimImageShape.started', stimImageShape.tStartRefresh)
        trials_4.addData('stimImageShape.stopped', stimImageShape.tStopRefresh)
        trials_4.addData('leftImageShape.started', leftImageShape.tStartRefresh)
        trials_4.addData('leftImageShape.stopped', leftImageShape.tStopRefresh)
        trials_4.addData('rightImageShape.started', rightImageShape.tStartRefresh)
        trials_4.addData('rightImageShape.stopped', rightImageShape.tStopRefresh)
        # check responses
        if key_resp_13.keys in ['', [], None]:  # No response was made
            key_resp_13.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_13.corr = 1;  # correct non-response
            else:
               key_resp_13.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_4 (TrialHandler)
        trials_4.addData('key_resp_13.keys',key_resp_13.keys)
        trials_4.addData('key_resp_13.corr', key_resp_13.corr)
        if key_resp_13.keys != None:  # we had a response
            trials_4.addData('key_resp_13.rt', key_resp_13.rt)
        trials_4.addData('key_resp_13.started', key_resp_13.tStartRefresh)
        trials_4.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
        
        # ------Prepare to start Routine "feedbackShape"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        if key_resp_13.keys: # if a keypress has been made
            if key_resp_13.keys[0] =='f':
                if key_resp_13.corr:
                    left = 'resources/dccs/RedRabbitRed.png'
                    right = 'resources/dccs/BlueBoatWhite.png'
                    msg = 'That is correct!'
        #            audio = 'resources/dccs/audio_thatsRight.mp3'
                else:
                    left = 'resources/dccs/RedRabbitWhite.png'
                    right = 'resources/dccs/BlueBoatRed.png'
                    msg = 'This is the same shape, so you should choose this box.'
        #            audio = 'resources/dccs/audio_error_shape_ft-dccs.mp3'
        
            elif key_resp_13.keys[0] =='j':
                if key_resp_13.corr:
                    right = 'resources/dccs/BlueBoatRed.png'
                    left = 'resources/dccs/RedRabbitWhite.png'
                    msg = 'That is correct!'
        #            audio = 'resources/dccs/audio_thatsRight.mp3'
                else:
                    left = 'resources/dccs/RedRabbitRed.png'
                    right = 'resources/dccs/BlueBoatWhite.png'
                    msg = 'This is the same shape, so you should choose this box.'
        #            audio = 'resources/dccs/audio_error_shape_ft-dccs.mp3'
        else: # this is classed as an incorrect response
            if corrAns == 'j':
                right = 'resources/dccs/BlueBoatRed.png'
                left = 'resources/dccs/RedRabbitWhite.png'
                msg = 'This is the same shape, so you should choose this box.'
        #        audio = 'resources/dccs/audio_error_shape_ft-dccs.mp3'
            else:
                left = 'resources/dccs/RedRabbitRed.png'
                right = 'resources/dccs/BlueBoatWhite.png'
                msg = 'This is the same shape, so you should choose this box.'
        #        audio = 'resources/dccs/audio_error_shape_ft-dccs.mp3'
        
        leftImageFeedback.setImage(left)
        middleImageFeedback.setImage(middle)
        rightImageFeedback.setImage(right)
        textFeedbackShape.setText(msg)
        # keep track of which components have finished
        feedbackShapeComponents = [leftImageFeedback, middleImageFeedback, rightImageFeedback, textFeedbackShape]
        for thisComponent in feedbackShapeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedbackShapeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedbackShape"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackShapeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackShapeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *leftImageFeedback* updates
            if leftImageFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageFeedback.frameNStart = frameN  # exact frame index
                leftImageFeedback.tStart = t  # local t and not account for scr refresh
                leftImageFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageFeedback, 'tStartRefresh')  # time at next scr refresh
                leftImageFeedback.setAutoDraw(True)
            if leftImageFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageFeedback.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageFeedback.tStop = t  # not accounting for scr refresh
                    leftImageFeedback.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageFeedback, 'tStopRefresh')  # time at next scr refresh
                    leftImageFeedback.setAutoDraw(False)
            
            # *middleImageFeedback* updates
            if middleImageFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                middleImageFeedback.frameNStart = frameN  # exact frame index
                middleImageFeedback.tStart = t  # local t and not account for scr refresh
                middleImageFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(middleImageFeedback, 'tStartRefresh')  # time at next scr refresh
                middleImageFeedback.setAutoDraw(True)
            if middleImageFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > middleImageFeedback.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    middleImageFeedback.tStop = t  # not accounting for scr refresh
                    middleImageFeedback.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(middleImageFeedback, 'tStopRefresh')  # time at next scr refresh
                    middleImageFeedback.setAutoDraw(False)
            
            # *rightImageFeedback* updates
            if rightImageFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageFeedback.frameNStart = frameN  # exact frame index
                rightImageFeedback.tStart = t  # local t and not account for scr refresh
                rightImageFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageFeedback, 'tStartRefresh')  # time at next scr refresh
                rightImageFeedback.setAutoDraw(True)
            if rightImageFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageFeedback.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageFeedback.tStop = t  # not accounting for scr refresh
                    rightImageFeedback.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageFeedback, 'tStopRefresh')  # time at next scr refresh
                    rightImageFeedback.setAutoDraw(False)
            
            # *textFeedbackShape* updates
            if textFeedbackShape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textFeedbackShape.frameNStart = frameN  # exact frame index
                textFeedbackShape.tStart = t  # local t and not account for scr refresh
                textFeedbackShape.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textFeedbackShape, 'tStartRefresh')  # time at next scr refresh
                textFeedbackShape.setAutoDraw(True)
            if textFeedbackShape.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textFeedbackShape.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textFeedbackShape.tStop = t  # not accounting for scr refresh
                    textFeedbackShape.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textFeedbackShape, 'tStopRefresh')  # time at next scr refresh
                    textFeedbackShape.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackShapeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedbackShape"-------
        for thisComponent in feedbackShapeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_4.addData('leftImageFeedback.started', leftImageFeedback.tStartRefresh)
        trials_4.addData('leftImageFeedback.stopped', leftImageFeedback.tStopRefresh)
        trials_4.addData('middleImageFeedback.started', middleImageFeedback.tStartRefresh)
        trials_4.addData('middleImageFeedback.stopped', middleImageFeedback.tStopRefresh)
        trials_4.addData('rightImageFeedback.started', rightImageFeedback.tStartRefresh)
        trials_4.addData('rightImageFeedback.stopped', rightImageFeedback.tStopRefresh)
        trials_4.addData('textFeedbackShape.started', textFeedbackShape.tStartRefresh)
        trials_4.addData('textFeedbackShape.stopped', textFeedbackShape.tStopRefresh)
        
        # ------Prepare to start Routine "clearShape"-------
        continueRoutine = True
        # update component parameters for each repeat
        if key_resp_13.keys:
            if key_resp_13.corr:
                counterOne +=1
            else:
                counterTwo +=1
        else:
            key_resp_13.corr = 0
            counterTwo +=1
        # keep track of which components have finished
        clearShapeComponents = []
        for thisComponent in clearShapeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        clearShapeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "clearShape"-------
        while continueRoutine:
            # get current time
            t = clearShapeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=clearShapeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in clearShapeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "clearShape"-------
        for thisComponent in clearShapeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "clearShape" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_4'
    
    
    # ------Prepare to start Routine "continueShape"-------
    continueRoutine = True
    # update component parameters for each repeat
    if counterOne >= 1:
        outPut = 'Lets move forward. Press the space key to continue.'
        block.finished = True
    if counterTwo>=1:
        outPut = 'Please try the practice again. Press the space key.'
        isForward += 1
        block.finished = False
        counterOne = 0
        counterTwo = 0
        if isForward == 3:
            outPut = 'Thank you for your participation!'
            block.finished = True
    textContinueStatus.setText(outPut)
    key_resp_14.keys = []
    key_resp_14.rt = []
    _key_resp_14_allKeys = []
    # keep track of which components have finished
    continueShapeComponents = [textContinueStatus, key_resp_14]
    for thisComponent in continueShapeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    continueShapeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "continueShape"-------
    while continueRoutine:
        # get current time
        t = continueShapeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=continueShapeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textContinueStatus* updates
        if textContinueStatus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textContinueStatus.frameNStart = frameN  # exact frame index
            textContinueStatus.tStart = t  # local t and not account for scr refresh
            textContinueStatus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textContinueStatus, 'tStartRefresh')  # time at next scr refresh
            textContinueStatus.setAutoDraw(True)
        
        # *key_resp_14* updates
        waitOnFlip = False
        if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.tStart = t  # local t and not account for scr refresh
            key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_14.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_14_allKeys.extend(theseKeys)
            if len(_key_resp_14_allKeys):
                key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in continueShapeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "continueShape"-------
    for thisComponent in continueShapeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('textContinueStatus.started', textContinueStatus.tStartRefresh)
    block.addData('textContinueStatus.stopped', textContinueStatus.tStopRefresh)
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
        key_resp_14.keys = None
    block.addData('key_resp_14.keys',key_resp_14.keys)
    if key_resp_14.keys != None:  # we had a response
        block.addData('key_resp_14.rt', key_resp_14.rt)
    block.addData('key_resp_14.started', key_resp_14.tStartRefresh)
    block.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
    # the Routine "continueShape" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'block'


# ------Prepare to start Routine "colorRedEx"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_15.keys = []
key_resp_15.rt = []
_key_resp_15_allKeys = []
# keep track of which components have finished
colorRedExComponents = [textRed, image_13, image_14, image_15, image_16, image_17, image_18, key_resp_15, text_18]
for thisComponent in colorRedExComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
colorRedExClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "colorRedEx"-------
while continueRoutine:
    # get current time
    t = colorRedExClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=colorRedExClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textRed* updates
    if textRed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textRed.frameNStart = frameN  # exact frame index
        textRed.tStart = t  # local t and not account for scr refresh
        textRed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textRed, 'tStartRefresh')  # time at next scr refresh
        textRed.setAutoDraw(True)
    
    # *image_13* updates
    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        image_13.setAutoDraw(True)
    
    # *image_14* updates
    if image_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_14.frameNStart = frameN  # exact frame index
        image_14.tStart = t  # local t and not account for scr refresh
        image_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
        image_14.setAutoDraw(True)
    
    # *image_15* updates
    if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_15.frameNStart = frameN  # exact frame index
        image_15.tStart = t  # local t and not account for scr refresh
        image_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
        image_15.setAutoDraw(True)
    if image_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_15.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            image_15.tStop = t  # not accounting for scr refresh
            image_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_15, 'tStopRefresh')  # time at next scr refresh
            image_15.setAutoDraw(False)
    
    # *image_16* updates
    if image_16.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        image_16.frameNStart = frameN  # exact frame index
        image_16.tStart = t  # local t and not account for scr refresh
        image_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
        image_16.setAutoDraw(True)
    if image_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_16.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_16.tStop = t  # not accounting for scr refresh
            image_16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_16, 'tStopRefresh')  # time at next scr refresh
            image_16.setAutoDraw(False)
    
    # *image_17* updates
    if image_17.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        image_17.frameNStart = frameN  # exact frame index
        image_17.tStart = t  # local t and not account for scr refresh
        image_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
        image_17.setAutoDraw(True)
    if image_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_17.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_17.tStop = t  # not accounting for scr refresh
            image_17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_17, 'tStopRefresh')  # time at next scr refresh
            image_17.setAutoDraw(False)
    
    # *image_18* updates
    if image_18.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
        # keep track of start time/frame for later
        image_18.frameNStart = frameN  # exact frame index
        image_18.tStart = t  # local t and not account for scr refresh
        image_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
        image_18.setAutoDraw(True)
    
    # *key_resp_15* updates
    waitOnFlip = False
    if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.tStart = t  # local t and not account for scr refresh
        key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_15.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_15.getKeys(keyList=['j'], waitRelease=False)
        _key_resp_15_allKeys.extend(theseKeys)
        if len(_key_resp_15_allKeys):
            key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
            key_resp_15.rt = _key_resp_15_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_18* updates
    if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in colorRedExComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "colorRedEx"-------
for thisComponent in colorRedExComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textRed.started', textRed.tStartRefresh)
thisExp.addData('textRed.stopped', textRed.tStopRefresh)
thisExp.addData('image_13.started', image_13.tStartRefresh)
thisExp.addData('image_13.stopped', image_13.tStopRefresh)
thisExp.addData('image_14.started', image_14.tStartRefresh)
thisExp.addData('image_14.stopped', image_14.tStopRefresh)
thisExp.addData('image_15.started', image_15.tStartRefresh)
thisExp.addData('image_15.stopped', image_15.tStopRefresh)
thisExp.addData('image_16.started', image_16.tStartRefresh)
thisExp.addData('image_16.stopped', image_16.tStopRefresh)
thisExp.addData('image_17.started', image_17.tStartRefresh)
thisExp.addData('image_17.stopped', image_17.tStopRefresh)
thisExp.addData('image_18.started', image_18.tStartRefresh)
thisExp.addData('image_18.stopped', image_18.tStopRefresh)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys = None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.addData('key_resp_15.started', key_resp_15.tStartRefresh)
thisExp.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_18.started', text_18.tStartRefresh)
thisExp.addData('text_18.stopped', text_18.tStopRefresh)
# the Routine "colorRedEx" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "colorBlueEx"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_16.keys = []
key_resp_16.rt = []
_key_resp_16_allKeys = []
# keep track of which components have finished
colorBlueExComponents = [textBlue, image_19, image_20, image_21, image_22, image_23, image_24, key_resp_16, text_19]
for thisComponent in colorBlueExComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
colorBlueExClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "colorBlueEx"-------
while continueRoutine:
    # get current time
    t = colorBlueExClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=colorBlueExClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlue* updates
    if textBlue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlue.frameNStart = frameN  # exact frame index
        textBlue.tStart = t  # local t and not account for scr refresh
        textBlue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlue, 'tStartRefresh')  # time at next scr refresh
        textBlue.setAutoDraw(True)
    
    # *image_19* updates
    if image_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_19.frameNStart = frameN  # exact frame index
        image_19.tStart = t  # local t and not account for scr refresh
        image_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
        image_19.setAutoDraw(True)
    
    # *image_20* updates
    if image_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_20.frameNStart = frameN  # exact frame index
        image_20.tStart = t  # local t and not account for scr refresh
        image_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_20, 'tStartRefresh')  # time at next scr refresh
        image_20.setAutoDraw(True)
    
    # *image_21* updates
    if image_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_21.frameNStart = frameN  # exact frame index
        image_21.tStart = t  # local t and not account for scr refresh
        image_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_21, 'tStartRefresh')  # time at next scr refresh
        image_21.setAutoDraw(True)
    if image_21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_21.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            image_21.tStop = t  # not accounting for scr refresh
            image_21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_21, 'tStopRefresh')  # time at next scr refresh
            image_21.setAutoDraw(False)
    
    # *image_22* updates
    if image_22.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        image_22.frameNStart = frameN  # exact frame index
        image_22.tStart = t  # local t and not account for scr refresh
        image_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_22, 'tStartRefresh')  # time at next scr refresh
        image_22.setAutoDraw(True)
    if image_22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_22.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_22.tStop = t  # not accounting for scr refresh
            image_22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_22, 'tStopRefresh')  # time at next scr refresh
            image_22.setAutoDraw(False)
    
    # *image_23* updates
    if image_23.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        image_23.frameNStart = frameN  # exact frame index
        image_23.tStart = t  # local t and not account for scr refresh
        image_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
        image_23.setAutoDraw(True)
    if image_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_23.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_23.tStop = t  # not accounting for scr refresh
            image_23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_23, 'tStopRefresh')  # time at next scr refresh
            image_23.setAutoDraw(False)
    
    # *image_24* updates
    if image_24.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
        # keep track of start time/frame for later
        image_24.frameNStart = frameN  # exact frame index
        image_24.tStart = t  # local t and not account for scr refresh
        image_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_24, 'tStartRefresh')  # time at next scr refresh
        image_24.setAutoDraw(True)
    
    # *key_resp_16* updates
    waitOnFlip = False
    if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_16.frameNStart = frameN  # exact frame index
        key_resp_16.tStart = t  # local t and not account for scr refresh
        key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
        key_resp_16.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_16.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_16.getKeys(keyList=['f'], waitRelease=False)
        _key_resp_16_allKeys.extend(theseKeys)
        if len(_key_resp_16_allKeys):
            key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
            key_resp_16.rt = _key_resp_16_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_19* updates
    if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_19.frameNStart = frameN  # exact frame index
        text_19.tStart = t  # local t and not account for scr refresh
        text_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
        text_19.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in colorBlueExComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "colorBlueEx"-------
for thisComponent in colorBlueExComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textBlue.started', textBlue.tStartRefresh)
thisExp.addData('textBlue.stopped', textBlue.tStopRefresh)
thisExp.addData('image_19.started', image_19.tStartRefresh)
thisExp.addData('image_19.stopped', image_19.tStopRefresh)
thisExp.addData('image_20.started', image_20.tStartRefresh)
thisExp.addData('image_20.stopped', image_20.tStopRefresh)
thisExp.addData('image_21.started', image_21.tStartRefresh)
thisExp.addData('image_21.stopped', image_21.tStopRefresh)
thisExp.addData('image_22.started', image_22.tStartRefresh)
thisExp.addData('image_22.stopped', image_22.tStopRefresh)
thisExp.addData('image_23.started', image_23.tStartRefresh)
thisExp.addData('image_23.stopped', image_23.tStopRefresh)
thisExp.addData('image_24.started', image_24.tStartRefresh)
thisExp.addData('image_24.stopped', image_24.tStopRefresh)
# check responses
if key_resp_16.keys in ['', [], None]:  # No response was made
    key_resp_16.keys = None
thisExp.addData('key_resp_16.keys',key_resp_16.keys)
if key_resp_16.keys != None:  # we had a response
    thisExp.addData('key_resp_16.rt', key_resp_16.rt)
thisExp.addData('key_resp_16.started', key_resp_16.tStartRefresh)
thisExp.addData('key_resp_16.stopped', key_resp_16.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_19.started', text_19.tStartRefresh)
thisExp.addData('text_19.stopped', text_19.tStopRefresh)
# the Routine "colorBlueEx" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block_2 = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block_2')
thisExp.addLoop(block_2)  # add the loop to the experiment
thisBlock_2 = block_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_2.rgb)
if thisBlock_2 != None:
    for paramName in thisBlock_2:
        exec('{} = thisBlock_2[paramName]'.format(paramName))

for thisBlock_2 in block_2:
    currentLoop = block_2
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_2.rgb)
    if thisBlock_2 != None:
        for paramName in thisBlock_2:
            exec('{} = thisBlock_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructColor"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_17.keys = []
    key_resp_17.rt = []
    _key_resp_17_allKeys = []
    # keep track of which components have finished
    instructColorComponents = [text_20, text_21, star_3, text_22, text_23, text_24, key_resp_17]
    for thisComponent in instructColorComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructColorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructColor"-------
    while continueRoutine:
        # get current time
        t = instructColorClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructColorClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_20* updates
        if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_20.frameNStart = frameN  # exact frame index
            text_20.tStart = t  # local t and not account for scr refresh
            text_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
            text_20.setAutoDraw(True)
        
        # *text_21* updates
        if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_21.frameNStart = frameN  # exact frame index
            text_21.tStart = t  # local t and not account for scr refresh
            text_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
            text_21.setAutoDraw(True)
        
        # *star_3* updates
        if star_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            star_3.frameNStart = frameN  # exact frame index
            star_3.tStart = t  # local t and not account for scr refresh
            star_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(star_3, 'tStartRefresh')  # time at next scr refresh
            star_3.setAutoDraw(True)
        
        # *text_22* updates
        if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_22.frameNStart = frameN  # exact frame index
            text_22.tStart = t  # local t and not account for scr refresh
            text_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
            text_22.setAutoDraw(True)
        
        # *text_23* updates
        if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            text_23.setAutoDraw(True)
        
        # *text_24* updates
        if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_24.frameNStart = frameN  # exact frame index
            text_24.tStart = t  # local t and not account for scr refresh
            text_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
            text_24.setAutoDraw(True)
        
        # *key_resp_17* updates
        waitOnFlip = False
        if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_17.frameNStart = frameN  # exact frame index
            key_resp_17.tStart = t  # local t and not account for scr refresh
            key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
            key_resp_17.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_17.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_17.getKeys(keyList=['f', 'j'], waitRelease=False)
            _key_resp_17_allKeys.extend(theseKeys)
            if len(_key_resp_17_allKeys):
                key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
                key_resp_17.rt = _key_resp_17_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructColorComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructColor"-------
    for thisComponent in instructColorComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_2.addData('text_20.started', text_20.tStartRefresh)
    block_2.addData('text_20.stopped', text_20.tStopRefresh)
    block_2.addData('text_21.started', text_21.tStartRefresh)
    block_2.addData('text_21.stopped', text_21.tStopRefresh)
    block_2.addData('star_3.started', star_3.tStartRefresh)
    block_2.addData('star_3.stopped', star_3.tStopRefresh)
    block_2.addData('text_22.started', text_22.tStartRefresh)
    block_2.addData('text_22.stopped', text_22.tStopRefresh)
    block_2.addData('text_23.started', text_23.tStartRefresh)
    block_2.addData('text_23.stopped', text_23.tStopRefresh)
    block_2.addData('text_24.started', text_24.tStartRefresh)
    block_2.addData('text_24.stopped', text_24.tStopRefresh)
    # check responses
    if key_resp_17.keys in ['', [], None]:  # No response was made
        key_resp_17.keys = None
    block_2.addData('key_resp_17.keys',key_resp_17.keys)
    if key_resp_17.keys != None:  # we had a response
        block_2.addData('key_resp_17.rt', key_resp_17.rt)
    block_2.addData('key_resp_17.started', key_resp_17.tStartRefresh)
    block_2.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
    # the Routine "instructColor" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_5 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('resources/colorPract.csv'),
        seed=None, name='trials_5')
    thisExp.addLoop(trials_5)  # add the loop to the experiment
    thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    for thisTrial_5 in trials_5:
        currentLoop = trials_5
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                exec('{} = thisTrial_5[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "interTrialColor"-------
        continueRoutine = True
        routineTimer.add(0.800000)
        # update component parameters for each repeat
        # keep track of which components have finished
        interTrialColorComponents = [leftImageWait2, rightImageWait2]
        for thisComponent in interTrialColorComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        interTrialColorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "interTrialColor"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = interTrialColorClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=interTrialColorClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *leftImageWait2* updates
            if leftImageWait2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageWait2.frameNStart = frameN  # exact frame index
                leftImageWait2.tStart = t  # local t and not account for scr refresh
                leftImageWait2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageWait2, 'tStartRefresh')  # time at next scr refresh
                leftImageWait2.setAutoDraw(True)
            if leftImageWait2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageWait2.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageWait2.tStop = t  # not accounting for scr refresh
                    leftImageWait2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageWait2, 'tStopRefresh')  # time at next scr refresh
                    leftImageWait2.setAutoDraw(False)
            
            # *rightImageWait2* updates
            if rightImageWait2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageWait2.frameNStart = frameN  # exact frame index
                rightImageWait2.tStart = t  # local t and not account for scr refresh
                rightImageWait2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageWait2, 'tStartRefresh')  # time at next scr refresh
                rightImageWait2.setAutoDraw(True)
            if rightImageWait2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageWait2.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageWait2.tStop = t  # not accounting for scr refresh
                    rightImageWait2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageWait2, 'tStopRefresh')  # time at next scr refresh
                    rightImageWait2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in interTrialColorComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "interTrialColor"-------
        for thisComponent in interTrialColorComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_5.addData('leftImageWait2.started', leftImageWait2.tStartRefresh)
        trials_5.addData('leftImageWait2.stopped', leftImageWait2.tStopRefresh)
        trials_5.addData('rightImageWait2.started', rightImageWait2.tStartRefresh)
        trials_5.addData('rightImageWait2.stopped', rightImageWait2.tStopRefresh)
        
        # ------Prepare to start Routine "ISICodeColor"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ISICodeColorComponents = []
        for thisComponent in ISICodeColorComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISICodeColorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISICodeColor"-------
        while continueRoutine:
            # get current time
            t = ISICodeColorClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISICodeColorClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISICodeColorComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISICodeColor"-------
        for thisComponent in ISICodeColorComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # pick the ISI for the next routine
        # this code component is set to 'both' because we need to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(1000, 1500, 500)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # show in console for debugging
        print('thisISI: ', thisISI)
        
        # save this ISI to our output file
        trials_4.addData('ISI', thisISI)
        # the Routine "ISICodeColor" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fixationColor"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationColorComponents = [star_4, leftImageFixation2, rightImageFixation2]
        for thisComponent in fixationColorComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationColorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixationColor"-------
        while continueRoutine:
            # get current time
            t = fixationColorClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationColorClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *star_4* updates
            if star_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                star_4.frameNStart = frameN  # exact frame index
                star_4.tStart = t  # local t and not account for scr refresh
                star_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star_4, 'tStartRefresh')  # time at next scr refresh
                star_4.setAutoDraw(True)
            if star_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > star_4.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    star_4.tStop = t  # not accounting for scr refresh
                    star_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(star_4, 'tStopRefresh')  # time at next scr refresh
                    star_4.setAutoDraw(False)
            
            # *leftImageFixation2* updates
            if leftImageFixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageFixation2.frameNStart = frameN  # exact frame index
                leftImageFixation2.tStart = t  # local t and not account for scr refresh
                leftImageFixation2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageFixation2, 'tStartRefresh')  # time at next scr refresh
                leftImageFixation2.setAutoDraw(True)
            if leftImageFixation2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageFixation2.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageFixation2.tStop = t  # not accounting for scr refresh
                    leftImageFixation2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageFixation2, 'tStopRefresh')  # time at next scr refresh
                    leftImageFixation2.setAutoDraw(False)
            
            # *rightImageFixation2* updates
            if rightImageFixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageFixation2.frameNStart = frameN  # exact frame index
                rightImageFixation2.tStart = t  # local t and not account for scr refresh
                rightImageFixation2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageFixation2, 'tStartRefresh')  # time at next scr refresh
                rightImageFixation2.setAutoDraw(True)
            if rightImageFixation2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageFixation2.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageFixation2.tStop = t  # not accounting for scr refresh
                    rightImageFixation2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageFixation2, 'tStopRefresh')  # time at next scr refresh
                    rightImageFixation2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationColorComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixationColor"-------
        for thisComponent in fixationColorComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_5.addData('star_4.started', star_4.tStartRefresh)
        trials_5.addData('star_4.stopped', star_4.tStopRefresh)
        trials_5.addData('leftImageFixation2.started', leftImageFixation2.tStartRefresh)
        trials_5.addData('leftImageFixation2.stopped', leftImageFixation2.tStopRefresh)
        trials_5.addData('rightImageFixation2.started', rightImageFixation2.tStartRefresh)
        trials_5.addData('rightImageFixation2.stopped', rightImageFixation2.tStopRefresh)
        # the Routine "fixationColor" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "cueColor"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        cueColorComponents = [textCueColor, leftImageCue2, rightImageCue2]
        for thisComponent in cueColorComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cueColorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "cueColor"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cueColorClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cueColorClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textCueColor* updates
            if textCueColor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textCueColor.frameNStart = frameN  # exact frame index
                textCueColor.tStart = t  # local t and not account for scr refresh
                textCueColor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textCueColor, 'tStartRefresh')  # time at next scr refresh
                textCueColor.setAutoDraw(True)
            if textCueColor.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textCueColor.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textCueColor.tStop = t  # not accounting for scr refresh
                    textCueColor.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textCueColor, 'tStopRefresh')  # time at next scr refresh
                    textCueColor.setAutoDraw(False)
            
            # *leftImageCue2* updates
            if leftImageCue2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageCue2.frameNStart = frameN  # exact frame index
                leftImageCue2.tStart = t  # local t and not account for scr refresh
                leftImageCue2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageCue2, 'tStartRefresh')  # time at next scr refresh
                leftImageCue2.setAutoDraw(True)
            if leftImageCue2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageCue2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageCue2.tStop = t  # not accounting for scr refresh
                    leftImageCue2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageCue2, 'tStopRefresh')  # time at next scr refresh
                    leftImageCue2.setAutoDraw(False)
            
            # *rightImageCue2* updates
            if rightImageCue2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageCue2.frameNStart = frameN  # exact frame index
                rightImageCue2.tStart = t  # local t and not account for scr refresh
                rightImageCue2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageCue2, 'tStartRefresh')  # time at next scr refresh
                rightImageCue2.setAutoDraw(True)
            if rightImageCue2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageCue2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageCue2.tStop = t  # not accounting for scr refresh
                    rightImageCue2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageCue2, 'tStopRefresh')  # time at next scr refresh
                    rightImageCue2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cueColorComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cueColor"-------
        for thisComponent in cueColorComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_5.addData('textCueColor.started', textCueColor.tStartRefresh)
        trials_5.addData('textCueColor.stopped', textCueColor.tStopRefresh)
        trials_5.addData('leftImageCue2.started', leftImageCue2.tStartRefresh)
        trials_5.addData('leftImageCue2.stopped', leftImageCue2.tStopRefresh)
        trials_5.addData('rightImageCue2.started', rightImageCue2.tStartRefresh)
        trials_5.addData('rightImageCue2.stopped', rightImageCue2.tStopRefresh)
        
        # ------Prepare to start Routine "stimColor"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        stimImageColor.setImage(middle)
        leftImageColor.setImage(left)
        rightImageColor.setImage(right)
        key_resp_18.keys = []
        key_resp_18.rt = []
        _key_resp_18_allKeys = []
        # keep track of which components have finished
        stimColorComponents = [stimImageColor, leftImageColor, rightImageColor, key_resp_18]
        for thisComponent in stimColorComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stimColorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stimColor"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimColorClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stimColorClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimImageColor* updates
            if stimImageColor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimImageColor.frameNStart = frameN  # exact frame index
                stimImageColor.tStart = t  # local t and not account for scr refresh
                stimImageColor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimImageColor, 'tStartRefresh')  # time at next scr refresh
                stimImageColor.setAutoDraw(True)
            if stimImageColor.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimImageColor.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    stimImageColor.tStop = t  # not accounting for scr refresh
                    stimImageColor.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimImageColor, 'tStopRefresh')  # time at next scr refresh
                    stimImageColor.setAutoDraw(False)
            
            # *leftImageColor* updates
            if leftImageColor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageColor.frameNStart = frameN  # exact frame index
                leftImageColor.tStart = t  # local t and not account for scr refresh
                leftImageColor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageColor, 'tStartRefresh')  # time at next scr refresh
                leftImageColor.setAutoDraw(True)
            if leftImageColor.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageColor.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageColor.tStop = t  # not accounting for scr refresh
                    leftImageColor.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageColor, 'tStopRefresh')  # time at next scr refresh
                    leftImageColor.setAutoDraw(False)
            
            # *rightImageColor* updates
            if rightImageColor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageColor.frameNStart = frameN  # exact frame index
                rightImageColor.tStart = t  # local t and not account for scr refresh
                rightImageColor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageColor, 'tStartRefresh')  # time at next scr refresh
                rightImageColor.setAutoDraw(True)
            if rightImageColor.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageColor.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageColor.tStop = t  # not accounting for scr refresh
                    rightImageColor.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageColor, 'tStopRefresh')  # time at next scr refresh
                    rightImageColor.setAutoDraw(False)
            
            # *key_resp_18* updates
            waitOnFlip = False
            if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_18.frameNStart = frameN  # exact frame index
                key_resp_18.tStart = t  # local t and not account for scr refresh
                key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
                key_resp_18.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_18.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_18.tStop = t  # not accounting for scr refresh
                    key_resp_18.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_18, 'tStopRefresh')  # time at next scr refresh
                    key_resp_18.status = FINISHED
            if key_resp_18.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_18.getKeys(keyList=['f', 'j'], waitRelease=False)
                _key_resp_18_allKeys.extend(theseKeys)
                if len(_key_resp_18_allKeys):
                    key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
                    key_resp_18.rt = _key_resp_18_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_18.keys == str(corrAns)) or (key_resp_18.keys == corrAns):
                        key_resp_18.corr = 1
                    else:
                        key_resp_18.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimColorComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stimColor"-------
        for thisComponent in stimColorComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_5.addData('stimImageColor.started', stimImageColor.tStartRefresh)
        trials_5.addData('stimImageColor.stopped', stimImageColor.tStopRefresh)
        trials_5.addData('leftImageColor.started', leftImageColor.tStartRefresh)
        trials_5.addData('leftImageColor.stopped', leftImageColor.tStopRefresh)
        trials_5.addData('rightImageColor.started', rightImageColor.tStartRefresh)
        trials_5.addData('rightImageColor.stopped', rightImageColor.tStopRefresh)
        # check responses
        if key_resp_18.keys in ['', [], None]:  # No response was made
            key_resp_18.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_18.corr = 1;  # correct non-response
            else:
               key_resp_18.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_5 (TrialHandler)
        trials_5.addData('key_resp_18.keys',key_resp_18.keys)
        trials_5.addData('key_resp_18.corr', key_resp_18.corr)
        if key_resp_18.keys != None:  # we had a response
            trials_5.addData('key_resp_18.rt', key_resp_18.rt)
        trials_5.addData('key_resp_18.started', key_resp_18.tStartRefresh)
        trials_5.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
        
        # ------Prepare to start Routine "feedbackColor"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        if key_resp_18.keys:
            if key_resp_18.keys[0] =='f':
                if key_resp_18.corr:
                    left = 'resources/dccs/RedRabbitRed.png'
                    right = 'resources/dccs/BlueBoatWhite.png'
                    msg = 'That is correct!'
        #            audio2 = 'resources/dccs/audio_thatsRight.mp3'
                else:
                    left = 'resources/dccs/RedRabbitWhite.png'
                    right = 'resources/dccs/BlueBoatRed.png'
                    msg = 'This is the same color, so you should choose this box.'
        #            audio2 = 'resources/dccs/audio_error_color_ft-dccs.mp3'
            elif key_resp_18.keys[0] =='j':
                if key_resp_18.corr:
                    right = 'resources/dccs/BlueBoatRed.png'
                    left = 'resources/dccs/RedRabbitWhite.png'
                    msg = 'That is correct!'
        #            audio2 = 'resources/dccs/audio_thatsRight.mp3'
                else:
                    left = 'resources/dccs/RedRabbitRed.png'
                    right = 'resources/dccs/BlueBoatWhite.png'
                    msg = 'This is the same color, so you should choose this box.'
        #            audio2 = 'resources/dccs/audio_error_color_ft-dccs.mp3'
        else:
            if corrAns == 'j':
                    right = 'resources/dccs/BlueBoatRed.png'
                    left = 'resources/dccs/RedRabbitWhite.png'
                    msg =  'This is the same color, so you should choose this box.'
        #            audio2 = 'resources/dccs/audio_error_color_ft-dccs.mp3'
            else:
                    left = 'resources/dccs/RedRabbitRed.png'
                    right = 'resources/dccs/BlueBoatWhite.png'
                    msg =  'This is the same color, so you should choose this box.'
        #            audio2 = 'resources/dccs/audio_error_color_ft-dccs.mp3'
        leftImageFeedback2.setImage(left)
        middleImageFeedback2.setImage(middle)
        rightImageFeedback2.setImage(right)
        textFeedbackColor.setText(msg)
        # keep track of which components have finished
        feedbackColorComponents = [leftImageFeedback2, middleImageFeedback2, rightImageFeedback2, textFeedbackColor]
        for thisComponent in feedbackColorComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedbackColorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedbackColor"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackColorClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackColorClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *leftImageFeedback2* updates
            if leftImageFeedback2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageFeedback2.frameNStart = frameN  # exact frame index
                leftImageFeedback2.tStart = t  # local t and not account for scr refresh
                leftImageFeedback2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageFeedback2, 'tStartRefresh')  # time at next scr refresh
                leftImageFeedback2.setAutoDraw(True)
            if leftImageFeedback2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageFeedback2.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageFeedback2.tStop = t  # not accounting for scr refresh
                    leftImageFeedback2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageFeedback2, 'tStopRefresh')  # time at next scr refresh
                    leftImageFeedback2.setAutoDraw(False)
            
            # *middleImageFeedback2* updates
            if middleImageFeedback2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                middleImageFeedback2.frameNStart = frameN  # exact frame index
                middleImageFeedback2.tStart = t  # local t and not account for scr refresh
                middleImageFeedback2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(middleImageFeedback2, 'tStartRefresh')  # time at next scr refresh
                middleImageFeedback2.setAutoDraw(True)
            if middleImageFeedback2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > middleImageFeedback2.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    middleImageFeedback2.tStop = t  # not accounting for scr refresh
                    middleImageFeedback2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(middleImageFeedback2, 'tStopRefresh')  # time at next scr refresh
                    middleImageFeedback2.setAutoDraw(False)
            
            # *rightImageFeedback2* updates
            if rightImageFeedback2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageFeedback2.frameNStart = frameN  # exact frame index
                rightImageFeedback2.tStart = t  # local t and not account for scr refresh
                rightImageFeedback2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageFeedback2, 'tStartRefresh')  # time at next scr refresh
                rightImageFeedback2.setAutoDraw(True)
            if rightImageFeedback2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageFeedback2.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageFeedback2.tStop = t  # not accounting for scr refresh
                    rightImageFeedback2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageFeedback2, 'tStopRefresh')  # time at next scr refresh
                    rightImageFeedback2.setAutoDraw(False)
            
            # *textFeedbackColor* updates
            if textFeedbackColor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textFeedbackColor.frameNStart = frameN  # exact frame index
                textFeedbackColor.tStart = t  # local t and not account for scr refresh
                textFeedbackColor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textFeedbackColor, 'tStartRefresh')  # time at next scr refresh
                textFeedbackColor.setAutoDraw(True)
            if textFeedbackColor.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textFeedbackColor.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textFeedbackColor.tStop = t  # not accounting for scr refresh
                    textFeedbackColor.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textFeedbackColor, 'tStopRefresh')  # time at next scr refresh
                    textFeedbackColor.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackColorComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedbackColor"-------
        for thisComponent in feedbackColorComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_5.addData('leftImageFeedback2.started', leftImageFeedback2.tStartRefresh)
        trials_5.addData('leftImageFeedback2.stopped', leftImageFeedback2.tStopRefresh)
        trials_5.addData('middleImageFeedback2.started', middleImageFeedback2.tStartRefresh)
        trials_5.addData('middleImageFeedback2.stopped', middleImageFeedback2.tStopRefresh)
        trials_5.addData('rightImageFeedback2.started', rightImageFeedback2.tStartRefresh)
        trials_5.addData('rightImageFeedback2.stopped', rightImageFeedback2.tStopRefresh)
        trials_5.addData('textFeedbackColor.started', textFeedbackColor.tStartRefresh)
        trials_5.addData('textFeedbackColor.stopped', textFeedbackColor.tStopRefresh)
        
        # ------Prepare to start Routine "clearColor"-------
        continueRoutine = True
        # update component parameters for each repeat
        if key_resp_18.keys:
            if key_resp_18.corr:
                counterOne +=1
            else:
                counterTwo +=1
        else:
            key_resp_18.corr = 0
            counterTwo +=1
        # keep track of which components have finished
        clearColorComponents = []
        for thisComponent in clearColorComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        clearColorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "clearColor"-------
        while continueRoutine:
            # get current time
            t = clearColorClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=clearColorClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in clearColorComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "clearColor"-------
        for thisComponent in clearColorComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "clearColor" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_5'
    
    
    # ------Prepare to start Routine "continueColor"-------
    continueRoutine = True
    # update component parameters for each repeat
    if counterOne >= 1:
        outPut = 'Lets move forward. Press the space key to continue.'
        block_2.finished = True
    if counterTwo>=1:
        outPut = 'Please try the practice again. Press the space key.'
        isForward += 1
        block_2.finished = False
        counterOne = 0
        counterTwo = 0
        if isForward == 3:
            outPut = 'Thank you for your participation!'
            block_2.finished = True
    textContinueStatus2.setText(outPut)
    key_resp_19.keys = []
    key_resp_19.rt = []
    _key_resp_19_allKeys = []
    # keep track of which components have finished
    continueColorComponents = [textContinueStatus2, key_resp_19]
    for thisComponent in continueColorComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    continueColorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "continueColor"-------
    while continueRoutine:
        # get current time
        t = continueColorClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=continueColorClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textContinueStatus2* updates
        if textContinueStatus2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textContinueStatus2.frameNStart = frameN  # exact frame index
            textContinueStatus2.tStart = t  # local t and not account for scr refresh
            textContinueStatus2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textContinueStatus2, 'tStartRefresh')  # time at next scr refresh
            textContinueStatus2.setAutoDraw(True)
        
        # *key_resp_19* updates
        waitOnFlip = False
        if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_19.frameNStart = frameN  # exact frame index
            key_resp_19.tStart = t  # local t and not account for scr refresh
            key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
            key_resp_19.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_19.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_19.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_19_allKeys.extend(theseKeys)
            if len(_key_resp_19_allKeys):
                key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
                key_resp_19.rt = _key_resp_19_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in continueColorComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "continueColor"-------
    for thisComponent in continueColorComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_2.addData('textContinueStatus2.started', textContinueStatus2.tStartRefresh)
    block_2.addData('textContinueStatus2.stopped', textContinueStatus2.tStopRefresh)
    # check responses
    if key_resp_19.keys in ['', [], None]:  # No response was made
        key_resp_19.keys = None
    block_2.addData('key_resp_19.keys',key_resp_19.keys)
    if key_resp_19.keys != None:  # we had a response
        block_2.addData('key_resp_19.rt', key_resp_19.rt)
    block_2.addData('key_resp_19.started', key_resp_19.tStartRefresh)
    block_2.addData('key_resp_19.stopped', key_resp_19.tStopRefresh)
    # the Routine "continueColor" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'block_2'


# ------Prepare to start Routine "introDCCS"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_20.keys = []
key_resp_20.rt = []
_key_resp_20_allKeys = []
# keep track of which components have finished
introDCCSComponents = [textIntroDCCS, key_resp_20]
for thisComponent in introDCCSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introDCCSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introDCCS"-------
while continueRoutine:
    # get current time
    t = introDCCSClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introDCCSClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textIntroDCCS* updates
    if textIntroDCCS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textIntroDCCS.frameNStart = frameN  # exact frame index
        textIntroDCCS.tStart = t  # local t and not account for scr refresh
        textIntroDCCS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textIntroDCCS, 'tStartRefresh')  # time at next scr refresh
        textIntroDCCS.setAutoDraw(True)
    
    # *key_resp_20* updates
    waitOnFlip = False
    if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.tStart = t  # local t and not account for scr refresh
        key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_20.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_20.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_20_allKeys.extend(theseKeys)
        if len(_key_resp_20_allKeys):
            key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
            key_resp_20.rt = _key_resp_20_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introDCCSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introDCCS"-------
for thisComponent in introDCCSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textIntroDCCS.started', textIntroDCCS.tStartRefresh)
thisExp.addData('textIntroDCCS.stopped', textIntroDCCS.tStopRefresh)
# check responses
if key_resp_20.keys in ['', [], None]:  # No response was made
    key_resp_20.keys = None
thisExp.addData('key_resp_20.keys',key_resp_20.keys)
if key_resp_20.keys != None:  # we had a response
    thisExp.addData('key_resp_20.rt', key_resp_20.rt)
thisExp.addData('key_resp_20.started', key_resp_20.tStartRefresh)
thisExp.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
thisExp.nextEntry()
# the Routine "introDCCS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructCombo"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_21.keys = []
key_resp_21.rt = []
_key_resp_21_allKeys = []
# keep track of which components have finished
instructComboComponents = [text_25, text_26, star_5, text_27, text_28, text_29, key_resp_21]
for thisComponent in instructComboComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructComboClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructCombo"-------
while continueRoutine:
    # get current time
    t = instructComboClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructComboClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_25* updates
    if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_25.frameNStart = frameN  # exact frame index
        text_25.tStart = t  # local t and not account for scr refresh
        text_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
        text_25.setAutoDraw(True)
    
    # *text_26* updates
    if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_26.frameNStart = frameN  # exact frame index
        text_26.tStart = t  # local t and not account for scr refresh
        text_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
        text_26.setAutoDraw(True)
    
    # *star_5* updates
    if star_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        star_5.frameNStart = frameN  # exact frame index
        star_5.tStart = t  # local t and not account for scr refresh
        star_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(star_5, 'tStartRefresh')  # time at next scr refresh
        star_5.setAutoDraw(True)
    
    # *text_27* updates
    if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_27.frameNStart = frameN  # exact frame index
        text_27.tStart = t  # local t and not account for scr refresh
        text_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
        text_27.setAutoDraw(True)
    
    # *text_28* updates
    if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_28.frameNStart = frameN  # exact frame index
        text_28.tStart = t  # local t and not account for scr refresh
        text_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
        text_28.setAutoDraw(True)
    
    # *text_29* updates
    if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_29.frameNStart = frameN  # exact frame index
        text_29.tStart = t  # local t and not account for scr refresh
        text_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
        text_29.setAutoDraw(True)
    
    # *key_resp_21* updates
    waitOnFlip = False
    if key_resp_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_21.frameNStart = frameN  # exact frame index
        key_resp_21.tStart = t  # local t and not account for scr refresh
        key_resp_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_21, 'tStartRefresh')  # time at next scr refresh
        key_resp_21.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_21.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_21.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_21.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_21.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_21_allKeys.extend(theseKeys)
        if len(_key_resp_21_allKeys):
            key_resp_21.keys = _key_resp_21_allKeys[-1].name  # just the last key pressed
            key_resp_21.rt = _key_resp_21_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComboComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructCombo"-------
for thisComponent in instructComboComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_25.started', text_25.tStartRefresh)
thisExp.addData('text_25.stopped', text_25.tStopRefresh)
thisExp.addData('text_26.started', text_26.tStartRefresh)
thisExp.addData('text_26.stopped', text_26.tStopRefresh)
thisExp.addData('star_5.started', star_5.tStartRefresh)
thisExp.addData('star_5.stopped', star_5.tStopRefresh)
thisExp.addData('text_27.started', text_27.tStartRefresh)
thisExp.addData('text_27.stopped', text_27.tStopRefresh)
thisExp.addData('text_28.started', text_28.tStartRefresh)
thisExp.addData('text_28.stopped', text_28.tStopRefresh)
thisExp.addData('text_29.started', text_29.tStartRefresh)
thisExp.addData('text_29.stopped', text_29.tStopRefresh)
# check responses
if key_resp_21.keys in ['', [], None]:  # No response was made
    key_resp_21.keys = None
thisExp.addData('key_resp_21.keys',key_resp_21.keys)
if key_resp_21.keys != None:  # we had a response
    thisExp.addData('key_resp_21.rt', key_resp_21.rt)
thisExp.addData('key_resp_21.started', key_resp_21.tStartRefresh)
thisExp.addData('key_resp_21.stopped', key_resp_21.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructCombo" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
LoopSelectFreqNumber = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('resources/selectFreqNum.csv'),
    seed=None, name='LoopSelectFreqNumber')
thisExp.addLoop(LoopSelectFreqNumber)  # add the loop to the experiment
thisLoopSelectFreqNumber = LoopSelectFreqNumber.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopSelectFreqNumber.rgb)
if thisLoopSelectFreqNumber != None:
    for paramName in thisLoopSelectFreqNumber:
        exec('{} = thisLoopSelectFreqNumber[paramName]'.format(paramName))

for thisLoopSelectFreqNumber in LoopSelectFreqNumber:
    currentLoop = LoopSelectFreqNumber
    # abbreviate parameter names if possible (e.g. rgb = thisLoopSelectFreqNumber.rgb)
    if thisLoopSelectFreqNumber != None:
        for paramName in thisLoopSelectFreqNumber:
            exec('{} = thisLoopSelectFreqNumber[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "countReset"-------
    continueRoutine = True
    # update component parameters for each repeat
    colorLoopCounter = 0
    shapeLoopCounter = 0
    # keep track of which components have finished
    countResetComponents = []
    for thisComponent in countResetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    countResetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "countReset"-------
    while continueRoutine:
        # get current time
        t = countResetClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=countResetClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countResetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "countReset"-------
    for thisComponent in countResetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "countReset" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    colorLoop = data.TrialHandler(nReps=1.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('resources/color.csv'),
        seed=None, name='colorLoop')
    thisExp.addLoop(colorLoop)  # add the loop to the experiment
    thisColorLoop = colorLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisColorLoop.rgb)
    if thisColorLoop != None:
        for paramName in thisColorLoop:
            exec('{} = thisColorLoop[paramName]'.format(paramName))
    
    for thisColorLoop in colorLoop:
        currentLoop = colorLoop
        # abbreviate parameter names if possible (e.g. rgb = thisColorLoop.rgb)
        if thisColorLoop != None:
            for paramName in thisColorLoop:
                exec('{} = thisColorLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "interTrialCombo"-------
        continueRoutine = True
        routineTimer.add(0.800000)
        # update component parameters for each repeat
        # keep track of which components have finished
        interTrialComboComponents = [image_25, image_26]
        for thisComponent in interTrialComboComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        interTrialComboClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "interTrialCombo"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = interTrialComboClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=interTrialComboClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_25* updates
            if image_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_25.frameNStart = frameN  # exact frame index
                image_25.tStart = t  # local t and not account for scr refresh
                image_25.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_25, 'tStartRefresh')  # time at next scr refresh
                image_25.setAutoDraw(True)
            if image_25.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_25.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    image_25.tStop = t  # not accounting for scr refresh
                    image_25.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_25, 'tStopRefresh')  # time at next scr refresh
                    image_25.setAutoDraw(False)
            
            # *image_26* updates
            if image_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_26.frameNStart = frameN  # exact frame index
                image_26.tStart = t  # local t and not account for scr refresh
                image_26.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_26, 'tStartRefresh')  # time at next scr refresh
                image_26.setAutoDraw(True)
            if image_26.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_26.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    image_26.tStop = t  # not accounting for scr refresh
                    image_26.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_26, 'tStopRefresh')  # time at next scr refresh
                    image_26.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in interTrialComboComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "interTrialCombo"-------
        for thisComponent in interTrialComboComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        colorLoop.addData('image_25.started', image_25.tStartRefresh)
        colorLoop.addData('image_25.stopped', image_25.tStopRefresh)
        colorLoop.addData('image_26.started', image_26.tStartRefresh)
        colorLoop.addData('image_26.stopped', image_26.tStopRefresh)
        
        # ------Prepare to start Routine "ISICodeCombo"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ISICodeComboComponents = []
        for thisComponent in ISICodeComboComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISICodeComboClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISICodeCombo"-------
        while continueRoutine:
            # get current time
            t = ISICodeComboClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISICodeComboClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISICodeComboComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISICodeCombo"-------
        for thisComponent in ISICodeComboComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # pick the ISI for the next routine
        # this code component is set to 'both' because we need to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(1000, 1500, 500)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # show in console for debugging
        print('thisISI: ', thisISI)
        
        # save this ISI to our output file
        colorLoop.addData('ISI', thisISI)
        # the Routine "ISICodeCombo" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fixationCombo"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComboComponents = [star_6, leftImageFixation3, rightImageFixation3]
        for thisComponent in fixationComboComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationComboClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixationCombo"-------
        while continueRoutine:
            # get current time
            t = fixationComboClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationComboClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *star_6* updates
            if star_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                star_6.frameNStart = frameN  # exact frame index
                star_6.tStart = t  # local t and not account for scr refresh
                star_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star_6, 'tStartRefresh')  # time at next scr refresh
                star_6.setAutoDraw(True)
            if star_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > star_6.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    star_6.tStop = t  # not accounting for scr refresh
                    star_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(star_6, 'tStopRefresh')  # time at next scr refresh
                    star_6.setAutoDraw(False)
            
            # *leftImageFixation3* updates
            if leftImageFixation3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageFixation3.frameNStart = frameN  # exact frame index
                leftImageFixation3.tStart = t  # local t and not account for scr refresh
                leftImageFixation3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageFixation3, 'tStartRefresh')  # time at next scr refresh
                leftImageFixation3.setAutoDraw(True)
            if leftImageFixation3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageFixation3.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageFixation3.tStop = t  # not accounting for scr refresh
                    leftImageFixation3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageFixation3, 'tStopRefresh')  # time at next scr refresh
                    leftImageFixation3.setAutoDraw(False)
            
            # *rightImageFixation3* updates
            if rightImageFixation3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageFixation3.frameNStart = frameN  # exact frame index
                rightImageFixation3.tStart = t  # local t and not account for scr refresh
                rightImageFixation3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageFixation3, 'tStartRefresh')  # time at next scr refresh
                rightImageFixation3.setAutoDraw(True)
            if rightImageFixation3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageFixation3.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageFixation3.tStop = t  # not accounting for scr refresh
                    rightImageFixation3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageFixation3, 'tStopRefresh')  # time at next scr refresh
                    rightImageFixation3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComboComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixationCombo"-------
        for thisComponent in fixationComboComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        colorLoop.addData('star_6.started', star_6.tStartRefresh)
        colorLoop.addData('star_6.stopped', star_6.tStopRefresh)
        colorLoop.addData('leftImageFixation3.started', leftImageFixation3.tStartRefresh)
        colorLoop.addData('leftImageFixation3.stopped', leftImageFixation3.tStopRefresh)
        colorLoop.addData('rightImageFixation3.started', rightImageFixation3.tStartRefresh)
        colorLoop.addData('rightImageFixation3.stopped', rightImageFixation3.tStopRefresh)
        # the Routine "fixationCombo" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "cueCombo"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        textCueCombo.setText(cue)
        # keep track of which components have finished
        cueComboComponents = [textCueCombo, leftImageCue3, rightImageCue3]
        for thisComponent in cueComboComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cueComboClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "cueCombo"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cueComboClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cueComboClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textCueCombo* updates
            if textCueCombo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textCueCombo.frameNStart = frameN  # exact frame index
                textCueCombo.tStart = t  # local t and not account for scr refresh
                textCueCombo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textCueCombo, 'tStartRefresh')  # time at next scr refresh
                textCueCombo.setAutoDraw(True)
            if textCueCombo.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textCueCombo.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textCueCombo.tStop = t  # not accounting for scr refresh
                    textCueCombo.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textCueCombo, 'tStopRefresh')  # time at next scr refresh
                    textCueCombo.setAutoDraw(False)
            
            # *leftImageCue3* updates
            if leftImageCue3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageCue3.frameNStart = frameN  # exact frame index
                leftImageCue3.tStart = t  # local t and not account for scr refresh
                leftImageCue3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageCue3, 'tStartRefresh')  # time at next scr refresh
                leftImageCue3.setAutoDraw(True)
            if leftImageCue3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageCue3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageCue3.tStop = t  # not accounting for scr refresh
                    leftImageCue3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageCue3, 'tStopRefresh')  # time at next scr refresh
                    leftImageCue3.setAutoDraw(False)
            
            # *rightImageCue3* updates
            if rightImageCue3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageCue3.frameNStart = frameN  # exact frame index
                rightImageCue3.tStart = t  # local t and not account for scr refresh
                rightImageCue3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageCue3, 'tStartRefresh')  # time at next scr refresh
                rightImageCue3.setAutoDraw(True)
            if rightImageCue3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageCue3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageCue3.tStop = t  # not accounting for scr refresh
                    rightImageCue3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageCue3, 'tStopRefresh')  # time at next scr refresh
                    rightImageCue3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cueComboComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cueCombo"-------
        for thisComponent in cueComboComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        colorLoop.addData('textCueCombo.started', textCueCombo.tStartRefresh)
        colorLoop.addData('textCueCombo.stopped', textCueCombo.tStopRefresh)
        colorLoop.addData('leftImageCue3.started', leftImageCue3.tStartRefresh)
        colorLoop.addData('leftImageCue3.stopped', leftImageCue3.tStopRefresh)
        colorLoop.addData('rightImageCue3.started', rightImageCue3.tStartRefresh)
        colorLoop.addData('rightImageCue3.stopped', rightImageCue3.tStopRefresh)
        
        # ------Prepare to start Routine "stimCombo"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        stimImageCombo.setImage(middle)
        leftImageCombo.setImage(left)
        rightImageCombo.setImage(right)
        key_resp_22.keys = []
        key_resp_22.rt = []
        _key_resp_22_allKeys = []
        # keep track of which components have finished
        stimComboComponents = [stimImageCombo, leftImageCombo, rightImageCombo, key_resp_22]
        for thisComponent in stimComboComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stimComboClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stimCombo"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimComboClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stimComboClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimImageCombo* updates
            if stimImageCombo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimImageCombo.frameNStart = frameN  # exact frame index
                stimImageCombo.tStart = t  # local t and not account for scr refresh
                stimImageCombo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimImageCombo, 'tStartRefresh')  # time at next scr refresh
                stimImageCombo.setAutoDraw(True)
            if stimImageCombo.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimImageCombo.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    stimImageCombo.tStop = t  # not accounting for scr refresh
                    stimImageCombo.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimImageCombo, 'tStopRefresh')  # time at next scr refresh
                    stimImageCombo.setAutoDraw(False)
            
            # *leftImageCombo* updates
            if leftImageCombo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageCombo.frameNStart = frameN  # exact frame index
                leftImageCombo.tStart = t  # local t and not account for scr refresh
                leftImageCombo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageCombo, 'tStartRefresh')  # time at next scr refresh
                leftImageCombo.setAutoDraw(True)
            if leftImageCombo.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageCombo.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageCombo.tStop = t  # not accounting for scr refresh
                    leftImageCombo.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageCombo, 'tStopRefresh')  # time at next scr refresh
                    leftImageCombo.setAutoDraw(False)
            
            # *rightImageCombo* updates
            if rightImageCombo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageCombo.frameNStart = frameN  # exact frame index
                rightImageCombo.tStart = t  # local t and not account for scr refresh
                rightImageCombo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageCombo, 'tStartRefresh')  # time at next scr refresh
                rightImageCombo.setAutoDraw(True)
            if rightImageCombo.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageCombo.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageCombo.tStop = t  # not accounting for scr refresh
                    rightImageCombo.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageCombo, 'tStopRefresh')  # time at next scr refresh
                    rightImageCombo.setAutoDraw(False)
            
            # *key_resp_22* updates
            waitOnFlip = False
            if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_22.frameNStart = frameN  # exact frame index
                key_resp_22.tStart = t  # local t and not account for scr refresh
                key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
                key_resp_22.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_22.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_22.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_22.tStop = t  # not accounting for scr refresh
                    key_resp_22.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_22, 'tStopRefresh')  # time at next scr refresh
                    key_resp_22.status = FINISHED
            if key_resp_22.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_22.getKeys(keyList=['f', 'j'], waitRelease=False)
                _key_resp_22_allKeys.extend(theseKeys)
                if len(_key_resp_22_allKeys):
                    key_resp_22.keys = _key_resp_22_allKeys[-1].name  # just the last key pressed
                    key_resp_22.rt = _key_resp_22_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_22.keys == str(corrAns)) or (key_resp_22.keys == corrAns):
                        key_resp_22.corr = 1
                    else:
                        key_resp_22.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimComboComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stimCombo"-------
        for thisComponent in stimComboComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        colorLoop.addData('stimImageCombo.started', stimImageCombo.tStartRefresh)
        colorLoop.addData('stimImageCombo.stopped', stimImageCombo.tStopRefresh)
        colorLoop.addData('leftImageCombo.started', leftImageCombo.tStartRefresh)
        colorLoop.addData('leftImageCombo.stopped', leftImageCombo.tStopRefresh)
        colorLoop.addData('rightImageCombo.started', rightImageCombo.tStartRefresh)
        colorLoop.addData('rightImageCombo.stopped', rightImageCombo.tStopRefresh)
        # check responses
        if key_resp_22.keys in ['', [], None]:  # No response was made
            key_resp_22.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_22.corr = 1;  # correct non-response
            else:
               key_resp_22.corr = 0;  # failed to respond (incorrectly)
        # store data for colorLoop (TrialHandler)
        colorLoop.addData('key_resp_22.keys',key_resp_22.keys)
        colorLoop.addData('key_resp_22.corr', key_resp_22.corr)
        if key_resp_22.keys != None:  # we had a response
            colorLoop.addData('key_resp_22.rt', key_resp_22.rt)
        colorLoop.addData('key_resp_22.started', key_resp_22.tStartRefresh)
        colorLoop.addData('key_resp_22.stopped', key_resp_22.tStopRefresh)
        
        # ------Prepare to start Routine "stopColorLoop"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        stopColorLoopComponents = []
        for thisComponent in stopColorLoopComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stopColorLoopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stopColorLoop"-------
        while continueRoutine:
            # get current time
            t = stopColorLoopClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stopColorLoopClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stopColorLoopComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stopColorLoop"-------
        for thisComponent in stopColorLoopComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if colorLoopCounter==numFreq:
            colorLoop.finished=True
        colorLoopCounter +=1
        # the Routine "stopColorLoop" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'colorLoop'
    
    
    # set up handler to look after randomisation of conditions etc
    shapeLoop = data.TrialHandler(nReps=1.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('resources/shape.csv'),
        seed=None, name='shapeLoop')
    thisExp.addLoop(shapeLoop)  # add the loop to the experiment
    thisShapeLoop = shapeLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisShapeLoop.rgb)
    if thisShapeLoop != None:
        for paramName in thisShapeLoop:
            exec('{} = thisShapeLoop[paramName]'.format(paramName))
    
    for thisShapeLoop in shapeLoop:
        currentLoop = shapeLoop
        # abbreviate parameter names if possible (e.g. rgb = thisShapeLoop.rgb)
        if thisShapeLoop != None:
            for paramName in thisShapeLoop:
                exec('{} = thisShapeLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "interTrialCombo"-------
        continueRoutine = True
        routineTimer.add(0.800000)
        # update component parameters for each repeat
        # keep track of which components have finished
        interTrialComboComponents = [image_25, image_26]
        for thisComponent in interTrialComboComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        interTrialComboClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "interTrialCombo"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = interTrialComboClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=interTrialComboClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_25* updates
            if image_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_25.frameNStart = frameN  # exact frame index
                image_25.tStart = t  # local t and not account for scr refresh
                image_25.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_25, 'tStartRefresh')  # time at next scr refresh
                image_25.setAutoDraw(True)
            if image_25.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_25.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    image_25.tStop = t  # not accounting for scr refresh
                    image_25.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_25, 'tStopRefresh')  # time at next scr refresh
                    image_25.setAutoDraw(False)
            
            # *image_26* updates
            if image_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_26.frameNStart = frameN  # exact frame index
                image_26.tStart = t  # local t and not account for scr refresh
                image_26.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_26, 'tStartRefresh')  # time at next scr refresh
                image_26.setAutoDraw(True)
            if image_26.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_26.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    image_26.tStop = t  # not accounting for scr refresh
                    image_26.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_26, 'tStopRefresh')  # time at next scr refresh
                    image_26.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in interTrialComboComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "interTrialCombo"-------
        for thisComponent in interTrialComboComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        shapeLoop.addData('image_25.started', image_25.tStartRefresh)
        shapeLoop.addData('image_25.stopped', image_25.tStopRefresh)
        shapeLoop.addData('image_26.started', image_26.tStartRefresh)
        shapeLoop.addData('image_26.stopped', image_26.tStopRefresh)
        
        # ------Prepare to start Routine "ISICodeCombo"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ISICodeComboComponents = []
        for thisComponent in ISICodeComboComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISICodeComboClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISICodeCombo"-------
        while continueRoutine:
            # get current time
            t = ISICodeComboClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISICodeComboClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISICodeComboComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISICodeCombo"-------
        for thisComponent in ISICodeComboComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # pick the ISI for the next routine
        # this code component is set to 'both' because we need to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(1000, 1500, 500)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # show in console for debugging
        print('thisISI: ', thisISI)
        
        # save this ISI to our output file
        colorLoop.addData('ISI', thisISI)
        # the Routine "ISICodeCombo" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fixationCombo"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComboComponents = [star_6, leftImageFixation3, rightImageFixation3]
        for thisComponent in fixationComboComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationComboClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixationCombo"-------
        while continueRoutine:
            # get current time
            t = fixationComboClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationComboClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *star_6* updates
            if star_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                star_6.frameNStart = frameN  # exact frame index
                star_6.tStart = t  # local t and not account for scr refresh
                star_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star_6, 'tStartRefresh')  # time at next scr refresh
                star_6.setAutoDraw(True)
            if star_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > star_6.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    star_6.tStop = t  # not accounting for scr refresh
                    star_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(star_6, 'tStopRefresh')  # time at next scr refresh
                    star_6.setAutoDraw(False)
            
            # *leftImageFixation3* updates
            if leftImageFixation3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageFixation3.frameNStart = frameN  # exact frame index
                leftImageFixation3.tStart = t  # local t and not account for scr refresh
                leftImageFixation3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageFixation3, 'tStartRefresh')  # time at next scr refresh
                leftImageFixation3.setAutoDraw(True)
            if leftImageFixation3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageFixation3.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageFixation3.tStop = t  # not accounting for scr refresh
                    leftImageFixation3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageFixation3, 'tStopRefresh')  # time at next scr refresh
                    leftImageFixation3.setAutoDraw(False)
            
            # *rightImageFixation3* updates
            if rightImageFixation3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageFixation3.frameNStart = frameN  # exact frame index
                rightImageFixation3.tStart = t  # local t and not account for scr refresh
                rightImageFixation3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageFixation3, 'tStartRefresh')  # time at next scr refresh
                rightImageFixation3.setAutoDraw(True)
            if rightImageFixation3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageFixation3.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageFixation3.tStop = t  # not accounting for scr refresh
                    rightImageFixation3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageFixation3, 'tStopRefresh')  # time at next scr refresh
                    rightImageFixation3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComboComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixationCombo"-------
        for thisComponent in fixationComboComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        shapeLoop.addData('star_6.started', star_6.tStartRefresh)
        shapeLoop.addData('star_6.stopped', star_6.tStopRefresh)
        shapeLoop.addData('leftImageFixation3.started', leftImageFixation3.tStartRefresh)
        shapeLoop.addData('leftImageFixation3.stopped', leftImageFixation3.tStopRefresh)
        shapeLoop.addData('rightImageFixation3.started', rightImageFixation3.tStartRefresh)
        shapeLoop.addData('rightImageFixation3.stopped', rightImageFixation3.tStopRefresh)
        # the Routine "fixationCombo" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "cueCombo"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        textCueCombo.setText(cue)
        # keep track of which components have finished
        cueComboComponents = [textCueCombo, leftImageCue3, rightImageCue3]
        for thisComponent in cueComboComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cueComboClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "cueCombo"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cueComboClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cueComboClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textCueCombo* updates
            if textCueCombo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textCueCombo.frameNStart = frameN  # exact frame index
                textCueCombo.tStart = t  # local t and not account for scr refresh
                textCueCombo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textCueCombo, 'tStartRefresh')  # time at next scr refresh
                textCueCombo.setAutoDraw(True)
            if textCueCombo.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textCueCombo.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textCueCombo.tStop = t  # not accounting for scr refresh
                    textCueCombo.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textCueCombo, 'tStopRefresh')  # time at next scr refresh
                    textCueCombo.setAutoDraw(False)
            
            # *leftImageCue3* updates
            if leftImageCue3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageCue3.frameNStart = frameN  # exact frame index
                leftImageCue3.tStart = t  # local t and not account for scr refresh
                leftImageCue3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageCue3, 'tStartRefresh')  # time at next scr refresh
                leftImageCue3.setAutoDraw(True)
            if leftImageCue3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageCue3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageCue3.tStop = t  # not accounting for scr refresh
                    leftImageCue3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageCue3, 'tStopRefresh')  # time at next scr refresh
                    leftImageCue3.setAutoDraw(False)
            
            # *rightImageCue3* updates
            if rightImageCue3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageCue3.frameNStart = frameN  # exact frame index
                rightImageCue3.tStart = t  # local t and not account for scr refresh
                rightImageCue3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageCue3, 'tStartRefresh')  # time at next scr refresh
                rightImageCue3.setAutoDraw(True)
            if rightImageCue3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageCue3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageCue3.tStop = t  # not accounting for scr refresh
                    rightImageCue3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageCue3, 'tStopRefresh')  # time at next scr refresh
                    rightImageCue3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cueComboComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cueCombo"-------
        for thisComponent in cueComboComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        shapeLoop.addData('textCueCombo.started', textCueCombo.tStartRefresh)
        shapeLoop.addData('textCueCombo.stopped', textCueCombo.tStopRefresh)
        shapeLoop.addData('leftImageCue3.started', leftImageCue3.tStartRefresh)
        shapeLoop.addData('leftImageCue3.stopped', leftImageCue3.tStopRefresh)
        shapeLoop.addData('rightImageCue3.started', rightImageCue3.tStartRefresh)
        shapeLoop.addData('rightImageCue3.stopped', rightImageCue3.tStopRefresh)
        
        # ------Prepare to start Routine "stimCombo"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        stimImageCombo.setImage(middle)
        leftImageCombo.setImage(left)
        rightImageCombo.setImage(right)
        key_resp_22.keys = []
        key_resp_22.rt = []
        _key_resp_22_allKeys = []
        # keep track of which components have finished
        stimComboComponents = [stimImageCombo, leftImageCombo, rightImageCombo, key_resp_22]
        for thisComponent in stimComboComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stimComboClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stimCombo"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimComboClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stimComboClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimImageCombo* updates
            if stimImageCombo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimImageCombo.frameNStart = frameN  # exact frame index
                stimImageCombo.tStart = t  # local t and not account for scr refresh
                stimImageCombo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimImageCombo, 'tStartRefresh')  # time at next scr refresh
                stimImageCombo.setAutoDraw(True)
            if stimImageCombo.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimImageCombo.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    stimImageCombo.tStop = t  # not accounting for scr refresh
                    stimImageCombo.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimImageCombo, 'tStopRefresh')  # time at next scr refresh
                    stimImageCombo.setAutoDraw(False)
            
            # *leftImageCombo* updates
            if leftImageCombo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImageCombo.frameNStart = frameN  # exact frame index
                leftImageCombo.tStart = t  # local t and not account for scr refresh
                leftImageCombo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImageCombo, 'tStartRefresh')  # time at next scr refresh
                leftImageCombo.setAutoDraw(True)
            if leftImageCombo.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImageCombo.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImageCombo.tStop = t  # not accounting for scr refresh
                    leftImageCombo.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImageCombo, 'tStopRefresh')  # time at next scr refresh
                    leftImageCombo.setAutoDraw(False)
            
            # *rightImageCombo* updates
            if rightImageCombo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImageCombo.frameNStart = frameN  # exact frame index
                rightImageCombo.tStart = t  # local t and not account for scr refresh
                rightImageCombo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImageCombo, 'tStartRefresh')  # time at next scr refresh
                rightImageCombo.setAutoDraw(True)
            if rightImageCombo.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImageCombo.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImageCombo.tStop = t  # not accounting for scr refresh
                    rightImageCombo.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImageCombo, 'tStopRefresh')  # time at next scr refresh
                    rightImageCombo.setAutoDraw(False)
            
            # *key_resp_22* updates
            waitOnFlip = False
            if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_22.frameNStart = frameN  # exact frame index
                key_resp_22.tStart = t  # local t and not account for scr refresh
                key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
                key_resp_22.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_22.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_22.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_22.tStop = t  # not accounting for scr refresh
                    key_resp_22.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_22, 'tStopRefresh')  # time at next scr refresh
                    key_resp_22.status = FINISHED
            if key_resp_22.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_22.getKeys(keyList=['f', 'j'], waitRelease=False)
                _key_resp_22_allKeys.extend(theseKeys)
                if len(_key_resp_22_allKeys):
                    key_resp_22.keys = _key_resp_22_allKeys[-1].name  # just the last key pressed
                    key_resp_22.rt = _key_resp_22_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_22.keys == str(corrAns)) or (key_resp_22.keys == corrAns):
                        key_resp_22.corr = 1
                    else:
                        key_resp_22.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimComboComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stimCombo"-------
        for thisComponent in stimComboComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        shapeLoop.addData('stimImageCombo.started', stimImageCombo.tStartRefresh)
        shapeLoop.addData('stimImageCombo.stopped', stimImageCombo.tStopRefresh)
        shapeLoop.addData('leftImageCombo.started', leftImageCombo.tStartRefresh)
        shapeLoop.addData('leftImageCombo.stopped', leftImageCombo.tStopRefresh)
        shapeLoop.addData('rightImageCombo.started', rightImageCombo.tStartRefresh)
        shapeLoop.addData('rightImageCombo.stopped', rightImageCombo.tStopRefresh)
        # check responses
        if key_resp_22.keys in ['', [], None]:  # No response was made
            key_resp_22.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_22.corr = 1;  # correct non-response
            else:
               key_resp_22.corr = 0;  # failed to respond (incorrectly)
        # store data for shapeLoop (TrialHandler)
        shapeLoop.addData('key_resp_22.keys',key_resp_22.keys)
        shapeLoop.addData('key_resp_22.corr', key_resp_22.corr)
        if key_resp_22.keys != None:  # we had a response
            shapeLoop.addData('key_resp_22.rt', key_resp_22.rt)
        shapeLoop.addData('key_resp_22.started', key_resp_22.tStartRefresh)
        shapeLoop.addData('key_resp_22.stopped', key_resp_22.tStopRefresh)
        
        # ------Prepare to start Routine "stopShapeLoop"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        stopShapeLoopComponents = []
        for thisComponent in stopShapeLoopComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stopShapeLoopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stopShapeLoop"-------
        while continueRoutine:
            # get current time
            t = stopShapeLoopClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stopShapeLoopClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stopShapeLoopComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stopShapeLoop"-------
        for thisComponent in stopShapeLoopComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if shapeLoopCounter==0:
            shapeLoop.finished=True
        shapeLoopCounter +=1
        # the Routine "stopShapeLoop" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'shapeLoop'
    
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'LoopSelectFreqNumber'


# ------Prepare to start Routine "goodbye"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_23.keys = []
key_resp_23.rt = []
_key_resp_23_allKeys = []
# keep track of which components have finished
goodbyeComponents = [headerGoodbye, messageGoodbye, key_resp_23]
for thisComponent in goodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
goodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "goodbye"-------
while continueRoutine:
    # get current time
    t = goodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=goodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *headerGoodbye* updates
    if headerGoodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        headerGoodbye.frameNStart = frameN  # exact frame index
        headerGoodbye.tStart = t  # local t and not account for scr refresh
        headerGoodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(headerGoodbye, 'tStartRefresh')  # time at next scr refresh
        headerGoodbye.setAutoDraw(True)
    
    # *messageGoodbye* updates
    if messageGoodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        messageGoodbye.frameNStart = frameN  # exact frame index
        messageGoodbye.tStart = t  # local t and not account for scr refresh
        messageGoodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(messageGoodbye, 'tStartRefresh')  # time at next scr refresh
        messageGoodbye.setAutoDraw(True)
    
    # *key_resp_23* updates
    waitOnFlip = False
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_23_allKeys.extend(theseKeys)
        if len(_key_resp_23_allKeys):
            key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
            key_resp_23.rt = _key_resp_23_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goodbye"-------
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('headerGoodbye.started', headerGoodbye.tStartRefresh)
thisExp.addData('headerGoodbye.stopped', headerGoodbye.tStopRefresh)
thisExp.addData('messageGoodbye.started', messageGoodbye.tStartRefresh)
thisExp.addData('messageGoodbye.stopped', messageGoodbye.tStopRefresh)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys = None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
thisExp.addData('key_resp_23.started', key_resp_23.tStartRefresh)
thisExp.addData('key_resp_23.stopped', key_resp_23.tStopRefresh)
thisExp.nextEntry()
# the Routine "goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
