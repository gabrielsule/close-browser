import time
import os
import sys
import psutil
import click

def countdown(t, p):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

    closeApp(p)
    

def closeApp(procName):
    os.system('taskkill /im '+ procName +'.exe /f')
    

def isAlive(procName):
    for proc in psutil.process_iter():
        try:
            if procName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;     


@click.command()
@click.option('--proc', '-p', required=True,
    help='proceso a cerrar',
)
@click.option('--time', '-t', required=False,
    help='tiempo de espera', default='10'
)
def process(proc, time):
    _p = proc
    _t = int(time)

    if isAlive(_p):
        countdown(_t, _p)

if __name__ =='__main__':
    process()
