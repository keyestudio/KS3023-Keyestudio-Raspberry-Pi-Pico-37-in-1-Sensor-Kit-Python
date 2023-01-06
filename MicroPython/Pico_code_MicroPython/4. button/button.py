'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 4
 * button
 * http://www.keyestudio.com
'''
from machine import Pin
import time

button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        print("You pressed the button!")   #按下则打印相应信息
    else:
        print("You loosen the button!")
    time.sleep(0.1) #延时0.1秒
