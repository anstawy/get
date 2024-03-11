import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [ 0, 0, 0, 0, 0, 0, 1, 0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
for i in range(8):
    GPIO.output(dac[i], number[i])
time.sleep(15)

GPIO.output(dac, 0)
GPIO.output(number, 0)
GPIO.cleanup()