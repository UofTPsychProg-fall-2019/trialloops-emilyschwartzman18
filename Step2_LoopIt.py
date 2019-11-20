#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()


#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things

#face1=visual.ImageStim(mywin,pos=(0,0),size=(.71,.71),image='bf01_h.jpg')
#face1.draw()
#mywin.flip()
#keys=event.waitKeys(keyList='space')

# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']
stim=['bf01_h.jpg','bm1_h.jpg','wf1_h.jpg']

# make your loop
facenum=0
for t in stim:
    facenum=facenum+1
    face=visual.ImageStim(win,pos=(0,0),size=(.71,.71),image=t)
    text=visual.TextStim(win,pos=(0,.6),color=(-1,-1,-1),text='face '+str(facenum))
    face.draw()
    text.draw()
    win.flip()
    keys=event.waitKeys(keyList='space')
    
    # include your trial code in your loop but replace anything that should 
    # change on each trial with a variable that uses your iterater
    # e.g. thisStimName = stim[t]
    #      thisStim = visual.ImageStim(win, image=thisStimName ...)
    
    # if you're recording responses, be sure to store your responses in a list
    # or DataFrame which also uses your iterater!


#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(2)
win.close()
