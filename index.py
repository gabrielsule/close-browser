import time
import os

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Cerrando')
    closebrowser()

def closebrowser():
    os.system('taskkill /im firefox.exe /f')
    os.system('taskkill /im chrome.exe /f')

countdown(10)    
