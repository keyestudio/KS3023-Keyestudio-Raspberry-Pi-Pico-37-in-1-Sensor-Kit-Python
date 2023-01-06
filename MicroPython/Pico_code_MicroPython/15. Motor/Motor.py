'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 15
 * 130-DC Motor
 * http://www.keyestudio.com
'''
from machine import Pin
import time

#电机的两个引脚
INA = Pin(14, Pin.OUT)
INB = Pin(15, Pin.OUT)

while True:
    #逆时针转2s
    INA.value(1)
    INB.value(0)
    time.sleep(2)
    #停止1s
    INA.value(0)
    INB.value(0)
    time.sleep(1)
    #顺时针转2s
    INA.value(0)
    INB.value(1)
    time.sleep(2)
    #停止1s
    INA.value(0)
    INB.value(0)
    time.sleep(1)