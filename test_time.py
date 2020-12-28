#import GPIO library
import sys
import logging
import time

from datetime import datetime

now_all = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

prev = datetime.now()

#print "ding dong!!"
for i in range(4):
    current = datetime.now()
    print current.strftime("%d/%m/%Y %H:%M:%S")
    time.sleep(2)
    
    print (current-prev).total_seconds()

    prev = current 

        