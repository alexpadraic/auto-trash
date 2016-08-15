from time import sleep
#!/usr/bin/env python
 
# import required libs
import time
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
import os
import calendar
import datetime
import time

os.chdir('/home/pi/Pictures')

def ClickPictures():
  date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
  camera = PiCamera()
  camera.resolution = (1024,768)

  for i in range(11):
    camera.capture(date+'_'+str(i)+'_img.jpg')
  

def CounterClockwise():
  
  GPIO.cleanup() #cleaning up in case GPIOS have been preactivated
 
# Use BCM GPIO references
# instead of physical pin numbers
  GPIO.setmode(GPIO.BCM)
 
# be sure you are setting pins accordingly
# GPIO10,GPIO9,GPIO11,GPI25
  StepPins = [17,18,21,22]
 
# Set all pins as output
  for pin in StepPins:
      GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, False)

  seq = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
  for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(StepPins[pin], seq[halfstep][pin])
            time.sleep(0.001)

  GPIO.cleanup();

def ClockWise():

  GPIO.cleanup() #cleaning up in case GPIOS have been preactivated
 
# Use BCM GPIO references
# instead of physical pin numbers
  GPIO.setmode(GPIO.BCM)
 
# be sure you are setting pins accordingly
# GPIO10,GPIO9,GPIO11,GPI25
  StepPins = [17,18,21,22]
 
# Set all pins as output
  for pin in StepPins:
      GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, False)
      
  seq = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
  seq.reverse()
  for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(StepPins[pin], seq[halfstep][pin])
            time.sleep(0.001)
  GPIO.cleanup();

##ClickPictures();
##CounterClockwise();
ClockWise();


  
    
