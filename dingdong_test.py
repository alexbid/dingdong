#import GPIO library
import RPi.GPIO as GPIO
import time
from signal import signal, SIGINT
from sys import exit

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
GPIO.setup(4, GPIO.OUT)

try:
    while True:
        if GPIO.input(23)==0:
            print 'pass'
        else:
            print "ding dong!!"
            

finally:
    #cleanup the GPIO pins before ending
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    GPIO.cleanup()
