'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 7
 * Line Tracking sensor
 * http://www.keyestudio.com
'''
from machine import Pin
import time

sensor = Pin(3, Pin.IN, Pin.PULL_UP)

while True:
    if sensor.value() == 0:
        print("0   White")   #按下则打印相应信息
    else:
        print("1   Black")
    time.sleep(0.1) #延时0.1秒
