from time import sleep
from picamera import PiCamera
import os
import calendar
import datetime

os.chdir('/home/pi/Pictures')

import datetime
import time
date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

camera = PiCamera()
camera.resolution = (1024,768)

for i in range(11):
    camera.capture(date+'_'+str(i)+'_img.jpg')

##camera.stop_preview()
