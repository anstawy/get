import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def bin2d(a):
    return[int(elem) for elem in bin(a)[2:].zfill(8)]
    
try:
    while True:
        T = float(input())
        for i in range(256):
            GPIO.output(dac, bin2d(i))
            time.sleep(T)
        for i in range(255, -1, -1):
            GPIO.output(dac, bin2d(i))
            time.sleep(T)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()