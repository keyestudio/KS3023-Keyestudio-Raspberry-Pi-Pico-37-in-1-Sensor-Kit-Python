'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 3
 * Laser
 * http://www.keyestudio.com
'''
from machine import Pin
import time

laser = Pin(2, Pin.OUT)# 构建激光对象,激光与引脚0相连，并设置引脚2为输出模式
while True:
    laser.value(1)# 激光点亮
    time.sleep(2)# 等待2秒
    laser.value(0)# 激光熄灭
    time.sleep(2)# 等待2秒