import RPi.GPIO as GPIO
import time 
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def bin2d(a):
    return[int(elem) for elem in bin(a)[2:].zfill(8)]


def adc():
    for value in range(256):
        GPIO.output(dac, bin2d(value))
        compValue = GPIO.input(comp)
        time.sleep(0.0007)
        if compValue == 1 and value!=0:
            return value
    
try:
    while True:
        i = adc()
        print(i, bin2d(i) , '{:.2f}'.format(i * 3.3 / 256))


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()