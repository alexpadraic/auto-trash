#!/usr/bin/env python

# import required libs and functions
import time
import RPi.GPIO as GPIO
from picamera import PiCamera
import os
import calendar
import datetime
from classify_image import run_inference_on_image
from class_list import class_dictionary

os.chdir('/home/pi/Pictures')
camera = PiCamera()

# Half-step sequence for smooth motion
seq = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
      ]

# Sets up the pins for each of the plates in the motor
StepPins = [17,18,21,22] # be sure you are setting pins accordingly GPIO17,GPIO18,GPIO21,GPI22


def predict_top_5(image_url):
    print("Predict top 5")
    return run_inference_on_image(image_url)


def top_prediction_tuple(predictions_list):
    return predictions_list[0]


def top_prediction_name(prediction):
    return prediction[0]


def top_prediction_number(prediction):
    return prediction[1]


def what_is_it(image_name):
    print "Setting variable for image filepath..."
    image_path = '/home/pi/Pictures/' + image_name

    print "Pulling-out the top 5 matched results..."
    top_5 = predict_top_5(image_path)

    print "Pulling-out the top class..."
    top = top_5[0]

    print "Pulling-out the top class name..."
    top_name = top[0]

    class_dictionary = class_dictionary();

    if class_dictionary[top_name] == 'c':
        return 'c'
    else:
        return 'r'


def ClickPicture():
    date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

    camera.resolution = (1024,768)
    camera.start_preview()

    time.sleep(0.5)

    image_name = date+'_'+'_img.jpg'
    print image_name

    camera.capture(image_name)
    camera.stop_preview()

    GPIO.cleanup()

    return image_name


def RunMotor():
  for i in range(512): # running motor (512) steps in one revolution
        for halfstep in range(8): # 8 steps in each cycle
            for pin in range(4): # 4 plates
                GPIO.output(StepPins[pin], seq[halfstep][pin]) # activate the pins
            time.sleep(0.001) # delay between each step


def SetPins():
    # Set all pins as output
    for pin in StepPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)


def CounterClockwise():
    GPIO.cleanup(); # cleaning up in case GPIOS have been preactivated
    GPIO.setmode(GPIO.BCM); # use BCM GPIO references instead of physical pin numbers
    SetPins(); # set all pins as output
    RunMotor(); # turns the motor 90 degrees
    GPIO.cleanup(); # cleaning up GPIOs


def ClockWise():
    seq.reverse() # reverse the sequence direction
    CounterClockwise() # calls the same function, just in reverse

def MasterFunction():

    print "HELLO - WELCOME TO CERBERUS"

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    i=GPIO.input(17)

    if i==0:
        print 'No Intruders'
        time.sleep(2)

    elif i==1:
        print 'Intruder Detected'

        image_name = ClickPicture();
        trash_type = what_is_it(image_name)
        print trash_type

        if trash_type == "r":
            ClockWise();
            time.sleep(1)
            CounterClockwise();
        else:
            CounterClockwise();
            time.sleep(1)
            ClockWise();

        del image_name


while True:
  MasterFunction()