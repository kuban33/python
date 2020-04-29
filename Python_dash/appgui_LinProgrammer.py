# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:58:37 2019

"""
import sys
from pywinauto.application import Application

cfgpath = '\\\czcifi02.tymphany.com\LV_Instr\LV_Doc\V300\SW\LINAK\LinakConfigFiles\SettlingRig_15mms_0_440mm_hrbitov_v01.cfg'

#sys.exit(1)

app = Application().start("C:\Program Files (x86)\Linak\LinProgrammer\LinProgrammer.exe")
dlg = app['LinProgrammer. Version 1.45']
buttonOK = dlg['Load file']
buttonOK.click()

#app.window(title="Open")['File name:Edit'].set_text('ahoj')

dlgload = app.window(title="Open")
editFilename = dlgload['File name:Edit']
editFilename.set_text(cfgpath)
buttonOpwn = dlgload['Cancel']
#buttonCancel.click()
#'Open'

#app['LinProgrammer. Version 1.45']['Load file'].click()


sys.exit(0)