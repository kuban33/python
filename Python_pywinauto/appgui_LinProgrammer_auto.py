# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:58:37 2019

"""
import sys
from pywinauto.timings import Timings
from pywinauto.application import Application

apppath="C:\\Program Files (x86)\\Linak\\LinProgrammer\\LinProgrammer.exe"
cfgpath="\\\\czcifi02.tymphany.com\\LV_Instr\\LV_Doc\\V300\\SW\\LINAK\\LinakConfigFiles\\ConfigFiles_26062019\\V300_config_15mms_20_mmss.cfg"

Timings.Slow()

#start app
app = Application().start(apppath)

#main app
dlg_app=app['LinProgrammer. Version 1.45']
#button Load File
dlg_app['Load file'].click()

#Open dialog
dlg_open=app.window(title="Open")
#entry path to file
dlg_open['File name:Edit'].set_text(cfgpath)
#confirm 
dlg_open['Open'].click()

dlg_app['Program'].wait('enabled')
#back to main app, program button
dlg_app['Program'].click()

dlg_app['Verify'].wait('enabled')
#back to main app, verify button
dlg_app['Verify'].click()

print(" >>>>>> ")
print(dlg_app.print_control_identifiers)

sys.exit(0)