'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 24
 * Gas sensor
 * http://www.keyestudio.com
'''
import machine
import utime

mq2_D = machine.Pin(22, machine.Pin.IN)
mq2_A = machine.ADC(26)

while True:
    digitalVal = mq2_D.value()
    analogVal = mq2_A.read_u16()
    print(digitalVal, end = "  ")
    print(analogVal, end = "  ")
    if digitalVal == 0:
        print("Exceeding")
    else:
        print("Normal")
    utime.sleep(0.1)
