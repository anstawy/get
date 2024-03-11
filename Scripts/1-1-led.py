import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(14, GPIO.IN)

GPIO.output(2, GPIO.input(14))
