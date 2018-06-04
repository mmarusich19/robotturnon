import time
import setup
from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions

sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)


while True:
  PTW.state['d1'] = RPL.digitalRead(sensor_pin)
  PTW.post()

  import RoboPiLib as RPL
  import setup
  RPL.servoWrite(0,1000)
  RPL.servoWrite(1,2000)
  if RPL.digitalRead(sensor_pin) == 0:
     import RoboPiLib as RPL
     import setup
     RPL.servoWrite(0,1000)
     RPL.servoWrite(1,15000)
     time.sleep(2)
     RPL.servoWrite(0,1000)
     RPL.servoWrite(1,2000)
    

