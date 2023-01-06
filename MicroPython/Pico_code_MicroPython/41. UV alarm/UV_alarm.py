'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 41
 * UV_alarm
 * http://www.keyestudio.com
'''
from machine import Pin
import time

buzzer = Pin(3, Pin.OUT)
sensor = machine.ADC(26)

while True:
    analogVal = sensor.read_u16()
    print(analogVal)
    if analogVal > 1000:
        buzzer.value(1)
    else:
        buzzer.value(0)
    time.sleep(0.5)