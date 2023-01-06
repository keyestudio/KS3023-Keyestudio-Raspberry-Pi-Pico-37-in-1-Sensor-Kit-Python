'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 26
 * UV_sensor
 * http://www.keyestudio.com
'''
import machine
import utime

led = machine.Pin(27, machine.Pin.OUT)
sensor = machine.ADC(26)
led.value(1)#点亮LED

while True:
    analogVal = sensor.read_u16()
    print(analogVal)
    utime.sleep(0.1)
