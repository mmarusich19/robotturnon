import time
import setup
from setup import RPL
import RoboPiLib as RPL
RPL.servoWrite(0,1000)
start = time.time()

global x
x = 2

while True:
    global x
    x = x % 2
    elapsed = (time.time() - start)
    elapsed = int(elapsed)
    if elapsed % 6 == 0:
        if elapsed == 0:
             RPL.servoWrite(0,1000)
    if elapsed % 3 == 0:
        if elapsed == 3:
            import RoboPiLib as RPL
            import setup
            RPL.servoWrite(0,0)
    x = x + 1
