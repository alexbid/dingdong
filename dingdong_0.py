#import GPIO library
import RPi.GPIO as GPIO

#set GPIO numbering mode and define input pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN)

try:
	while True:
		if GPIO.input(16)==0:
			pass
		else:
			print "ding dong!!"

finally:
	#cleanup the GPIO pins before ending
	GPIO.cleanup()
