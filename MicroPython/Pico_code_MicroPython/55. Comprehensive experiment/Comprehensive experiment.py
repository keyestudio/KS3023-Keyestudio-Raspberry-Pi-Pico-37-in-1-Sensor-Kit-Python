'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 55
 * Comprehensive experiment
 * http://www.keyestudio.com
'''
from machine import Pin, PWM
import time
import random
import dht

pwm_r = PWM(Pin(2))
pwm_g = PWM(Pin(3))
pwm_b = PWM(Pin(4))

pwm_r.freq(1000)
pwm_g.freq(1000)
pwm_b.freq(1000)

pin = machine.Pin(19, machine.Pin.OUT, machine.Pin.PULL_DOWN)
xht = dht.DHT11(pin)

potentiometer = machine.ADC(28)
button = Pin(16, Pin.IN)
led = PWM(Pin(14))
led.freq(1000)
ird = Pin(11,Pin.IN)
B = machine.Pin(22, machine.Pin.IN)
X = machine.ADC(26)
Y = machine.ADC(27)
avoid = Pin(0, Pin.IN)
# 设置超声波引脚
trigger = Pin(6, Pin.OUT)
echo = Pin(7, Pin.IN)

def light(red, green, blue):
    pwm_r.duty_u16(red)
    pwm_g.duty_u16(green)
    pwm_b.duty_u16(blue)

act = {"1": "LLLLLLLLHHHHHHHHLHHLHLLLHLLHLHHH","2": "LLLLLLLLHHHHHHHHHLLHHLLLLHHLLHHH","3": "LLLLLLLLHHHHHHHHHLHHLLLLLHLLHHHH",
       "4": "LLLLLLLLHHHHHHHHLLHHLLLLHHLLHHHH","5": "LLLLLLLLHHHHHHHHLLLHHLLLHHHLLHHH","6": "LLLLLLLLHHHHHHHHLHHHHLHLHLLLLHLH",
       "7": "LLLLLLLLHHHHHHHHLLLHLLLLHHHLHHHH","8": "LLLLLLLLHHHHHHHHLLHHHLLLHHLLLHHH","9": "LLLLLLLLHHHHHHHHLHLHHLHLHLHLLHLH",
       "0": "LLLLLLLLHHHHHHHHLHLLHLHLHLHHLHLH","Up": "LLLLLLLLHHHHHHHHLHHLLLHLHLLHHHLH","Down": "LLLLLLLLHHHHHHHHHLHLHLLLLHLHLHHH",
       "Left": "LLLLLLLLHHHHHHHHLLHLLLHLHHLHHHLH","Right": "LLLLLLLLHHHHHHHHHHLLLLHLLLHHHHLH","Ok": "LLLLLLLLHHHHHHHHLLLLLLHLHHHHHHLH",
       "*": "LLLLLLLLHHHHHHHHLHLLLLHLHLHHHHLH","#": "LLLLLLLLHHHHHHHHLHLHLLHLHLHLHHLH"}

def read_ircode(ird):
    wait = 1
    complete = 0
    seq0 = []
    seq1 = []

    while wait == 1:
        if ird.value() == 0:
            wait = 0
    while wait == 0 and complete == 0:
        start = time.ticks_us()
        while ird.value() == 0:
            ms1 = time.ticks_us()
        diff = time.ticks_diff(ms1,start)
        seq0.append(diff)
        while ird.value() == 1 and complete == 0:
            ms2 = time.ticks_us()
            diff = time.ticks_diff(ms2,ms1)
            if diff > 10000:
                complete = 1
        seq1.append(diff)

    code = ""
    for val in seq1:
        if val < 2000:
            if val < 700:
                code += "L"
            else:
                code += "H"
    # print(code)
    command = ""
    for k,v in act.items():
        if code == v:
            command = k
    if command == "":
        command = code
    return command


# 超声波测距，单位：厘米
def getDistance(trigger, echo):
    # 产生10us的方波
    trigger.low()   #预先给出一个短的低电平，以确保一个干净的高脉冲:
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)#拉高电平後，等待10微秒后，立即设置为低电平
    trigger.low()
    
    while echo.value() == 0: #建立一个while循环检测回波引腳是否值為0，记录当时时间
        start = time.ticks_us()
    while echo.value() == 1: #建立一个while循环检测回波引腳是否值為1，记录当时时间
        end = time.ticks_us()
    d = (end - start) * 0.0343 / 2 #声波行進時間 x 声速(343.2 m/s，即每微秒0.0343公分)，來回距離再除以2
    return d


keys = 0
nums = 0
print(keys % 7)
def toggle_handle(pin):
    global keys
    keys += 1
    print(keys % 7)

button.irq(trigger = Pin.IRQ_FALLING, handler = toggle_handle)

def showRGB():
    R = random.randint(0,65535)
    G = random.randint(0,65535)
    B = random.randint(0,65535)
    light(R, G, B)
    time.sleep(0.3)

def showxht11():
    print("temperature：{} ℃  humidity：{} %".format(xht.temperature, xht.humidity))
    time.sleep(1)

def IRreceive():
    command = read_ircode(ird)
    print(command)

def showJoystick():
    B_value = B.value()
    X_value = X.read_u16()
    Y_value = Y.read_u16()
    print("button:", end = " ")
    print(B_value, end = " ")
    print("X:", end = " ")
    print(X_value, end = " ")
    print("Y:", end = " ")
    print(Y_value)
    time.sleep(0.1)

def adjustLight():
    pot_value = potentiometer.read_u16()
    print(pot_value)
    led.duty_u16(pot_value)
    time.sleep(0.1)

def showAvoid():
    if avoid.value() == 0:
        print("There are obstacles")
    else:
        print("All going well")
    time.sleep(0.1)

def showDistance():
    distance = getDistance(trigger, echo)
    print("The distance is ：{:.2f} cm".format(distance))
    time.sleep(0.1)

while True:
    nums = keys % 7  #按键次数对7取余,得到0 1 2 3 4 5 6 
    if nums == 0:  #显示RGB
        showRGB()
    elif nums == 1:  #显示红外接收的值
        IRreceive()
    elif nums == 2:  #显示温湿度
        showxht11()
    elif nums == 3:  #显示摇杆值
        showJoystick()
    elif nums == 4:  #电位器调节led
        adjustLight()
    elif nums == 5:  #显示障碍物信息
        showAvoid()
    elif nums == 6:  #显示超声波测距值
        showDistance()
