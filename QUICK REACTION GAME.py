#Import Stuff
import RPi.GPIO as gpio #GPIO Library
import time #For timing

gpio.setmode(GPIO.BCM)
gpio.setwarnings(False)

#Variables
winner_led1 = 4

#Setup gipo

gpio.setup(winner_led1, gpio.OUT)
