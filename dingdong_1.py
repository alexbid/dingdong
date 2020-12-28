
import RPi.GPIO as gpio
import time
from signal import signal, SIGINT
from sys import exit
 
def handler(signal_received, frame):
    # on gere un cleanup propre
    print('')
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    gpio.cleanup()
    exit(0)
 
def main():
    # on passe en mode BMC qui veut dire que nous allons utiliser directement
    # le numero GPIO plutot que la position physique sur la carte
    gpio.setmode(gpio.BCM)
 
    # defini le port GPIO 4 comme etant une sortie output
    gpio.setup(4, gpio.OUT)
 
    # Mise a 1 pendant 2 secondes puis 0 pendant 2 seconde
    while True:
        print("on")
        gpio.output(4, gpio.HIGH)
        time.sleep(0.2)
        print("off")
        gpio.output(4, gpio.LOW)
        time.sleep(2)
 
 
if __name__ == '__main__':
    # try
    signal(SIGINT, handler)
    main()
