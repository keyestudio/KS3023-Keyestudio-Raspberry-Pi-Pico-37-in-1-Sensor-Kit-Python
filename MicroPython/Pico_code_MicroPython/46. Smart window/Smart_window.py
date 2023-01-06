'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 46
 * Smart_window
 * http://www.keyestudio.com
'''
import utime
from machine import Pin
from machine import PWM

pwm = PWM(Pin(9))#舵机引脚接GP9
pwm.freq(50)#20ms的周期，所以频率为50Hz
sensor = machine.ADC(26)#ADC0
'''
角度对应的占空比
0°----2.5%----1638
45°----5%----3276
90°----7.5%----4915
135°----10%----6553
180°----12.5%----8192
考虑到误差，将占空比定在1000~9000，这样可以顺利转动0~180度
'''
angle_0 = 1638
angle_90 = 4915
angle_180 = 8192
    
while True:
    value = sensor.read_u16()
    print(value)
    if value > 2000:
        pwm.duty_u16(angle_0)
        utime.sleep(0.5)
    else:
        pwm.duty_u16(angle_180)
        utime.sleep(0.5)

    