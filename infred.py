import mraa
import time
import servo
import oled
import random

left = mraa.Gpio(73)
left.dir(mraa.DIR_IN)
right = mraa.Gpio(71)
right.dir(mraa.DIR_IN)
up = mraa.Gpio(60)
up.dir(mraa.DIR_IN)
x = mraa.Gpio(62)
x.dir(mraa.DIR_OUT)

def checkLeftright(degree):
    a = left.read()
    b = right.read()
    if a == 0 and degree < 135:
        degree += 45
        servo.ctrlLeftright(degree)
        oled.showFace(random.randint(0,3))
        time.sleep(0.2)
        return degree
    if b == 0 and degree > 45:
        degree -= 45
        servo.ctrlLeftright(degree)
        oled.showFace(random.randint(0,3))
        time.sleep(0.2)
        return degree
    return degree
	
def checkUpdown(status):
    c = up.read()
    if c == 0:
        servo.ctrlUpdown(60)
        status = 1 - status
        x.write(status)
        time.sleep(0.7)
        servo.ctrlUpdown(90)
        time.sleep(0.2)
    return status

if __name__ == '__main__':
    while(True):
        x.write(1)
        a = left.read()
        b = right.read()
        time.sleep(1)
        print (a,b)
        x.write(0)
        time.sleep(1)