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
    value = 0
    for i in range(7, -1, -1):
        value += 2**i
        GPIO.output(dac, bin2d(value))
        time.sleep(0.007)
        if GPIO.input(comp) == 1:
            value -= 2**i
    return value
    
try:
    while True:
        i = adc()
        print(i, bin2d(i) , '{:.2f}'.format(i * 3.3 / 256))


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()