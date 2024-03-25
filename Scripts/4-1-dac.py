import RPi.GPIO as GPIO
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def bin2d(a):
    return[int(elem) for elem in bin(a)[2:].zfill(8)]
try:
    while True:
        a = int(input('Введите число от 0 до 255'))
        if a == 'q':
            break
        elif int(a) % 1 == 0 and a.isdigit() and 0<= int(a)<= 255:
            GPIO.output(dac, bin2d(int(a)))
            print(( '{:.4f}'.format(int(a) * 3.3 / 255 ))) 
exept ValueError:
    print('число от 0 до 255')  
   
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()