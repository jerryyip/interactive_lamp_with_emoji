import time
import pyupm_servo as servo

s1 = servo.ES08A(13)
s2 = servo.ES08A(19)

def ctrlLeftright(drgee):
    s1.setAngle(drgee)
    return 0

def ctrlUpdown(drgee):
    s2.setAngle(drgee)
    return 0

if __name__ == '__main__':
    a = input("drgee1")
    s1.setAngle(a)
    b = input("drgee2")
    s2.setAngle(b)
	time.sleep(1)