import time
from datetime import datetime
import atexit


def atex_func():
    print('atex_func end')
    with open(f"atexit.txt","a") as f:
        f.write('\n{datetime.now} atexit end')

    

import signal
import sys

def signal_func(signum, frame):
    print(f"signal_func end  type {signum}")
    with open("signal.txt","a") as f:
        f.write('\n{datetime.now} signal end')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_func)
signal.signal(signal.SIGTERM, signal_func)

i=0
while True:
    time.sleep(5)
    i+=1
    with open("doing.txt","a") as f:
        f.write('do smth')
    print(i)