'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 48
 * Flame_alarm
 * http://www.keyestudio.com
'''
from machine import Pin
import time

buzzer = Pin(3, Pin.OUT)
sensor = Pin(22, Pin.IN)

while True:
    analogVal = sensor.value()
    print(analogVal)
    if analogVal == 0:
        buzzer.value(1)
    else:
        buzzer.value(0)
    time.sleep(0.5)