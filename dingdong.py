#import GPIO library
import sys
import logging
import RPi.GPIO as GPIO
import time
from signal import signal, SIGINT
from sys import exit
from datetime import datetime

log_file = sys.argv[1]

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.OUT)

logging.basicConfig(filename=log_file, level=logging.INFO)

try:
    start_string = datetime.now()
    logging.info("ding dong ON at!!! " + start_string.strftime("%d/%m/%Y %H:%M:%S"))
    
    dingdong_sensi = 0
    prev = start_string

    while True:
        if GPIO.input(23)==0:
            pass
        else:
            current = datetime.now()
            if ((current-prev).total_seconds() > 3): dingdong_sensi = 0

            logging.info("ding dong signal at!!! %s - %s - sensi %s", current.strftime("%d/%m/%Y %H:%M:%S"), (current-prev).total_seconds(), dingdong_sensi)
            
            dingdong_sensi = dingdong_sensi + 1

            if (dingdong_sensi > 4) and ((current-prev).total_seconds() < 3):
                logging.info("ding dong!!! %s", current.strftime("%d/%m/%Y %H:%M:%S"))
                for i in range(2):
                    GPIO.output(4, GPIO.HIGH)
                    time.sleep(0.2)
                    GPIO.output(4, GPIO.LOW)
                    time.sleep(2)

                    dingdong_sensi = 0
                time.sleep(3)
            prev = current 

finally:
    #cleanup the GPIO pins before ending
    end_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    logging.info("ding dong OFF at!!! " + end_string)
    GPIO.cleanup()
