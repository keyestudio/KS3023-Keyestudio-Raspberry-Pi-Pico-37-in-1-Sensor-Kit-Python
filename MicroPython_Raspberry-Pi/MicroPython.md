# **MicroPython_Tutorial(Raspberry Pi)**

## 1. Preparations

### 1.1. Tools needed for the Raspberry Pi system

**Hardware Tool:**

- Raspberry Pi 4B/3B/2B

- Above 16G TFT Memory Card

- Card Reader

- Computer and other parts

#### 1.1.1. Install Software Tools

**Windows System:**

**Putty**

Download link: [https://www.chiark.greenend.org.uk/~sgtatham/putty/](https://www.chiark.greenend.org.uk/~sgtatham/putty/)

![](./media/c26be4cd1f5543f20f275556ce5892c0.png)

![](./media/d888918aa7bf9e5ea94597aad1ee4224.png)



1.  After downloading the package file ![](./media/e597704d7033c7c3c5da06d4f561822c.png), double-click it and tap “Next”.

![](./media/01f1b2d98915be2be9c0c2a3d330dde2.png)

2.  Click “Next”.

![](./media/bd698753a8eea7a2ff5c5e0e598cbd94.png)

3.  Choose“Install PuTTY files”and click“Install”.

![](./media/071a0acc98bb2dc5cd45d85dec72d111.png)

4.  After a few seconds, click "Finish".

![](./media/ec368c3a549c09edd70f9786456d5430.png)

**SSH Remote Login software -WinSCP**

Link of Download:[https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

1.  After downloading the package file![](./media/1719daa1002d7477ad4700e1df85d2df.png), click
![](./media/e09e48a32781d08aabb06156efe1de49.png).

![](./media/5ee80ade909fe3eb73dc9535704b4c0b.png)

2.  Click “Accept”.

![](./media/9c652f54f6a7d53f6b2aedba40104a00.png)

![](./media/f32891714d5966037d59d1812aa15686.png)

![](./media/57d6139ba0aac9ca996bcbe6f6fd218f.png)

![](./media/49ffed878ee84546b156af3a0bf5556e.png)

![](./media/14ffa1e11243835d30ffb933219dcef5.png)

**SD Card Formatter**  

Format TFT card tool

Download SD Card Formatter ：
[http://www.canadiancontent.net/tech/download/SD_Card_Formatter.html](http://www.canadiancontent.net/tech/download/SD_Card_Formatter.html)

![](./media/fa229f4e063572ce1c59574c308bf452.png)

![](./media/ac5d5eb9463805484b9239b99faf04eb.png)

1.  Unzip the SDCardFormatterv5\_WinEN package, double-click ![](./media/8c6f8da97bf702080a8e302db2e9f982.png) to run it.

![](./media/046c67e4072093ee3dad27e8088fcf9f.png)

2.  Click“Next”and choose ![](./media/13dc08ae2b5cb52ae3d7ea198134d778.png), then tap“Next”.

![](./media/384203e0b54ddfe37f18b65f70e786e5.png)

![](./media/cf4e91eac0c0573cff282256a915a01a.png)

3.  Click“Next”and“Install”.

![](./media/0af58ee3afb14005a884ca2dc941157f.png)

![](./media/807623ddeea20c8b61503845d8aec9bc.png)

4.  After a few seconds, click "Finish".

![](./media/df2deb7e04c25ee207e994f0d2808194.png)

**Win32DiskImager**

Download link: [https://sourceforge.net/projects/win32diskimager/](https://sourceforge.net/projects/win32diskimager/)

![](./media/4ffb55fd466198ca9524afbde7806271.png)a. After the download, double-click and tap “Run”.

![](./media/0f86f055a814207b0b09e1a7e6cb20bc.png)

Select ![](./media/5cdab33a0a7ddd4ab5b2ca8cb04670be.png) and click“Next”.

![](./media/d70ecd0554cbdbd60997a2356b55dc0d.png)

Click“Browse...”and find out the folder where the Win32DiskImager is located, tap“Next”.

![](./media/1cdc2638bc1e9fe214344429f5e97a13.png)

![](./media/cc7949bb335b75000e77b18c85e4e07b.png)

Tick ![](./media/99d088dd3f9e62d94fe8d56bd4638d1d.png) and click “Next”and“Install”.

![](./media/c03510a9961a0e7307945dff10de3550.png)

![](./media/0c9c0d647479ee984fc29c3cedc72c79.png)

Click “Finish” after the installation is complete.

![](./media/1d75c6dd9ea4a2c437a2b655b713a1db.png)

**WNetWatcher**

Download：[http://www.nirsoft.net/utils/wnetwatcher.zip](http://www.nirsoft.net/utils/wnetwatcher.zip)


#### 1.1.2. Raspberry Pi Imager

Download link for the latest version:

[https://www.raspberrypi.org/downloads/raspberry-pi-os/](https://www.raspberrypi.org/downloads/raspberry-pi-os/)

Old version：

- > Raspbian：[https://downloads.raspberrypi.org/raspbian/images/](https://downloads.raspberrypi.org/raspbian/images/)

- > Raspbian full：[https://downloads.raspberrypi.org/raspbian\_full/images/](https://downloads.raspberrypi.org/raspbian\_full/images/)

- > Raspbian lite：[https://downloads.raspberrypi.org/raspbian\_lite/images/](https://downloads.raspberrypi.org/raspbian\_lite/images/)

We use the 2020.08.20 version in the tutorial and recommend you to use this version.

(<span style="color: rgb(255, 76, 65);">Please download this version as shown in the picture below.</span>)

![](./media/3e0526d601054847d1b1feee8384dbbe.png)

### 1.2. Install Raspberry Pi OS on Raspberry Pi

#### (1) Interface the TFT memory card with a card reader, then plug the card reader into a computer’s USB port.
![Img](./media/img-20231011081236.jpg)

#### (2) Use the SD Card Formatter to format a TFT memory card, as illustrated below.

![](./media/79d747e6f00f857a593b3327397cc44f.png)

![](./media/cbc55902de71ce984d873ca2cb67fffa.png)

![](./media/82031b5354cc4edeccf2bfa7465b7c6c.png)

#### (3) Burn system

Burn the Raspberry Pi OS to the TFT memory card using Win32DiskImager software.

![](./media/80d236cae8bdf63d80dc65048ffb52b3.png)

![](./media/243d1ef34211eafe1a92b67fc0ee85a2.png)

![](./media/ea854c476e9a8d4f82dd4a7c714cd5af.png)

Don’t eject card reader after burning mirror system, build a file named SSH, then delete <span style="color: rgb(255, 76, 65);">.txt</span> .

The SSH login function can be activated by copying SSH file to boot category, as shown below.

![](./media/ffb73310322accd671da373bb2e71945.png)Eject card reader.

#### (4) Log in system

(<span style="color: rgb(255, 76, 65);">Raspberry and PC should be in the same local area network.</span>)

1). Insert TFT memory card into Raspberry Pi, connect internet cable and plug in power. If you have screen and HDMI cable of Raspberry Pi, you could view Raspberry Pi OS activating. If not, you can enter the desktop of Raspberry Pi via SSH remote login software---WinSCP and xrdp.
![Img](./media/img-20231011100206.png)

2). Use the WNetWatcher software to find the IP address of the Raspberry Pi.
![Img](./media/img-20231007165908.png)

If there is no IP address as shown in the figure above, follow the following steps to set it.
![Img](./media/img-20231007165912.png)
![Img](./media/img-20231007165916.png)

Once the setup is complete, record the IP and MAC addresses of the Raspberry Pi. As shown in the red box below, the MAC address of the Raspberry Pi is <span style="color: rgb(255, 76, 65);">b8:27:eb:17:16:01</span>, and the ip address is <span style="color: rgb(255, 76, 65);">192.168.0.57</span>. 
![Img](./media/img-20231007165925.png)

If you do not know the mac address and the ip address of the Raspberry Pi, then unplug the network cable of the Raspberry PI first, open the **WNetWatcher** query, and the detection times will be displayed on the right side of the interface. Connect the Raspberry Pi cable and query it once using **WNetWatcher**, and the Raspberry Pi address is detected one less time than the other addresses. Then write down the ip and mac addresses.

#### (5) Remote login

**Enter default user name, password and host name on WinSCP to log in. Only a Raspberry Pi is connected in same network.**

![](./media/0a41d5c629ec98afbc31dc47ff5c18ec.png)

![](./media/ff64e71b9e30df60d0b099dbc2532587.png)
![Img](./media/img-20231007170058.png)
![Img](./media/img-20231007170103.png)

#### (6) Check IP and mac address

![](./media/a4285a452978026c9e60c31d35974315.png)

Click to open terminal and input the password: <span style="color: rgb(255, 76, 65);">raspberry</span>, and press“**Enter**” on keyboard.

![](./media/a433a9ee584c821a702d0250937e2ba8.png)

![](./media/7fb10d842cc7fd824a325d30fc3ecdc7.png)

Logging in successfully, open the terminal, input <span style="color: rgb(255, 76, 65);">**ip a**</span> and tap“**Enter**”to check IP and mac address.

![](./media/132e9ab754a0f63e38b3e4cfbc3679f2.png)


#### (7) Fix IP address of Raspberry Pi

IP address is changeable, therefore, we need to make IP address fixed for convenient use.

**Follow the below steps:**

Switch to root user

If without root user’s password

① Set root password

Input password in the terminal: <span style="color: rgb(255, 76, 65);">sudo passwd root</span> to set password.

② Switch to root user

<span style="color: rgb(255, 76, 65);">su root</span>

③ Fix the configuration file of IP address

Firstly change IP address of the following configuration file.

(<span style="color: rgb(255, 76, 65);">\#New IP address: address 192.168.0.57</span>)

Copy the above new address to terminal and press“Enter”.

Configuration File:

```c
echo -e '

auto eth0

iface eth0 inet static

\#Change IP address

address 192.168.0.57

netmask 255.255.255.0

gateway 192.168.1.1

network 192.168.1.0

broadcast 192.168.1.255

dns-domain 119.29.29.29

dns-nameservers 119.29.29.29

metric 0

mtu 1492

'\>/etc/network/interfaces.d/eth0
```

As shown below:

![](./media/a68a4f59d4d364efa28b6680a2c48d43.png)

④ Reboot the system to activate the configuration file.

Input the restart command in the terminal: <span style="color: rgb(255, 76, 65);">sudo reboot</span>

You could log in via fixed IP afterwards.

⑤ Check IP and insure IP address fixed well.

![](./media/b4313e2d78a4289705c658a1ebbc962b.png)

#### (8) Log in desktop on Raspberry Pi wirelessly

In fact, we can log in desktop on Raspberry Pi wirelessly even without screen and HDMI cable.

VNC and Xrdp are commonly used to log in desktop of Raspberry Pi wirelessly. Let’s take example of Xrdp.

**Install Xrdp Service in the terminal**

Installation commands:

Switch to Root User: <span style="color: rgb(255, 76, 65);">su root</span>

Installation: <span style="color: rgb(255, 76, 65);">apt-get install xrdp</span>

Enter <span style="color: rgb(255, 76, 65);">y</span> and press“**Enter**”.

As shown below:

![](./media/aa59941ff4c1e582e8183c1dc3767fce.png)

Open the remote desktop connection on Windows

Press WIN+R on keyboard and enter <span style="color: rgb(255, 76, 65);">mstsc.exe</span>.

As shown below:

![](./media/e5a66a3a1c998f8feb1c21c7a457ec4e.png)

Input IP address of Raspberry Pi, as shown below.

Click“**Connect**”and tap“**Connect**”.

**192.168.0.57** is IP address we use, you could change into your IP address.

![Img](./media/img-20231007172853.png)

Click“Yes”.

![](./media/297813f1370ce5c158fac61511f61295.png)

Input user name: <span style="color: rgb(255, 76, 65);">pi</span>, default password: <span style="color: rgb(255, 76, 65);">raspberry</span>, as shown below.

![](./media/251fddc1decc15d0b69f8a0c7467d5c1.png)

Click“OK”or“Enter”, you will view the desktop of Raspberry Pi OS, as shown below.

![](./media/56bd5693edd484c4433dc438b58c6130.png)

Now, we finish the basic configuration of Raspberry Pi OS.


### 1.3. Using MicroPython

MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments. MicroPython is packed full of advanced features such as an interactive prompt, arbitrary precision integers, closures, list comprehension, generators, exception handling and more. Yet it is compact enough to fit and run within just 256k of code space and 16k of RAM. MicroPython aims to be as compatible with normal Python as possible to allow you to transfer code with ease from the desktop to a microcontroller or embedded system.

For more information, please go to the official website: [https://micropython.org/](https://micropython.org/)

**Programming the Pico:** You could use C/C++ or MicroPython. MicroPython is an interpreted language that is made specifically for microcontrollers. Many microcontroller users have familiarity with C/C++ as they are used on the Arduino and ESP32 boards. In this tutorial, we will use Thonny recommended by Raspberry Pi. Thonny bills itself as a “Python IDE for Beginners”, and it is available for Windows, Mac OSX and Linux. It was also part of the Raspberry Pi operating system(formerly Raspbian).

**Boot and Install MicroPython:** The first thing that we need to do is to get MicroPython installed onto the Pico.

**Download and burn firmware**

Go to the official website to download the UF2 file:

[https://www.raspberrypi.com/documentation/microcontrollers/\#getting-started-with-micropython](https://www.raspberrypi.com/documentation/microcontrollers/#getting-started-with-micropython)

What I downloaded is![](./media/b9acf3a180cc573115d6956dd97473a6.png). Once the download is complete, we proceed to burn the firmware.

With BOOTSEL held down, then plug the Pico into Raspberry Pi or your computer’s USB port.

Release it after the connection was finished. You should see a drive appearing on your computer with the name“RPI-RP2”.

![](./media/fea09bd325ab8872862583c0898cefb9.png)

Move the UF2 file into“RPI-RP2”, and the Raspberry Pi Pico will automatically restart. At this point, the burning is complete.

![](./media/2b92b23b34ad785e441050dda48f4cd1.png)

**Connect the Pico from a Raspberry Pi over USB**

The MicroPython firmware is equipped with a virtual USB serial port which is accessed through the micro USB connector on Raspberry Pi Pico. Your computer should notice this serial port and list it as a character device, most likely <span style="color: rgb(255, 76, 65);">/dev/ttyACM0</span>.

You can run <span style="color: rgb(255, 76, 65);">ls /dev/tty\*</span> to list your serial ports. There may be quite a few, but MicroPython’s USB serial will start with <span style="color: rgb(255, 76, 65);">/dev/ttyACM</span>. If in doubt, unplug the micro USB connector and see which one disappears. If you don’t see anything, you can try rebooting your Raspberry Pi.

Enter the following command to install minicom:

sudo apt install minicom

![](./media/446a7c06287ab5dad20b372e7b4fb409.png)

open it as such:

minicom -o -D /dev/ttyACM0

![](./media/ffbca82d2585a6c716390e05e8d6efba.png)

Press Ctrl + B.

![](./media/4ce46e1813574740300c02558d3b6a78.png)

Enter print("hello world"), it will show“hello world”.

![](./media/2af344f21b35759955c8e1ed469d897f.png)

The on-board LED on Raspberry Pi Pico is connected to GPIO pin 25. The machine module is used to control on-chip hardware. This is standard on all MicroPython ports. Here we are using it to take control of a GPIO, so we can drive it high and low. If you type this in to light up the LED.

```Python
from machine import Pin

led = Pin(25, Pin.OUT)

led.value(1)
```
![](./media/fe8f847fa40eacf2bcd8f24cc9d7b5db.png)

You can turn the LED off with:

led.value(0)

![](./media/0cb1575e8cb7c0a95e0f08c305905335.png)

Now we have successfully connected the Pico from a Raspberry Pi over USB.

**Install Thonny**

The Raspberry Pi Imager that we downloaded comes with some commonly used software, and Thonny is among them.

![](./media/3ca36d4733dbbbb82d82572c24c7d63d.png)

If the Raspberry Pi Imager does not have Thonny, you need to manually download it yourself. Enter the following command in the terminal to download and install Thonny.

<span style="color: rgb(0, 209, 0);">sudo apt install thonny</span>
<br>
<br>

When opening Thonny for the first time select "<span style="color: rgb(255, 76, 65);">Standard Mode</span>" in the top right of the window. Open Thonny again, the interface is shown in the figure below.

![](./media/a8bcc7174c4dba688f1336f215e7b34a.png)

Select "<span style="color: rgb(255, 76, 65);">MicroPython (Raspberry Pi Pico)</span>" from the list, as shown below.

![](./media/336ca9ecc12b7a07f37cff36491253d4.png)

Click “<span style="color: rgb(255, 76, 65);">Tools</span>” and “<span style="color: rgb(255, 76, 65);">Options</span>”.

![](./media/7abc24e9a41c82fce2b40dfb965fc97c.png)

Select <span style="color: rgb(255, 76, 65);">MicroPython(Raspberry Pi Pico)</span> and the <span style="color: rgb(255, 76, 65);">Port</span> as shown below.

![](./media/c2072789c815d381d97fbdfe998c7606.png)

![](./media/391bc339a8408c995418d51b52106f51.png)

Or select <span style="color: rgb(255, 76, 65);">MicroPython (generic)</span>：

![](./media/dbe48b9675eddfd7734762cd9ba64fbc.png)

![](./media/94e9cb956adbe4aa4de09b5c36634a36.png)

Click “Ok”.

**Thonny User Interface**

Now we will introduce Thonny user interface. At the top is the main menu, there are“File”,“Edit”,“View”,“Run”,“Tools”and“Help”.

![](./media/d81465d9c7706b05fb3e88133e4a583c.png)

Click“File”, it shows some operations related to files.

![](./media/5e4f37a816a51859152e04054aa68d3e.png)

Click“Edit”, these are some options about code, such as copying, cutting, pasting.

![](./media/4664d6d018c346bae517ab7c53236edf.png)

In the View drop-down menu, these are tools to assist you. For example, if we do not tick Shell (the Shell is the“command line”of the Pico, and you can execute code directly here.), the result won’t be displayed. Click “Files”, the files we saved will be shown on the left.

![](./media/096012bd728ecc7f3b83a476eaaae88e.png)

We can select interpreter in the "Run" drop-down menu, there are also some shortcuts used in programming.

![](./media/b1009509de595def420463a8a75614be.png)

In "Tools" menu, we can select interpreter, font and import modules, etc.

![](./media/9166ea3917cb99210c6d8836498d4922.png)

![](./media/de527c958196751da2e0f7a71c22e0bc.png)

In Help menu, we will see“Help contents”,“Version history”and more.

The icons below the main menu are our commonly used tool shortcuts.

![](./media/66b40a6a5c2d65fec40db9f4e8163ace.jpeg)

When we open or save files, it will shows the following contents.

![](./media/e1620ada69e63235e5137bad72301dbf.png)

<span style="color: rgb(255, 76, 65);">Note:</span> if we select“MicroPython(generic)”, then“MicroPython Device”will be displayed.

![](./media/85ae2ed55edaad8c13e4517d6a1d962d.png)

We can open programs saved on the Raspberry Pi or the Pico, or save them on This computer or Raspberry Pi Pico.

Copy the code below to the Thonny and save it to the Pico as **test\.py**.

```Python
from machine import Pin, Timer

led = Pin(25, Pin.OUT)

tim = Timer()

def tick(timer):

global led

led.toggle()

tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
```

![](./media/6723d4e2dd2ca7b17740430bf6585ea4.png)

Click ![](./media/5df8ee106f3f7e2a3cab589ccac6934b.png) to run the code, the on-board LED will blink, then click ![](./media/ebb4ab42307b2b2d84cf6fa2dd971fd6.png) to stop, the LED won’t blink. If we unplug the MicroUSB cable and plug it in again, the LED won’t blink after powering up. This is because we did not name the file main\.py and save it to the Pico. Click“File”, then click“Save as...”to choose Raspberry Pi Pico. After that, enter main\.py as the file name(don’t forget to enter the .py file extension) and click“OK”. Run the code again, the LED will continue to blink.

![](./media/df73855c0dd7f29cc4fc4dabe5ed1147.png)

When we unplug the cable again, then plug it in and power on, the LED will blink. This is because the Raspberry Pi Pico starts running the program saved on main\.py after powering up.

**Add Modules(Libraries)**

Python is a powerful language due to its modules. Python scripting language with the most rich and powerful class library, enough to  support the vast majority of day-to-day applications. By importing modules, this makes it easier for us when using some complex sensors.

The method is simple, just save the module that we need to the Pico, or open the file saved on our computer, click“File” to choose “Save as”, then save it to the Pico board (right click the mouse, you can delete files). For instance, I saved some library files required for these courses on my Pico. Click“View”to choose“Files”, they will be displayed on the left of the interface.

![](./media/82923d59e018fd32c1c2836a3c0b470a.png)

When using sensors, we can import the corresponding modules directly.

![](./media/2d5a05351f23a99bddb011d6186c685a.png)

We save all the code in this tutorial to the Raspberry Pi. Open the terminal and create a folder in <span style="color: rgb(0, 209, 0);">**/home/pi**</span>.

![](./media/19c626dbfa3928bb73e86e3f5f67f8af.png)

Copy the code to the folder and enter ls, it will show the following content.

![](./media/6271e5c2593ad77d2575bbfc6953c80a.png)

When using Thonny, we open this path to find the code we saved directly.

![](./media/6653914827d24ee8e7b5138ad6f68f1a.png)

### 1.4. Keyestudio Raspberry Pico IO Shield

#### (1) Overview

The Keyestudio Raspberry Pico IO shield is designed for Raspberry Pi Pico. No soldering required. To make the connection easier, the interfaces on the shield have silkscreen labels.The silkscreen labels of the 3pin interface generally are G, V, S. On the shield, G represents GND, V represents the VCC interface (3.3V), and S represents digital ports or analog ports. The pitch of the pin header on the shield is 2.54mm. The sequence of the pin header is the same as the Pico board’s when wiring. The shield also comes with a reset button, a PWR power indicator and four holes.

The shield offers a variety of communication interfaces including I2C, UART, SPI, analog IO and digital IO, and provides an interface of power supply ranging from 6.5V to 12V.

#### (2) Specifications:

Output current: ≦500mA

DC input voltage: 6.5 - 12V

Output voltage: DC 3.3V/5V

Ambient temperature(recommended): -10°C \~ 50°C

Dimensions: 45.339MM \*83.617MM

Pin pitch: 2.54mm

#### (3) Schematic diagram

![](./media/ce7c33ca7cceb48d25e86c6ef34bdd5e.png)

#### (4) Pinout

![](./media/5fcf607da671e653f78e4ea67db3aa52.jpeg)

#### (5) Connection

As shown below, stack the Raspberry Pi Pico board onto the Raspberry Pi Pico shield.

![](./media/027bcb15b34415d54164c03a796a10ab.jpeg)

## 2. Basic Projects

There are 37 sensors and modules in this kit. Next, we will analyze and introduce how they work step by step. Interface sensors with the Raspberry Pi Pico board and the Pico shield, run test codes and observe experimental phenomenon.

**<span style="color: rgb(255, 76, 65);">Note:</span> please wire up components according to the given connection diagrams.**

### Project 1: Lighting up LED

![](./media/ce8d61c97eb89c94c05cc1f6299316b5.jpeg)

**1. Overview**

In this project, we will make an experiment to light up the white LED module. The high and low levels can be controlled by programming, then the state of the LED can be controlled.

**2. Working Principle**

The two circuit diagrams are given. The left one is wrong wiring-up diagram. Why? Theoretically, when the S terminal outputs high levels, LED will receive the voltage and light up.

Due to limitation of IO ports of Pico board, weak current can’t make LED brighten.

The right one is correct wiring-up diagram. GND and VCC are powered up. When the S terminal is a high level, the triode Q1 will be connected and LED will light up(note: current passes through LED and R3 to reach GND by VCC not IO ports). Conversely, when the S terminal is a low level, the triode Q1 will be disconnected and LED will go off.

The triode Q1 is equal to a switch and R1 and R3 stand for limited resistors which can curb the size of current to prevent from burning out components.

![](./media/02b87e0da508ebe73b0b43533ab78b69.png)
![](./media/1bfd37f6a9dc54da35df36c8f7d37e64.jpeg)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.16111in;height:0.45972in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.39375in;height:0.76042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/12ecb079cf6481a6f0f04d6b7bb31fd8.png" style="width:1.20417in;height:0.93889in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.88056in;height:0.32083in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.83611in;height:0.44792in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio Purple LED Module*1</td>
<td>3P Dupont Wire*1</td>
<td><p>Micro</p>
<p>USB Cable*1</p></td>
</tr>
</tbody>
</table>

(<span style="color: rgb(255, 76, 65);">Note:</span> in all experiments, the microUSB cable is connected to the pico via a Raspberry Pi, and the 3p Dupont wire is torn from a 40P Dupont wire.)

<br>
<br>


**4. Wiring Diagram**

![](./media/f1421990330a20cbc6a846511ec0a916.png)

**5. Run the test code**

After opening Thonny and connecting to the Pico, click“View” and “Files”, then the code saved on the Raspberry Pi and the Pico will be shown on the left side.

![](./media/1fcf94991854f44fe0d6037b1e60e751.png)

We have saved the code on the Raspberry Pi earlier. Find and click LED\.py and Bink\.py. Next, click ![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the code. If it did not work, try clicking ![](./media/03c901befd9389c4369699ad93c1aeef.png) to stop running, then run the code again. You also can press the reset button on the Pico shield and click ![](./media/03c901befd9389c4369699ad93c1aeef.png) to run it again.

![](./media/668ba35c4cf06ea9d8e082365144f1ef.png)

**6. Code Explanation**

**Machine** module is indispensable, we will use **import machine** or **from machine import...** to program pico with microPython.

**time.sleep()** function is used to set delayed time, as
**time.sleep(0.01)**, which means, the delayed time is 10ms.

**led = Pin(0, Pin.OUT)**, created a pin example and we name **led**.

**0** is indicative of connected pin GP0, **Pin.OUT** represents output mode, can use **.value()** to output high levels (3.3V) **led.value(1)**
or low levels (0V) **led.value(0)**.

**import machine** is used to import modules. When creating pins examples, it will change into **led = machine.Pin(0, machine.Pin.OUT)**.

**while True** is loop function, it means that sentences under this function will loop unless **True** changes into **False.** For the
function **while**, **led.value(1)**, outputs high levels to the pin 0; then LED lights up. Then the delayed function **time.sleep(1)** will
wait for 1s. When **led.value(0)** output low levels to the pin 0, the LED will go off，and the function **time.sleep(1)** will wait for 1s,
cyclically, and LED will flash.

**7. Test Result**

Code 1: upload the code and power on, the purple LED on the module will light up.

Code 2: upload the code and power on, the purple LED will flash with the interval of 1s.

![](./media/a48e818367414fa963e18e8ecc1ae08b.jpeg)

<span style="color: rgb(255, 76, 65);">Note:</span> press ![](./media/03c901befd9389c4369699ad93c1aeef.png) to stop running.
<br>
<br>

**8. Test Code**

Test Code1:

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 1.1
 * turn on led
 * http://www.keyestudio.com
'''
from machine import Pin

led = Pin(0, Pin.OUT)# Define led, and connect LED to pin 0, set pin 0 to output mode

led.value(1)# Light up at high level  
```    


Test Code2:

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 1.2
 * Blink
 * http://www.keyestudio.com
'''
from machine import Pin
import time

led = Pin(0, Pin.OUT)# Define led, and connect LED to pin 0, set pin 0 to output mode
while True:
    led.value(1)# light up led
    time.sleep(1)# delay 1s
    led.value(0)# turn off led
    time.sleep(1)# delay 1s
```
### Project 2: Traffic Lights Module

![](./media/e191c790f251715b418bcfd39a32917f.jpeg)

**1. Overview**

In this lesson, we will learn how to control multiple LED lights and simulate the operation of traffic lights.

Traffic lights are signal devices positioned at road intersections, pedestrian crossings, and other locations to control flows of traffic.

In this kit, we will use the traffic lights module to simulate the traffic lights.

**2. Working Principle**

In previous lesson, we already know how to control an LED. In this part, we only need to control three separated LEDs. Output high levels to the signal R(3.3V), then the red LED will be on.

![](./media/1479f32d51a02c2230cb535197093d4c.png)


**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:0.98958in;height:0.39167in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.19931in;height:0.65486in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/6ff6e93b37472de2695aefed0939a14e.png" style="width:1.25833in;height:0.71736in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/fc3fd9c0110b04d1af77a2ff8c01a10a.png" style="width:0.95208in;height:0.39931in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.02917in;height:0.55139in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio Traffic Lights Module*1</td>
<td>5P Dupont Wire*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/9f7d4dcfe9b1a7a708f1d7bb008588bc.png)

**5. Run the test code**

Find and double-click **Traffic\_Light.py** to open it, then click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the code.

![](./media/26de880d80116e0086c3be3c6b8fc656.png)

**6. Code Explanation**

Create pins, set pins mode and delayed functions.

We use the **for** loop.

The simplest form is **for i in range()**.

In the code, we used range(3), which means the variable i starts from 0, increase 1 for each time, to 2.

**7. Test Result**

Run the code, the green LED will be on for 5s then off, the yellow LED will flash for 3s then go off and the red one will be on for 5s then off.

![](./media/4d677447ff2a0620da5f5d30f54fa355.jpeg)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 2
 * Traffic_Light
 * http://www.keyestudio.com
'''
import machine
import time

led_red = machine.Pin(14, machine.Pin.OUT)
led_amber = machine.Pin(13, machine.Pin.OUT)
led_green = machine.Pin(12, machine.Pin.OUT)

while True:
    led_green.value(1) # green led will be on for 5s
    time.sleep(5)# 5s later
    led_green.value(0)# green led will be off
    for i in range(3):#yellow led flashes for three times
        led_amber.value(1)
        time.sleep(0.5)
        led_amber.value(0)
        time.sleep(0.5)
    led_red.value(1) # red led will be on for 5s
    time.sleep(5)
    led_red.value(0)
```
### Project 3: Laser Sensor

![](./media/d5d84e9d26d2cc89772a05eed6340bc0.jpeg)

**1. Description**

Lasers are widely used to cut, weld, surface treat, and more on specific materials. The energy of the laser is very high. The toy laser pointer may cause glare to the human eye, and it may cause retinal damage for a long time. my country also prohibits the use of laser to illuminate the aircraft.

**2. Working Principle**

The laser head sensor module is mainly composed of a laser head with a light-emitting die, a condenser lens, and a copper adjustable sleeve.

We can see the circuit schematic diagram of this module which is very similar to the LED we have learned. They are all driven by triodes. A high-level digital signal is directly input at the signal end, then the sensor will start to work; if inputting low levels, the sensor won’t work.

<span style="color: rgb(255, 76, 65);">Note:</span> don’t point an laser emitter at eyes of people.

<br>
<br>

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.16111in;height:0.45972in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.39375in;height:0.76042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/88abe96ca71fe1b89b23d92c890650ee.png" style="width:1.07708in;height:0.70833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.88056in;height:0.32083in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.83611in;height:0.44792in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio DIY Laser Module*1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Connection Diagram**

![](./media/56a32f3859169de574822242faad6630.png)

**5. Run the test code**

Find **Laser\.py**, then double-click the code and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/817fbff98599647ec66ff28d8fba5d48.png)

**6. Test Result**

Upload the test code and power up, the laser tube on the module emits a red laser signal for 2 seconds, and stops emitting a red laser signal for 2 seconds.

![](./media/c1e4370566b5843eaa59c1179a411133.jpeg)

**7. Test code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 3
 * Laser
 * http://www.keyestudio.com
'''
from machine import Pin
import time

laser = Pin(2, Pin.OUT)# define laser, connect the laser module to pin 2 and set the pin to output mode
while True:
    laser.value(1)# light up the laser
    time.sleep(2)# delay 2s
    laser.value(0)# turn off the laser
    time.sleep(2)# delay 2s
```

### Project 4: Button Sensor

![](./media/4d5f6ea741d1e346e03f6efe7cfc9d2d.jpeg)

**1. Overview**

In this kit, there is a Keyestudio single-channel button module, which mainly uses a tact switch and comes with a yellow button cap.

In previous lessons, we learned how to make the pins of our single-chip microcomputer output a high level or low level. In this experiment, we will read the high level (3.3V) and low level (0V).

We can determine whether the button on the sensor is pressed by reading the high and low level of the S terminal on the sensor.

**2. Working Principle**

The button module has four pins. The pin 1 is connected to the pin 3 and the pin 2 is linked with the pin 4. When the button is not pressed, they are disconnected. Yet, when the button is pressed, they are connected. If the button is released, the signal end is high level.

![](./media/a51debfc8a38d0d5729d1da394f95ca5.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.34653in;height:0.73472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/efcc7b40d80043b7b1f90ceaa8d73639.png" style="width:1.23611in;height:0.84861in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.91736in;height:0.33403in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.99167in;height:0.53125in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Button Sensor*1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/a3c4e790c1282b3522375f8c27213c68.png)

**5. Run the test code**

Find **button\.py**，double-click it，and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/55ebf96932130eacb4d0743974604fa1.png)

**6. Code Explanation**

**button = Pin(15, Pin\.IN,  Pin.PULL\_UP)**, we define the pin of the button as GP15 and set to PULL-UP mode.

We can use **button = Pin(15, Pin\.IN) to** set INPUT mode, at this time, the pins are in high resistance state.

**button.value()** reads levels of buttons. Function returns High or Low.

**if..else.. sentence**, when the logic judge is TRUE, the code under the if will be activated; otherwise, the code udder the else will be activated.

When pico detects the button pressed, the signal end is low level (GP 15 is low level). **button.value()** is 0. If pico detects the button unpressed, **button.value()** is 1 and else sentence will be activated.

**7. Test Result**

Run the code, and look at the Shell. When the button is pressed, “You pressed the button\!”will be displayed; if released,“You loosen the button\!”will appear, as shown below.

![](./media/a458c5ccc0b147528cfdf59ff7e0fb62.jpeg)

![](./media/44395956f5203a0b84d1f326994d496b.png)

**8. Test code**

```Python
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
        print("You pressed the button!")   #press the button to print the message
    else:
        print("You loosen the button!")
    time.sleep(0.1) #delay 0.1s
```

### Project 5: Capacitive Sensor

![](./media/794f73317cd5349345e92cebb5ccb410.jpeg)

**1. Description**

In this kit, there is a capacitive touch module which mainly uses a TTP223-BA6 chip. It is a touch detection chip, which provides a touch button, and its function is to replace the traditional button with a variable area button. When we power on, the sensor needs about 0.5 seconds to stabilize. Do not touch the keys during this time period. At this time, all functions are disabled, and self-calibration is always performed. The calibration period is about 4 seconds. We display the test results in the shell.

**2. Working Principle**

![](./media/7fe7f9d2bdf7b9b25e708c52d7dda66d.png)

When our fingers touch the module, the signal S outputs high levels, the red LED on the module flashes. We can determine if the button is pressed or not by reading high and low levels on the sensor.

**3. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.34653in;height:0.73472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0f78442477f8d2a5f5ef81974e03ee1c.png" style="width:0.84722in;height:0.6375in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.91736in;height:0.33403in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.99167in;height:0.53125in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio DIY Capacitive Module*1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Connection Diagram**

![](./media/c47a7e69ffa79fd05fe420aaec4948b8.png)

**5. Run the test code**

Find **Touch\.py**, double-click it and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/8164a460514b74f1f31894e0661c5152.png)

**6. Code Explanation**

When we touch the sensor, the Shell monitor will show“You pressed the button\!”, if not,“You loosen the button\!”will be shown on the monitor.

![](./media/e473773b5b2f145cd04d8af353c1008a.jpeg)

![](./media/d97e81eb2fed48fa46f70650c3be99a5.png)

**7. Test code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 5
 * Touch sensor
 * http://www.keyestudio.com
'''
from machine import Pin
import time

button = Pin(3, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 1:
        print("You pressed the button!")   #Touch the button to print the message
    else:
        print("You loosen the button!")
    time.sleep(0.1) #delay 0.1s
```

### Project 6: Obstacle Avoidance Sensor

![](./media/e6dda88bb6faf8fc06d81361b7f48a3d.jpeg)

**1. Overview**

In this kit, there is a Keyestudio obstacle avoidance sensor, which mainly uses an infrared emitting and a receiving tube. In the
experiment, we will determine whether there is an obstacle by reading the high and low level of the S terminal on the sensor.

**2. Working Principle**

NE555 circuit provides IR signals with frequency to the emitter TX, then the IR signals will fade with the increase of transmission distance. If encountering the obstacle, it will be reflected back.

When the receiver RX meets the weak signals reflected back, the receiving pin will output high levels, which indicates the obstacle is far away. On the contrary, it the reflected signals are stronger, low levels will be output, which represents the obstacle is close. There are two potentiometers on the module, and one is for adjusting emission power, another one is for receiving frequency.

![](./media/f32ebd19bd8e893ab6c865f83b274900.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.40139in;height:0.76458in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b62846d9a80a7e7aed5ffbef0caedf7c.png" style="width:1.24167in;height:0.72083in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio DIY Obstacle Avoidance Sensor*1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/23909e37c3ab412e5fcfa0f76375b490.png)

**5. Run the test code**

Find **Avoid\.py**，double-click it and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/7e5f138634b1bba5f291f613c7bbb4b4.png)

**6. Code Explanation**

Run the code, we start to adjust the two potentiometers to sense distance.

1.  Adjust the potentiometer transmitting power. Make the P LED at the critical point of ON and OFF states.

2.  Adjust the potentiometer receiving frequency. Rotate it clockwise, the frequency will increase. Make the S LED at the critical point of ON and OFF states, then the 38KHz square wave can be produced.

**7. Test Result**

Run the code, when the sensor detects the obstacle, the Shell will show“There are obstacles”; if the obstacle is not detected, “All
going well” will be shown.

![](./media/5a9ec58b818860fc3b4154638a66e106.jpeg)

![](./media/3fe2e80ea6b928f57c4920e32e493de7.png)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 6
 * Infrared obstacle avoidance sensor
 * http://www.keyestudio.com
'''
from machine import Pin
import time

sensor = Pin(16, Pin.IN)
while True:
    if sensor.value() == 0:
        print("There are obstacles")
    else:
        print("All going well")
    time.sleep(0.1)
```
### Project 7: Line Tracking Sensor

![](./media/deac96f3f54b7bedea5399a3aca20c71.jpeg)

**1. Description**

In this kit, there is a DIY electronic building block single-channel line tracking sensor which mainly uses a TCRT5000 reflective black and white line recognition sensor element.

In the experiment, we judge the color (black and white) of the object detected by the sensor by reading the high and low levels of the S terminal on the module; and display the test results on the shell.

**2. Working Principle**

![](./media/b4bec738ca3565a2ce3a274bfec4a57a.png)

When a black or no object is detected, the signal terminal will output high levels; when white object is detected, the signal terminal is low level; its detection height is 0-3cm. We can adjust the sensitivity by rotating the potentiometer on the sensor. When the potentiometer is rotated, the sensitivity is best when the red LED on the sensor is at the critical point between off and on.

**3. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.40139in;height:0.76458in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/3538e48e4603a0afb9ae18197769c3ef.png" style="width:0.89375in;height:0.67569in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio DIY Line Tracking Sensor*1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/6419b67e57f34fbed9f04913ed55a404.png)

**5. Run the test code**

Find **Line\_tracking.py**，double-click it and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/d7343b2fb458cd56338ddecb8539198d.png)

**6. Test Result**

Upload test code, wire up, open the monitor and set baud rate to 9600.

In the experiment, when the sensor doesn’t detect an object or detects a black object, the val is 1, and the monitor will display "Black" ; when a white object (can reflect light) is detected, the val is 0, and the monitor will display "White" ;

![](./media/bd815a52d64d79a976551c87be753e37.jpeg)

![](./media/1db4c201360f9c863ba62f020df422aa.png)

**7. Test code**

```Python
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
        print("0   White")   #Press to print the message
    else:
        print("1   Black")
    time.sleep(0.1) #delay 0.1s
```

### Project 8: Photo Interrupter

![](./media/20519af325d65d055bd8b70c1475438e.jpeg)

**1. Description**

This kit contains a photo interrupter which mainly uses 1 ITR-9608 photoelectric switch. It is a photoelectric switch optical switch
sensor.

**2. Working Principle**

When the paper is put in the slot, C is connected with VCC and the signal end S of the sensor are high levels; then the red LED will be off. Otherwise, the red LED will be on.

![](./media/95c79c5260ec5e7d4de31094ea608767.png)

**3. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.40139in;height:0.76458in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/1fd8fab1f649d7f3f7711afd088046d3.png" style="width:0.90347in;height:0.68333in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio DIY Photo Interrupter*1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/a391decf73d6630e4e046aaceff5ca3b.png)

**5. Run the test code**

Find **Photo\_Interrupt.py**，double-click it and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/75779aabfb5b0eab280c36df2d81cd31.png)

**6. Code Explanation**

Logic setting:

|Initial Setting | Set PushCounter to 0; Set State to 0 (value of the sensor);Set lastState to 0|   |
| :--: | :--: | :--: |
| when an object enters the slot |lastState is 0，State turns into 1; lastState turns into 1 | Set PushCounter to PushCounter+1;print the value of PushCounter |
| when the object leaves the slot | lastState is 1，State becomes 0，two data are not equal，lastState turns into 0. | PushCounterdoesn’t change;Don’t print the value of PushCounter |
| When the object goes through this slot again | lastState is 0, State becomes 1，two data are not equal，lastState turns into 1. | Set PushCounter to PushCounter+1; And print the value of PushCounter|
| When the object leaves this slot again | lastState is 1，State turns into 0，two data are not equal lastState turns into 0 | PushCounter doesn’t change; Don’t print the PushCounter value|


**7. Test Result**

Wire up, upload test code, and the shell displays the PushCounter data. Every time when the object passes through the slot of the sensor, the PushCounter data will increase by 1 continuously, as shown below;

![](./media/f6f0d24dbc827bb5a4564ec1187555d8.jpeg)

![](./media/d1755df004604fcbb17e5677ec9d79d2.png)

**8. Test code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 8
 * Photo_Interrupt
 * http://www.keyestudio.com
'''
from machine import Pin
import time

sensor = Pin(3, Pin.IN, Pin.PULL_UP)
lastState = 0
PushCounter = 0

while True:
    State = sensor.value()
    if  State != lastState:
        if State == 1:
            PushCounter += 1
            print(PushCounter)   #Press to print the message
    lastState = State
```

### Project 9: Tilt Module

![](./media/9d4fcf498d8943539935d0f9638f22eb.jpeg)

**1. Overview**

In this kit, there is a Keyestudio tilt sensor. The tilt switch can output signals of different levels according to whether the module is
tilted. There is a ball inside. When the switch is higher than the horizontal level, the switch is turned on, and when it is lower than the horizontal level, the switch is turned off. This tilt module can be used for tilt detection, alarm or other detection.

**2. Working Principle**

The working principle is pretty simple. When pin 1 and 2 of the ball switch P1 are connected, the signal S is low level and the red LED will light up; when they are disconnected, the pin will be pulled up by the 4.7K R1 and make S a high level, then LED will be off.

![](./media/7b5da31ecdd90419d5b3326eebdb14e7.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.39444in;height:0.76111in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/f647184fbb638f8e5a92a388ee1a6f2b.png" style="width:1.02847in;height:0.76944in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Tilt Sensor*1</td>
<td>3P Dupont Wire*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/20f28f1a53426d420cc6a53f190b5dca.png)

**5. Run the test code**

Find Tilt **switch\.py**，double-click and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/a9f1036f79a96bebf514f275adaa32b0.png)

**6. Code Explanation**

Code explanation is as same as the project 3.

**7. Test Result**

Upload the code successfully, and observe the Shell.

Make the tilt module incline to one side, the red LED on the module will be off and the Shell page will display“1 The switch is turned off”; by contrast, if you make it incline the other side, the red LED will light up and“0 The switch is turned on”will be shown.

![](./media/f3097cbdac2b1167b04a761b8b596fa8.jpeg)

![](./media/ee441a8f5b10139e2c0b84f68588676c.png)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 9
 * Tilt switch
 * http://www.keyestudio.com
'''
from machine import Pin
import time

TiltSensor = Pin(17, Pin.IN)

while True:
    value = TiltSensor.value()
    print(value, end = " ")
    if  value== 0:
        print("The switch is turned on")
    else:
        print("The switch is turned off")
    time.sleep(0.1)
```
### Project 10: Hall Sensor

![](./media/3fa2bf365868256a8c9fe4f32c883c91.jpeg)

**1. Description**

In this kit, there is a Hall sensor which mainly adopts a A3144 linear Hall element. The element P1 is composed of a voltage regulator, a Hall voltage generator, a differential amplifier, a Schmitt trigger, a temperature compensation circuit and an open-collector output stage. In the experiment, we use the Hall sensor to detect the magnetic field and display the test results on the shell.

**2. Working Principle**

When the sensor detects no magnetic field or a north pole magnetic field, the signal terminal will be high level; when it senses a south pole magnetic field, the signal terminal will be low levels.

The stronger the magnetic field strength is, induction distance is longer.

**3. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.39444in;height:0.76111in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/bf9962d91f7f917f4212686ef6962fd3.png" style="width:0.89097in;height:0.66806in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio DIY Hall Sensor*1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/0cfa241425f6aff265622be8d99b631f.png)

**5. Run the test code**

Find and double-click **Hall\.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/55df03c6deaf4b460741faaf689f8bd7.png)

**6. Test Result**

Upload the test code, open the monitor.

when the sensor detects no magnetic fields or the north pole magnetic field, the monitor l will show“1 There is no magnetic field”and the LED on the sensor will be off; When it detects the south pole magnetic field, “0 A magnetic field”and the LED on the sensor will be on

![](./media/85a0107d2fe50ae3c20b2db98a1ba6b2.jpeg)

![](./media/34c8fcb8bbc1b57bce7e4541d376f0cc.png)

**7. Test code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 10
 * Hall magnetic
 * http://www.keyestudio.com
'''
from machine import Pin
import time

hall = Pin(5, Pin.IN)
while True:
    value = hall.value()
    print(value, end = " ")
    if value == 0:
        print("A magnetic field")
    else:
        print("There is no magnetic field")
    time.sleep(0.1)
```

### Project 11: Reed Switch Module

![](./media/2a699e913fa52d9acff4b0e4a8188540.png)

**1. Overview**

In this kit, there is a Keyestudio reed switch module, which mainly uses a MKA10110 green reed component.

The reed switch is the abbreviation of the dry reed switch. It is a passive electronic switch element with contacts.

It has the advantages of simple structure, small size and easy control.

Its shell is a sealed glass tube with two iron elastic reed electric plates.

In the experiment, we will determine whether there is a magnetic field near the module by reading the high and low level of the S terminal on the module; and, we display the test result in the shell.

**2. Working Principle**

Reed switch is an abbreviation of the dry reed contacts a passive electronic switching elements, and has the advantages of simple structure, small size and ease of control, its shell is a sealed glass tube, the tubes are installed two iron elastic reed plate, but also filling called rhodium metal inert gas. In peacetime, the glass tube in the two reeds made of special materials are separated. When a magnetic substance close to the glass tube, in the role of the magnetic field lines, the pipe within the two reeds are magnetized to attract each other in contact, the reed will suck together, so that the junction point of the connected circuit communication. After the disappearance of the outer magnetic reed because of their flexibility and separate, the line is disconnected. Therefore, as a use of the magnetic field signals to control the line switching device, reed tube can be used as a sensor for counting the number, spacing, etc., and also are widely used in a variety of communication devices.

![](./media/a4a9a00f86be808be0a9c784a6960cd6.jpeg)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.49028in;height:0.81319in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/92c44afcc82bb13a14e8438646670cc6.png" style="width:1.06875in;height:0.78681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Reed Switch Module*1</td>
<td>3P Dupont Wire*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/8b11ee443f3ad79e2d9b3a681bf4e74b.png)

**5. Run the test code**

Find Reed **Switch\.py**，double-click and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png). 

![](./media/974a5184e0d1be96ea8692742c3bac9e.png)

**6. Code Explanation**

The setting method is the same as the previous experiment. Note that it detects magnetic field.

**7. Test Result**

Upload the code. When the sensor detects a magnetic field, val is 0 and the red LED of the module lights up, "0 A magnetic field" will be displayed; when no magnetic field is detected, val is 1, and the LED on the module goes out, "1 There is no magnetic field" will be shown.

![](./media/0bf581a9308f0932ee66879e1420c5bb.jpeg)

![](./media/a6d062c3c503be4e8e789f21b6d3f8c5.png)

**8. Test Code：**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 11
 * Reed Switch
 * http://www.keyestudio.com
'''
from machine import Pin
import time

ReedSensor = Pin(18, Pin.IN)
while True:
    value = ReedSensor.value()
    print(value, end = " ")
    if value == 0:
        print("A magnetic field")
    else:
        print("There is no magnetic field")
    time.sleep(0.1)
```

### Project 12: PIR Motion Sensor

![](./media/d58ba7b9b4a0115b07cbb1c871ef8ec9.jpeg)

**1. Overview**

In this kit, there is a Keyestudio PIR motion sensor, which mainly uses an RE200B-P sensor elements. It is a human body pyroelectric motion sensor based on pyroelectric effect, which can detect infrared rays emitted by humans or animals, and the Fresnel lens can make the sensor's detection range farther and wider.

In the experiment, we determine if there is someone moving nearby by reading the high and low levels of the S terminal on the module. The detected results will be displayed on the Shell.

**2. Working Principle**

The upper left part is voltage conversion(VCC to 3.3V). The working voltage of sensors we use is 3.3V, therefore we can’t use 5V directly. The voltage conversion circuit is needed.

When no person is detected or no infrared signal is received, and pin 1 of the sensor outputs low level. At this time, the LED on the module will light up and the MOS tube Q1 will be connected and the signal terminal S will detect Low levels.

When one is detected or an infrared signal is received, and pin 1 of the sensor outputs a high level. Then LED on the module will go off, the MOS tube Q1 is disconnected and the signal terminal S will detect high levels.

![](./media/e62f4d614ab7e67ac373576d7ff96fee.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.40972in;height:0.76944in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/8712c267aff99cc16c2071398d6632af.png" style="width:1.23125in;height:0.83958in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio PIR Motion Sensor*1</td>
<td>3P Dupont Wire*1</td>
<td><p>Micro</p>
<p>USB Cable*1</p></td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/a5f247d1b76d442ec075ec29653648ba.png)

**5. Run the Test Code**

Find and double-click **PIR motion\.py** to open it, click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the code.

![](./media/f86ca2b6e8258b1ec1e3ca37599c8023.png)

**6. Code Explanation**

The setting method is the same as project 3.

**7. Test Result**

Upload the code, when the sensor detects someone nearby, value is 1, the LED will go off and the Shell page will show“1 Somebody is in this area\!”. In contrast, the value is 0, the LED will go up and“0 No one\!”will be shown.

![](./media/a4d98b4a08d468f9cb56fa2af973aa4a.jpeg)

![](./media/b59acfbea779d6984a83ad8e72630a25.png)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 12
 * PIR motion
 * http://www.keyestudio.com
'''
from machine import Pin
import time

PIR = Pin(19, Pin.IN)
while True:
    value = PIR.value()
    print(value, end = " ")
    if value == 1:
        print("Some body is in this area!")
    else:
        print("No one!")
    time.sleep(0.1)
```

### Project 13: Active Buzzer

![](./media/f4cc23dc8ed28d408e5a119855e19aa2.jpeg)

**1. Overview**

In this kit, it contains an active buzzer module and a power amplifier module (the principle is equivalent to a passive buzzer). In this experiment, we control the active buzzer to emit sounds. Since it has its own oscillating circuit, the buzzer will automatically sound if given large voltage.

**2. Working Principle**

![](./media/458b66a2a23d6e135e7cf9975fe27507.png)

From the schematic diagram, the pin of buzzer is connected to a resistor R2 and another port is linked with a NPN triode Q1. So, if this triode Q1 is powered, the buzzer will sound.

If the base electrode of the triode connected to the R1 resistor is a high level, the triode Q1 will be connected.If the base electrode is pulled down by the resistor R3, the triode is disconnected.

When we output a high level from the IO port to the triode, the buzzer will emit sounds; if outputting low levels, the buzzer won’t emit sounds.

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.43681in;height:0.78403in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/a5e355d0fd3c9b18c7684a9a2b99f0a5.png" style="width:1.00625in;height:0.74167in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Active Buzzer*1</td>
<td>3P Dupont Wire*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/e816661c31698424ee1c710228679e7d.png)

**5. Run the Test Code**

Find and double-click **A-buzzer\.py** to open it, then click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the code.

![](./media/bb8d6cc26509f7815ecccad02786dc63.png)

**6. Code Explanation**

In the experiment, the pin is set to 20. When setting HIGH, the active buzzer on the module will emit sounds; when setting LOW, the buzzer won’t chime.

**7. Test Result**

Upload the code and power on. The buzzer will chime for 1s and stop for 1s.

![](./media/4d04a020bccc360be34122920e86e822.jpeg)

**8. Test Code**

```Python 
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 13
 * Active buzzer
 * http://www.keyestudio.com
'''
from machine import Pin
import time

buzzer = Pin(20, Pin.OUT)
while True:
    buzzer.value(1)
    time.sleep(1)
    buzzer.value(0)
    time.sleep(1)
```

### Project 14: 8002b Audio Power Amplifier

![](./media/6e8569df97b72e866488a6f414f9e392.jpeg)

**1. Overview**

In this kit, there is a Keyestudio 8002b audio power amplifier. The main components of this module are an adjustable potentiometer, a speaker, and an audio amplifier chip;

The main function of this module is: it can amplify the output audio signal, with a magnification of 8.5 times, and play sound or music through the built-in low-power speaker, as an external amplifying device for some music playing equipment.

In the experiment, we used the 8002b power amplifier speaker module to emit sounds of various frequencies.

**2. Working Principle**

In fact, it is similar to a passive buzzer. The active buzzer has its own oscillation source.Yet, the passive buzzer does not have internal oscillation. When controlling the circuit, we need to input square waves of different frequencies to the positive pole of the component and ground the negative pole to control the buzzer to chime sounds of different frequencies.

![](./media/f5f372e0713df6439a7cc52f5caf1cad.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.43681in;height:0.78403in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/afd2d5f63e3823e1cb941fc73a51d3ac.png" style="width:1.15556in;height:0.67986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio 8002b Audio Power Amplifier*1</td>
<td>3P Dupont Wire*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/d7a129cb825ec46ad272f072cabdd90a.png)

**5. Run the test code**

Find and double-click **Horn\.py** to open it, then click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the code.

![](./media/fdfaeb6f8dd185133a4c725f734cbd23.png)

**6. Code Explanation**

We use PWM of the machine,

**buzzer = PWM(Pin(21))** is a **PWM** example and the pin of the buzzer is connected to GP21.

**buzzer.duty\_u16(1000)** is used to set duty cycle(1000/65535) and the larger this value, the louder the buzzer. When you set to 0, the buzzer doesn’t emit sounds.

**buzzer.freq()** is frequency setting.

PWM is also called pulse width modulation. Pulse width modulation (PWM) refers to the use of the digital output of the microprocessor to control the analog circuit, and is a method of digitally encoding the analog signal level. It uses a digital pin to send a square wave of a certain frequency, that is, a high level and a low level are alternately output for a period of time. The total time of each group of high level and low level is usually fixed, which is called cycle. The time of high level output is generally called pulse width, and the percentage of pulse width is called duty cycle. The longer the duration of the high level, the greater the duty cycle of the analog signal, and the greater the corresponding voltage. The pulse width in the figure below accounts for 50%, then the output voltage is 3.3 \* 50% = 1.65V.

![](./media/ee0a9b43ef24bd6f50cff177eb88f645.png)

Firstly, we set duty cycle to 1000/65535, and frequency of DO, RE, MI, FA, SO, LA and SI and emit DO, RE, MI, FA ,SO, LA and SI for 0.5s and turn off the buzzer.

**7. Test Result**

Upload the code and power on. Then the audio power amplifier will emit DO，Re，Mi，Fa，So，La，Si.

![](./media/3e4f5e7c1b555f11e01b9db4f5e6be30.jpeg)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 14
 * Passive buzzer
 * http://www.keyestudio.com
'''
from machine import Pin, PWM
from time import sleep
buzzer = PWM(Pin(21))

buzzer.duty_u16(1000)

buzzer.freq(523)#DO
sleep(0.5)
buzzer.freq(586)#RE
sleep(0.5)
buzzer.freq(658)#MI
sleep(0.5)
buzzer.freq(697)#FA
sleep(0.5)
buzzer.freq(783)#SO
sleep(0.5)
buzzer.freq(879)#LA
sleep(0.5)
buzzer.freq(987)#SI
sleep(0.5)
buzzer.duty_u16(0)
```

### Project 15: 130 Motor 

![](./media/6c4e0d18c7c1867e27c0bac8e1c6412b.jpeg)

**1. Description**

The 130 motor driver module is compatible with servo motors, which has high efficiency and good quality fans.

It adopts a HR1124S motor control chip. HR1124S is a single-channel H-bridge driver chip for DC motor solutions. In addition, this chip has low standby current and low quiescent current.

The module is compatible with various single-chip control boards. In the experiment, we can control the rotation direction of the motor by outputting the voltage directions of the two signal terminals IN+ and IN- to make the motor rotate.

**2. Working Principle**

The chip is used to help drive the motor.

We can’t drive it with a triode or an IO port due to its a large current of need. It is very simple to make the motor rotate. Just apply voltage to both ends of the motor. The direction of the motor is different in different voltage directions. Within the rated voltage, the higher the voltage, the faster the motor rotates; on the contrary, the lower the voltage, the slower the motor rotates, or even unable to rotate.

So we can use the PWM port to control the speed of the motor. We haven't learned PWM here, so we use the high and low levels to control the motor first.

![](./media/5ea2e4d2b18f87ffa9a31e834764ec4b.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.40417in;height:0.76667in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/6c2548137a8c675141b83227beeb2eb9.png" style="width:1.02917in;height:0.90694in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>keyestudio DIY 130 Motor*1</td>
<td>4P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<span style="color: rgb(255, 76, 65);">Note:</span> the motor is separated with its fan, you need to assemble it first.
<br>
<br>

**4. Wiring Diagram**

![](./media/83eb45f2c40b4ed32c034958b717f841.png)

**5. Run the test code**

Find **Motor\.py**，double-click and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/993f907653e757cd2320131dc8bd1ea4.png)

**6. Code Explanation**

Set pins to 14 and 15, when the pin 14 outputs high levels and the pin 15 outputs low levels, the motor will rotate counterclockwise; when both pins are set to low, the motor stops rotating.

**7. Test Result**

Burn the test 130 motor code, and connect the wires according to the Wiring Diagram; after power-on, the fan rotates counterclockwise for 2 seconds; stops for 1 second; rotates clockwise for 2 seconds; stops for 1 second; cycle alternately.

Wire up, upload test code and test the 130 motor, the fan will rotate counterclockwise for 2 seconds, stop for 1 second and clockwise for 2 seconds and stop for 1 second; cycle alternately.

![](./media/34de9462f97a58421247a4225e3c6528.jpeg)

**8. Test code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 15
 * 130-DC Motor
 * http://www.keyestudio.com
'''
from machine import Pin
import time

#set the two pins of the motor
INA = Pin(14, Pin.OUT)
INB = Pin(15, Pin.OUT)

while True:
    #counter-clockwise for 2s
    INA.value(1)
    INB.value(0)
    time.sleep(2)
    #stop for 1s
    INA.value(0)
    INB.value(0)
    time.sleep(1)
    #clockwise for 2s
    INA.value(0)
    INB.value(1)
    time.sleep(2)
    #stop for 1s
    INA.value(0)
    INB.value(0)
    time.sleep(1)
```

### Project 16: RGB Module

![](./media/b3515a7e0340f391bef256c9ed6ccd4b.jpeg)

**1. Overview**

Among these modules is a RGB module. It adopts a F10-full color RGB foggy common cathode LED. We connect the RGB module to the PWM port of MCU and the other pin to GND(for common anode RGB, the rest pin will be connected to VCC). So what is PWM?

PWM is a means of controlling the analog output via digital means. Digital control is used to generate square waves with different duty cycles (a signal that constantly switches between high and low levels) to control the analog output. In general, the input voltages of ports are 0V and 5V. What if the 3V is required? Or a switch among 1V, 3V and 3.5V? We cannot change resistors constantly. For this reason, we resort to PWM.

![](./media/bbcfcb9ae56abb7e80ee587246fc4be9.GIF)

For Arduino digital port voltage outputs, there are only LOW and HIGH levels, which correspond to the voltage outputs of 0V and 5V respectively. You can define LOW as“0”and HIGH as“1’, and let the Arduino output five hundred‘0’or“1”within 1 second. If output five hundred‘1’, that is 5V; if all of which is‘0’,that is 0V; if output 25001 pattern, that is 2.5V.

This process can be likened to showing a movie. The movie we watch are not completely continuous. Actually, it generates 25 pictures per second, which cannot be told by human eyes. Therefore, we mistake it as a continuous process. PWM works in the same way. To output different voltages, we need to control the ratio of 0 and 1. The more‘0’or‘1’ output per unit time, the more accurate the control.

**2. Working Principle**

For our experiment, we will control the RGB module to display different colors through three PWM values.

**3. Components**

![](./media/71e990d503b6f1822379091a37f58a6b.jpeg)

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.41042in;height:0.76944in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/51729b3ba2184cf0ca0d3242199731ad.png" style="width:1.05972in;height:0.78125in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:1.03264in;height:0.40278in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Common Cathode RGB Module *1</td>
<td>4P Dupont Wire*1</td>
<td><p>Micro</p>
<p>USB Cable*1</p></td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/9c7dfc42ed6ec851da62244db01ca496.png)

**5. Run the test code**

Find **rgb1\.py** and **rgb2\.py**，double-click and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/ad83069d0e3d6e46a2469b84b29b07c8.png)

**6. Code Explanation**

Code 1:

**red**, **green** and **blue** represent ports of red, green and blue color. Connect them to GP9 GP10 GP11 and set to 9, 10 and 11. The RGB will show red color, green color and blue color with an interval of one second.

Code 2:

In the code 2, we use PWM output, the frequency we set is **freq(1000)**. **.duty\_u16().** The data stands for the proportion of
color red, green and blue. The larger the data of the duty cycle, the larger the proportion of the color;

In the experiment, we can adjust the proportion of red, green and blue of RGB LED by setting corresponding values. Thus, the RGB can display the corresponding color.

<span style="color: rgb(255, 76, 65);">Note:</span> The duty ratio we set above is at most .duty\_u16(65535). 65535 is equal to 256\*256-1(0\~65535). When we compare the color table below, we only need to multiply the following value by 256.

**RGB Color Chart**

![](./media/4dea29ef0ba554d3ec21186d0dfb9890.png)

**7. Test Result**

Upload the code 1, the RGB on the module will show red, green and blue color with an interval of 1s.

Upload the code 2, the RGB on the module will show red, orange, yellow, green, cyan-blue, blue, purple and white color with an interval of 1s.

![](./media/99636ab436d8b62a912d77a0c2893108.jpeg)

**8. Test Code**

Test Code1:

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 16.1
 * RGB
 * http://www.keyestudio.com
'''
from machine import Pin
from time import sleep

red = Pin(9, Pin.OUT)
green = Pin(10, Pin.OUT)
blue = Pin(11, Pin.OUT)

while 1:
    red.value(1)
    green.value(0)
    blue.value(0)
    sleep(1)
    red.value(0)
    green.value(1)
    blue.value(0)
    sleep(1)
    red.value(0)
    green.value(0)
    blue.value(1)
    sleep(1)
```


Test Code2:

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 16.2
 * RGB
 * http://www.keyestudio.com
'''
from machine import Pin, PWM
from time import sleep
pwm_r = PWM(Pin(9))
pwm_g = PWM(Pin(10))
pwm_b = PWM(Pin(11))

pwm_r.freq(1000)
pwm_g.freq(1000)
pwm_b.freq(1000)

def light(red, green, blue):
    pwm_r.duty_u16(red)
    pwm_g.duty_u16(green)
    pwm_b.duty_u16(blue)

while 1:
    light(65535, 0, 0)#red
    sleep(1)
    light(65535, 25088, 0)#orange
    sleep(1)
    light(65535, 65535, 0)#yellow
    sleep(1)
    light(0, 65535, 0)#green
    sleep(1)
    light(0, 0, 65535)#blue
    sleep(1)
    light(0, 65535, 65535)#cyan
    sleep(1)
    light(41216, 8448, 61696)#purple
    sleep(1)
```


### Project 17: Potentiometer

![](./media/fe92a4f36758bc236d94290478fe5eac.jpeg)

**1. Overview**

The following we will introduce is the Keyestudio rotary potentiometer which is an analog sensor.

The digital IO ports can read the voltage value between 0 and 3.3V and the module only outputs high levels. However, the analog sensor can read the voltage value through ADC analog ports(GP26\~GP28) on the pico board.

In the experiment, we will display the test results on the Shell.

**2. Working Principle**

It uses a 10K adjustable resistor. We can change the resistance by rotating the potentiometer. The signal S can detect the voltage
changes(0-3.3V) which are analog quantity.

![](./media/a6ca9064a864e572984fdc41207eaaca.jpeg)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.35764in;height:0.74097in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/9d866a71104fb3cf1826c41c3c940ba8.png" style="width:1.05in;height:0.86667in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Rotary Potentiometer*1</td>
<td>3P Dupont Wire*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/fd0b5491083835560e344ed545f5da01.png)

**5. Run the Test Code**

Find and double-click **potentiometer\.py** to open it, then click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the code.

![](./media/e3eb271d20af21fd5b3fdbfe6c0d2a8b.png)

**6. Code Explanation**

In the experiment, we create **ADC examples**, connect GP26(ADC(26)).

**.read\_u16():** this is used to read analog value, the range is 0\~65535, **potentiometer.read\_u16()** means that reading the output
analog value of pin ADC(26), then name **pot\_value**.

**utime.sleep()** delayed function can work as same as the function
**time.sleep()**.

**7. Test Result**

Run the test code and observe the corresponding simulation value displayed in the Shell below. In the experiment, rotate the
potentiometer clockwise, the analog value increases, and turn the potentiometer counterclockwise, the analog value decreases, the range is 65535, as shown in the figure below.

![](./media/9db115aa9829ad066b9f26d525c22e0f.jpeg)

![](./media/3dd25ba81c3ed097ae2c3472231c0c55.png)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 17
 * Rotary potentiometer
 * http://www.keyestudio.com
'''
import machine
import utime

potentiometer = machine.ADC(26)

while True:
    pot_value = potentiometer.read_u16()
    print(pot_value)
    utime.sleep(0.1)
```


### Project 18: Steam Sensor

![](./media/0062e47b90828244595c1fb93c45f1d5.jpeg)

**1. Description**

This is a commonly used steam sensor. Its principle is to detect the amount of water by bare printed parallel lines on the circuit board. The more the water is, the more wires will be connected. As the conductive contact area increases, the output voltage will gradually rise. It can detect water vapor in the air as well. The steam sensor can be used as a rain water detector and level switch. When the humidity on the sensor surface surges, the output voltage will increase.

In the experiment, we connect the signal terminal (S terminal) of the sensor to the analog port of the pico development board. The analog value detected will be displayed on the serial monitor.

**2. Working Principle**

Its principle is to detect the amount of water through the exposed printed parallel lines on the circuit board. The more water there is, the more wires will be connected, and the conductive contact area increases. The voltage output by pin 2 will gradually increase. The larger the analog value detected by the signal terminal S is.

It can also detect steam in the air. Two position holes are used to install on the other devices

![](./media/790270169035ee740b28c49c4b1dde47.png)

**3. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.35764in;height:0.74097in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b64cdb5749df7d2b7dd3719216c7aff3.png" style="width:0.91458in;height:0.65417in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio DIY Steam Sensor *1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/506b3ebf75246b8fe2b8b024b41dc276.png)

**5. Run the test code**

Find **Water\.py**，double-click and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/e4053e3b2f8add99e8500fb1b913dba0.png)

**6. Test Result**

Wire up, run the test code , power up and set baud rate to 9600. The more water volume, the greater the output voltage and the analog value, as shown below.

![](./media/20324733c27c452684b463d45808e9fc.jpeg)

![](./media/f96ddda85f269bf48b4f42a73b2b3434.png)

**7. Test code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 18
 * Steam sensor
 * http://www.keyestudio.com
'''
import machine
import utime

sensor = machine.ADC(26)#ADC0

while True:
    value = sensor.read_u16()
    print(value)
    utime.sleep(0.1)

```

### Project 19: Sound Sensor

![](./media/c4d4961f71c7e91bae04507f72cb56eb.jpeg)

**1. Overview**

In this kit, there is a sound sensor. In the experiment, we test the analog value corresponding to the sound level in the current environment with it. The louder the sound, the larger the analog value;

**2. Working Principle**

![](./media/d55fc5234be47e7727c0bf48c049e341.jpeg)

It uses a high-sensitive microphone component and an LM386 chip.

We build the circuit with the LM386 chip and amplify the sound through the high-sensitive microphone. In addition, we can adjust the sound volume by the potentiometer. Rotate it clockwise, the sound will get louder.

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.40972in;height:0.76944in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/6406b86b355b4986a8b2ec74f770c2ba.png" style="width:1.09236in;height:0.82292in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.8875in;height:0.47569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Sound Sensor*1</td>
<td>3P Dupont Wire*1</td>
<td><p>Micro</p>
<p>USB Cable*1</p></td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/00ef9bf64d6866acfed596128fbb0401.png)

**5. Run the test code**

Find **MicroPhone\.py**，double-click and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/71b70c14a8e1f5761529228460896151.png)

**6. Test Result**

Upload the code power up by a USB cable, open the serial monitor and set baud rate to 9600. Rotate clockwise the potentiometer and speak at the MIC. Then you can see the analog value get larger, as shown below

![](./media/da9b57afa119f6f6572527e53abec077.jpeg)

![](./media/8392fa77a1c3804d24c468c3e716ef29.png)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 19
 * MicroPhone
 * http://www.keyestudio.com
'''
import machine
import utime

MicroPhone = machine.ADC(27)
while True:
    value = MicroPhone.read_u16()
    print(value)
    utime.sleep(0.1)
```

### Project 20: Photoresistor

![](./media/37bb57bcf72ba62056bbc61164185f0a.png)

**1. Description**

In this kit, there is a photoresistor which consists of photosensitive resistance elements. Its resistance changes with the light intensity. Also, it converts the resistance change into a voltage change through the characteristic of the photosensitive resistive element. When wiring it up, we interface its signal terminal (S terminal) with the analog port of pico , so as to sense the change of the analog value, and display the corresponding analog value in the shell.

**2. Working Principle**

If there is no light, the resistance is 0.2MΩ and the detected voltage at the terminal 2 is close to 0. When the light intensity increases, the resistance of photoresistor and detected voltage will diminish.

![](./media/7a523e0fa1beca5bd50fbe5eb5daa64f.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.45417in;height:0.79306in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/21847f439e9532462a71d11921112a66.png" style="width:1.02292in;height:0.73056in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Photoresistor*1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/a1088d3e804eedc28ee1d8c9855cdb68.png)

**5. Run the test code**

Find **photoresistance\.py** to double-click and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/4d6e281e3eb2491807fca97bfe067402.png)

**6. Test Result**

Upload the code power up by a USB cable, open the serial monitor. When the light intensity gets stronger, the analog value will get larger, as shown below;

![](./media/37676baeab1baf2830c563e9c1fb180f.jpeg)

![](./media/6fc451c0ce12aaad01acec4b479c5086.png)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 20
 * Photoresistance
 * http://www.keyestudio.com
'''
import machine
import utime

photoresistance = machine.ADC(28)
while True:
    value = photoresistance.read_u16()
    print(value)
    utime.sleep(0.1)
```

### Project 21: NTC-MF52AT Thermistor

![](./media/868d93395d983645baab872091991403.jpeg)

**1. Overview**

In the experiment, there is a NTC-MF52AT analog thermistor. We connect its signal terminal to the analog port of the Raspberry Pi Pico Board and read the corresponding analog value.

We can use analog values to calculate the temperature of the current environment through specific formulas. Since the temperature calculation formula is more complicated, we only read the corresponding analog value.

**2. Working Principle**

![](./media/84a67bb2b90b4740c09d914dc6402f48.png)

This module mainly uses NTC-MF52AT thermistor elements. The NTC-MF52AT thermistor element can sense the changes of the surrounding environment temperature. Resistance changes with the temperature, causing the voltage of the signal terminal S to change.

This sensor uses the characteristics of NTC-MF52AT thermistor element to convert resistance changes into voltage changes.

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.39306in;height:0.75972in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/481d8a887573a4aeeb9a61a8f5b1fe6f.png" style="width:1.04236in;height:0.73889in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio NTC-MF52AT Thermistor*1</td>
<td>3P Dupont Wire*1</td>
<td><p>Micro</p>
<p>USB Cable*1</p></td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/9dc4049d34a9c264b4dd1d7361cdfe4e.png)

**5. Run the test code**

Find and double-click **temperature\.py** and click ![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/3bd9db70fee5c2a309b0f5f214443044.png)

**6. Code Explanation**

The setting method is the same as experiment 11. **ADC(0)** is **ADC(26)**.

**Test Result**

Upload the test code, the more the temperature, the larger the analog value. As shown in Shell page.

![](./media/d10d3a2db145832e73da64f27f982df7.jpeg)

![](./media/86cd26f841e1b19b33c5cd13d7478fbc.png)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 21
 * Temperature sensor
 * http://www.keyestudio.com
'''
import machine
import utime
import math

sensor = machine.ADC(0)
while True:
    temp = sensor.read_u16()
    print("Temperature ADC: ", end = " ")
    print(temp)
    utime.sleep(0.1)
```


### Project 22: Thin-film Pressure Sensor

![](./media/a9ae2963fc87b3502703f7dd5eb208ec.jpeg)

**1. Overview**

In this kit, there is a Keyestudio thin-film pressure sensor. The thin-film pressure sensor composed of a new type of nano
pressure-sensitive material and a comfortable ultra-thin film substrate, has waterproof and pressure-sensitive functions.

In the experiment, we determine the pressure by collecting the analog signal on the S end of the module. The smaller the analog value, the greater the pressure; and the displayed results will shown on the Shell.

**2. Working Principle**

When the sensor is pressed by external forces, the resistance value of sensor will vary. We convert the pressure signals detected by the sensor into the electric signals through a circuit. Then we can obtain the pressure changes by detecting voltage signal changes.

![](./media/520fa537602873d2a337731318668348.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.42639in;height:0.77847in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/84d460c90f09b3f3baa5819ab8655e87.png" style="width:1.975in;height:0.61042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Thin-film Pressure Sensor*1</td>
<td>3P Dupont Wire*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/445c732571d879e6f5708af6f10fb03d.png)

**5. Run the Test Code**

Find and double-click **film pressure\.py**, then click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the code.

![](./media/e40dc61a267e06ff2bd2724e682e6d37.png)

**6. Code Explanation**

The setting method is the same as experiment 11. **ADC(1)** is **ADC(27)**.

**7. Test Result**

Upload the code, when the thin-film is pressed by fingers, the analog value will decrease, as shown below.

![](./media/49c8155267d1020cd3182e7ac352107d.jpeg)

![](./media/413a24ba47f8b963e3b10cc1365a2ccf.png)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 22
 * Film pressure sensor
 * http://www.keyestudio.com
'''
import machine
import utime

film = machine.ADC(1)
while True:
    value = film.read_u16()
    print(value)
    utime.sleep(0.1)
```

### Project 23: Flame Sensor

![](./media/c6c3bf0c9bf0af22a2aa06c5b7399cfd.jpeg)

**1. Description**

In daily life, it is often seen that a fire broke out without any precaution. It will cause great economic and human loss. So how can we avoid this situation? Right, install a flame sensor and a speaker in those places that easily break out a fire. When the flame sensor detects a fire, the speaker will alarm people quickly to put out the fire.

So in this project, you will learn how to use a flame sensor and an active buzzer module to simulate the fire alarm system.

**2. Working Principle**

This flame sensor can be used to detect fire or other light sources with wavelength stands at 760nm \~ 1100nm. Its detection angle is about 60°. You can rotate the potentiometer on the sensor to control its sensitivity. Adjust the potentiometer to make the LED at the critical point between on and off state. The sensitivity is the best.

From the below figure, power up. When detecting fire, the digital pin outputs low levels, the red LED2 will light up first, the digital signal terminal D0 outputs a low level, and the red LED1 will light up. The stronger the external infrared light, the smaller the value; the weaker the infrared light, the larger the value.

![](./media/01f69822915149445858a471784ebddf.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.40417in;height:0.76667in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/4ecedf84c69e9264059ffd14b02592bd.png" style="width:0.95278in;height:0.57153in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>keyestudio DIY Flame Sensor*1</td>
<td>4P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/d388bce2707000a4a8957267eecf51c7.png)

**5. Run the test code**

Find and double-click **Flame\_sensor.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/79dbf39207b7a7eadf7a5846db29ae28.png)

**6. Code Explanation**

Two pins we use are defined as 22 and 26 according to the wiring-up diagram, and print digital signals and analog signals respectively.

**7. Test Result**

Upload the test code and power up，LED2 is on and LED1 is off. Open the monitor, when fire is detected, LED1 will be on. the digital value will change from 1 to 0, and the analog value will become smaller, as shown in the figure below.

![](./media/b51d742306a2bacbe83573f63095112a.jpeg)

![](./media/96a61942c1b74bba45314710b71a648b.png)

**8. Test code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 23
 * Flame sensor
 * http://www.keyestudio.com
'''
import machine
import utime

flame_D = machine.Pin(22, machine.Pin.IN)
flame_A = machine.ADC(26)

while True:
    digitalVal = flame_D.value()
    analogVal = flame_A.read_u16()
    print(digitalVal, end = "  ")
    print(analogVal)
    utime.sleep(0.1)
```

### Project 24: MQ-2 Gas Sensor

![](./media/f712788d3997805df25abe4a99d42461.GIF)

**1. Description**

This analog gas sensor - MQ2 is used in gas leakage detecting equipment in consumer electronics and industrial markets.

This sensor is suitable for detecting LPG, I-butane, propane, methane, alcohol, Hydrogen and smoke. It has high sensitivity and quick response.

In addition, the sensitivity can be adjusted by rotating the potentiometer.

In the experiment, we read the analog value at the A0 port and the D0 port to determine the content of gas.

**2. Working Principle**

![](./media/c55edbe71237172f6b80877504a9debb.png)

The greater the concentration of smoke, the greater the conductivity, the lower the output resistance, the greater the output analog signal.

When in use, the A0 terminal reads the analog value of the corresponding gas; the D0 terminal is connected to an LM393 chip (voltage comparator), we can adjust the alarm threshold of the measured gas through the potentiometer, and output the digital value at D0. When the measured gas content exceeds the critical point, the D0 terminal outputs a low level; when the measured gas content does not exceed the critical point, the D0 terminal outputs a high level.

**3. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.40417in;height:0.76667in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/ee4483f37a6f3609acdb661095f4b706.png" style="width:1.04167in;height:0.52708in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>keyestudio DIY Analog Gas Sensor*1</td>
<td>4P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/ebd6c2127842acc8011cf7a2aa5d9c2d.png)

**5. Run the test code**

Find and double-click **MQ-2\.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/93bc0591b5c5cb136d07fe9eddaffa0a.png)

**6. Test Result**

Run the test code, the yellow-green LED on the module lights up, open the serial monitor, set baud rate to 9600 and display the corresponding data and characters.

In the experiment, we can see the simulated value is less than or equal to 45627, the gas content does not exceed the critical point, and the red LED is off; when the simulated value is greater than or equal to 45627, the gas content exceeds the critical point, and the red LED lights up. That means that the analog value of the critical point of gas content is between 43018-45627, we can adjust the critical point by rotating the potentiometer on the sensor.

![](./media/8d74895e19ff133863647b51d412a111.jpeg)

![](./media/b468f1307bb984818744475062acc88f.png)

**7. Test code**

```Pyhon
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
```

### Project 25: Joystick Module

![](./media/a28a09d0d9103cc8b93f2ae71f98482a.jpeg)

**1. Overview**

Game handle controllers are ubiquitous.

It mainly uses PS2 joysticks. When controlling it, we need to connect the X and Y ports of the module to the analog port of the single-chip microcomputer, port B to the digital port of the single-chip microcomputer, VCC to the power output port(3.3-5V), and GND to the GND of the MCU. We can read the high and low levels of two analog values and one digital port) to determine the working status of the joystick on the module.

In the experiment, two analog values(x axis and y axis) will be shown on Shell.

**2. Working Principle**

In fact, its working principle is very simple. Its inside structure is equivalent to two adjustable potentiometers and a button. When this button is not pressed and the module is pulled down by R1, low levels will be output ; on the contrary, when the button is pressed, VCC will be connected (high levels), When we move the joystick, the internal potentiometer will adjust to output different voltages, and we can read the analog value.

![](./media/efcb8ed421ab3572af890d73788a8c01.jpeg)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.40139in;height:0.76458in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/1f5bf5d8d48c675b98dd2cbfca6c31b7.png" style="width:1.18819in;height:0.63681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/fc3fd9c0110b04d1af77a2ff8c01a10a.png" style="width:0.95208in;height:0.39931in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Joystick Module*1</td>
<td>5P Dupont Wire*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/8f2094524e2a560df485e13786667d28.png)

**5. Run the Test Code**

Find and double-click **joystick\.py**, then click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png)to run the code.

![](./media/4ced85ed211aa4c740912ca3a0fd37d8.png)

**6. Code Explanation**

In the experiment, according to the wiring diagram, the x pin is set to GP26, the y pin is set to GP27 and the pin of the joystick is set to GP22. Teen the serial monitor displays the test data.

**7. Test Result**

Upload the code power up by a USB cable, the serial monitor will show the corresponding value. Move the joystick, the analog value of X axis and Y axis will change. Press the button, the digital value is 1, on the contrary is 0. as shown below;

![](./media/09b1c8c019a19f7b413cba9f1b76115f.jpeg)

![](./media/77338b29ddcce857e2cd2102d54f8292.png)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 26
 * Joystick
 * http://www.keyestudio.com
'''
import machine
import utime

B = machine.Pin(22, machine.Pin.IN)
X = machine.ADC(26)
Y = machine.ADC(27)
while True:
    B_value = B.value()
    X_value = X.read_u16()
    Y_value = Y.read_u16()
    print("button:", end = " ")
    print(B_value, end = " ")
    print("X:", end = " ")
    print(X_value, end = " ")
    print("Y:", end = " ")
    print(Y_value)
    utime.sleep(0.1)
```


### Project 26: Ultraviolet Sensor

![](./media/73df098dc8f87602650d64810bacad7a.png)

**1. Description**

There is a ultraviolet Sensor used for UV index monitoring, UV radiation dose measurement, flame detection. Suitable for measuring UV index of smart wearable devices, such as UV index detection of watches, smartphones and outdoor equipment. It can also be used to monitor the intensity of UV light, or as a UV flame detector when UV sanitizing items. The sensor has a specific spectral response. In the experiment, we use the purple led module to test the UV module, and then display the
results on the shell.

**2. Working Principle**

The output current of the UV sensor is proportional to the light intensity, and the output of the product has a very high consistency. The module circuit has been set up, and we directly use the ADC to collect the analog signal.

![](./media/0e7090143ee1a22480310d289d03faa2.png)

**3. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.3375in;height:0.72986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/4380c0a29b5226e64113a5b4e7f7a62d.png" style="width:0.82361in;height:0.61389in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.72014in;height:0.38611in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/12ecb079cf6481a6f0f04d6b7bb31fd8.png" style="width:0.8417in;height:0.63889in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio Ultraviolet Sensor*1</td>
<td>3P Dupont Wire*2</td>
<td>Micro USB Cable*1</td>
<td>Keyestudio DIY Purple LED*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/0394987102b736d2f122daf2e3ef55f7.png)

**(V of led module is connected to VUSB(5V) to make the LED brighter)**

**5. Run the test code**

Find and double **Ultraviolet\.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/c79e02ba393437ddd578128244fc336a.png)

**6. Code Explanation**

We first light up the purple LED, and then use it to illuminate the UV module to see the changes in the data on the serial monitor.

**7. Test Result**

Upload the test code and open the serial monitor. When we make the purple LED close to the ultraviolet module, view the data on the monitor, as shown below:

![](./media/b79ec44bc42cbad6ff70d2fda323566f.jpeg)

![](./media/3015106b0abda4e9124a773add3b1e1b.png)

**8. Test code**

```Python
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
led.value(1)#light up LED

while True:
    analogVal = sensor.read_u16()
    print(analogVal)
    utime.sleep(0.1)
```


### Project 27: SK6812 RGB Module

![](./media/effda831f7c06cea2c443d8352f1a693.jpeg)

**1. Overview**

In previous lessons, we learned about the plug-in RGB module and used PWM signals to color the three pins of the module.

There is a Keyestudio 6812 RGB module whose the driving principle is different from the plug-in RGB module. It can only control with one pin. This is a set. It is an intelligent externally controlled LED light source with the control circuit and the light-emitting circuit. Each LED element is the same as a 5050 LED lamp bead, and each component is a pixel. There are four lamp beads on the module, which indicates four pixels.

In the experiment, we make different lights show different colors.

**2. Working Principle**

From the schematic diagram, we can see that these four pixel lighting beads are all connected in series. In fact, no matter how many they are, we can use a pin to control a light and let it display any color. The pixel point contains a data latch signal shaping amplifier drive circuit, a high-precision internal oscillator and a 12V high-voltage programmable constant current control part, which effectively ensures the color of the pixel point light is highly consistent.

The data protocol adopts a single-wire zero-code communication method. After the pixel is powered up and reset, the S terminal receives the data transmitted from the controller. The first 24bit data sent is extracted by the first pixel and sent to the data latch of the pixel.

![](./media/f0d824a10a88aa0fbabfb685634672fc.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.44167in;height:0.78681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/42e093202e7233aaaa42b9ac64f51d98.png" style="width:0.96111in;height:0.675in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio 6812 RGB Module*1</td>
<td>3P Dupont Wire*1</td>
<td><p>MicroUSB</p>
<p>Cable*1</p></td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/25f4d0f5d90c89ed44e61fd160c34e63.png)

**5. Run the test code**

Find and double-click **sk6812\.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/8e2046e81c70889be4142f0ddb806340.png)

**6. Code Explanation**

**NUM\_LEDS = 4**，there are four light beads, therefore, we set to 4.

**PIN\_NUM = 16**，this is the pin number, we connect to GP16, can be changeable.

**brightness = 0.1**，this is the brightness setting, number 1 is the brightest.

**pixels\_show()**，this function is used to refresh and display.

**pixels\_set(i, color)**，this function is sued to set up the location of 6812RGB.

**pixels\_fill(color)**，display colors of all light beads.

**7. Test Result**

Upload the code, wire up according to connection diagrams and power on. Then we can see the light beads on the module show red, green, blue and white color, as shown below.

![](./media/54dbbf925443f58cbdaab221f682a429.jpeg)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 27
 * 6812 RGB LED
 * http://www.keyestudio.com
'''
import array, time
from machine import Pin
import rp2
 
# Configure the number of sk6812 LEDs, pins and brightness.
NUM_LEDS = 4
PIN_NUM = 16
brightness = 0.1
 
 
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def sk6812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()
 

# Create the StateMachine with the sk6812 program, outputting on Pin(16).
sm = rp2.StateMachine(0, sk6812, freq=8_000_000, sideset_base=Pin(PIN_NUM))
 
# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)
 
# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])
 
def pixels_show():
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g<<16) + (r<<8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(10)
 
def pixels_set(i, color):
    ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]
 
def pixels_fill(color):
    for i in range(len(ar)):
        pixels_set(i, color)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pixels_set(0, RED)
pixels_set(1, GREEN)
pixels_set(2, BLUE)
pixels_set(3, WHITE)
pixels_show()
time.sleep(5)
'''
for i in range(len(ar)):
    pixels_set(i, BLACK)
pixels_show()
'''
```


### Project 28: Rotary Encoder

![](./media/ec37b336b8f5620b62b04224b132840a.jpeg)

**1. Overview**

In this kit, there is a Keyestudio rotary encoder, dubbed as switch encoder. It is applied to automotive electronics, multimedia audio, instrumentation, household appliances, smart home, medical equipment and so on.

In the experiment, it it used for counting. When we rotate the rotary encoder clockwise, the set data falls by 1; if you rotate it anticlockwise, the set data is up 1; and when the middle button is pressed, the value will be show on Shell.

**2. Working Principle**

The incremental encoder converts the displacement into a periodic electric signal, and then converts this signal into a counting pulse, and the number of pulses indicates the size of the displacement. This module mainly uses 20-pulse rotary encoder components. It can calculate the number of pulses output during clockwise and reverse rotation. There is no limit to count rotation. It resets to the initial state, that is, starts counting from 0.

![](./media/2fb56ec6fa69e66fcca4243617d4b18c.jpeg)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.44514in;height:0.78819in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/9c5120f144225e1acee628a6870b671d.png" style="width:0.97778in;height:0.63333in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/fc3fd9c0110b04d1af77a2ff8c01a10a.png" style="width:0.95208in;height:0.39931in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.94722in;height:0.41875in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Rotary Encoder*1</td>
<td>5P Dupont Wire*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/be52de6cb96ad45601f2bae496b227a3.png)

**5. Run the test code**

Find and double-click **encoder\.py** to open it, then click
![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the code.

![](./media/abb1c23443681de8f57b98c6874d7097.png)

This is because we did not import the module needed by the encoder. We have mentioned how to import modules before, please refer to the previous method.

We save the code below to the Pico with the name of **rotary\.py**.

```Python
# The MIT License (MIT)
# Copyright (c) 2020 Mike Teachman
# https://opensource.org/licenses/MIT

# Platform-independent MicroPython code for the rotary encoder module

# Documentation:
#   https://github.com/MikeTeachman/micropython-rotary

import micropython

_DIR_CW = const(0x10)  # Clockwise step
_DIR_CCW = const(0x20)  # Counter-clockwise step

# Rotary Encoder States
_R_START = const(0x0)
_R_CW_1 = const(0x1)
_R_CW_2 = const(0x2)
_R_CW_3 = const(0x3)
_R_CCW_1 = const(0x4)
_R_CCW_2 = const(0x5)
_R_CCW_3 = const(0x6)
_R_ILLEGAL = const(0x7)

_transition_table = [

    # |------------- NEXT STATE -------------|            |CURRENT STATE|
    # CLK/DT    CLK/DT     CLK/DT    CLK/DT
    #   00        01         10        11
    [_R_START, _R_CCW_1, _R_CW_1,  _R_START],             # _R_START
    [_R_CW_2,  _R_START, _R_CW_1,  _R_START],             # _R_CW_1
    [_R_CW_2,  _R_CW_3,  _R_CW_1,  _R_START],             # _R_CW_2
    [_R_CW_2,  _R_CW_3,  _R_START, _R_START | _DIR_CW],   # _R_CW_3
    [_R_CCW_2, _R_CCW_1, _R_START, _R_START],             # _R_CCW_1
    [_R_CCW_2, _R_CCW_1, _R_CCW_3, _R_START],             # _R_CCW_2
    [_R_CCW_2, _R_START, _R_CCW_3, _R_START | _DIR_CCW],  # _R_CCW_3
    [_R_START, _R_START, _R_START, _R_START]]             # _R_ILLEGAL

_transition_table_half_step = [
    [_R_CW_3,            _R_CW_2,  _R_CW_1,  _R_START],
    [_R_CW_3 | _DIR_CCW, _R_START, _R_CW_1,  _R_START],
    [_R_CW_3 | _DIR_CW,  _R_CW_2,  _R_START, _R_START],
    [_R_CW_3,            _R_CCW_2, _R_CCW_1, _R_START],
    [_R_CW_3,            _R_CW_2,  _R_CCW_1, _R_START | _DIR_CW],
    [_R_CW_3,            _R_CCW_2, _R_CW_3,  _R_START | _DIR_CCW]]

_STATE_MASK = const(0x07)
_DIR_MASK = const(0x30)


def _wrap(value, incr, lower_bound, upper_bound):
    range = upper_bound - lower_bound + 1
    value = value + incr

    if value < lower_bound:
        value += range * ((lower_bound - value) // range + 1)

    return lower_bound + (value - lower_bound) % range


def _bound(value, incr, lower_bound, upper_bound):
    return min(upper_bound, max(lower_bound, value + incr))


def _trigger(rotary_instance):
    for listener in rotary_instance._listener:
        listener()


class Rotary(object):

    RANGE_UNBOUNDED = const(1)
    RANGE_WRAP = const(2)
    RANGE_BOUNDED = const(3)

    def __init__(self, min_val, max_val, reverse, range_mode, half_step):
        self._min_val = min_val
        self._max_val = max_val
        self._reverse = -1 if reverse else 1
        self._range_mode = range_mode
        self._value = min_val
        self._state = _R_START
        self._half_step = half_step
        self._listener = []

    def set(self, value=None, min_val=None,
            max_val=None, reverse=None, range_mode=None):
        # disable DT and CLK pin interrupts
        self._hal_disable_irq()

        if value is not None:
            self._value = value
        if min_val is not None:
            self._min_val = min_val
        if max_val is not None:
            self._max_val = max_val
        if reverse is not None:
            self._reverse = -1 if reverse else 1
        if range_mode is not None:
            self._range_mode = range_mode
        self._state = _R_START

        # enable DT and CLK pin interrupts
        self._hal_enable_irq()

    def value(self):
        return self._value

    def reset(self):
        self._value = 0

    def close(self):
        self._hal_close()

    def add_listener(self, l):
        self._listener.append(l)

    def remove_listener(self, l):
        if l not in self._listener:
            raise ValueError('{} is not an installed listener'.format(l))
        self._listener.remove(l)
        
    def _process_rotary_pins(self, pin):
        old_value = self._value
        clk_dt_pins = (self._hal_get_clk_value() <<
                       1) | self._hal_get_dt_value()
        # Determine next state
        if self._half_step:
            self._state = _transition_table_half_step[self._state &
                                                      _STATE_MASK][clk_dt_pins]
        else:
            self._state = _transition_table[self._state &
                                            _STATE_MASK][clk_dt_pins]
        direction = self._state & _DIR_MASK

        incr = 0
        if direction == _DIR_CW:
            incr = 1
        elif direction == _DIR_CCW:
            incr = -1

        incr *= self._reverse

        if self._range_mode == self.RANGE_WRAP:
            self._value = _wrap(
                self._value,
                incr,
                self._min_val,
                self._max_val)
        elif self._range_mode == self.RANGE_BOUNDED:
            self._value = _bound(
                self._value,
                incr,
                self._min_val,
                self._max_val)
        else:
            self._value = self._value + incr

        try:
            if old_value != self._value and len(self._listener) != 0:
                micropython.schedule(_trigger, self)
        except:
            pass
```


Save the following code in pico and name **rotary\_irq\_rp2.py** .

```Python
# The MIT License (MIT)
# Copyright (c) 2020 Mike Teachman
# Copyright (c) 2021 Eric Moyer
# https://opensource.org/licenses/MIT

# Platform-specific MicroPython code for the rotary encoder module
# Raspberry Pi Pico implementation

# Documentation:
#   https://github.com/MikeTeachman/micropython-rotary

from machine import Pin
from rotary import Rotary

IRQ_RISING_FALLING = Pin.IRQ_RISING | Pin.IRQ_FALLING


class RotaryIRQ(Rotary):
    def __init__(
        self,
        pin_num_clk,
        pin_num_dt,
        min_val=0,
        max_val=10,
        reverse=False,
        range_mode=Rotary.RANGE_UNBOUNDED,
        pull_up=False,
        half_step=False,
    ):
        super().__init__(min_val, max_val, reverse, range_mode, half_step)

        if pull_up:
            self._pin_clk = Pin(pin_num_clk, Pin.IN, Pin.PULL_UP)
            self._pin_dt = Pin(pin_num_dt, Pin.IN, Pin.PULL_UP)
        else:
            self._pin_clk = Pin(pin_num_clk, Pin.IN)
            self._pin_dt = Pin(pin_num_dt, Pin.IN)

        self._hal_enable_irq()

    def _enable_clk_irq(self):
        self._pin_clk.irq(self._process_rotary_pins, IRQ_RISING_FALLING)

    def _enable_dt_irq(self):
        self._pin_dt.irq(self._process_rotary_pins, IRQ_RISING_FALLING)

    def _disable_clk_irq(self):
        self._pin_clk.irq(None, 0)

    def _disable_dt_irq(self):
        self._pin_dt.irq(None, 0)

    def _hal_get_clk_value(self):
        return self._pin_clk.value()

    def _hal_get_dt_value(self):
        return self._pin_dt.value()

    def _hal_enable_irq(self):
        self._enable_clk_irq()
        self._enable_dt_irq()

    def _hal_disable_irq(self):
        self._disable_clk_irq()
        self._disable_dt_irq()

    def _hal_close(self):
        self._hal_disable_irq()
```

After that, these two modules will be shown on the left side. Then open **encoder\.py** again to run the code, it works.

![](./media/7fdd13e932dbbcc5e7f44ac2f2a49b8e.png)

**6. Code Explanation**

**SW=Pin(20,Pin\.IN, Pin.PULL\_UP)** means the pin of SW is connected to GP20, **pin\_num\_clk=18** shows that CLK is connected to GP18.

**pin\_num\_dt=19** indicates that DT is linked with GP19. These pins can be changed.

**try/except** is used to process the abnormal language of Python, **try** is the executable code. Press Ctrl+C to exit program.

**r.value()** returns the values of the encoder.

**7. Test Result**

Upload the code, rotate the knob on the rotary encoder clockwise, the displayed data will decrease; in contrast, rotate the knob anticlockwise, the data will rise. Equally, press the button on the rotary encoder.

![](./media/16059602dfb1130f170a2f2e8f468038.jpeg)

![](./media/a347fb4aea44c64f4b22515d5b318945.png)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 28
 * Encoder
 * http://www.keyestudio.com
'''
import time
from rotary_irq_rp2 import RotaryIRQ
from machine import Pin
SW=Pin(20,Pin.IN,Pin.PULL_UP)
r = RotaryIRQ(pin_num_clk=18,
              pin_num_dt=19,
              min_val=0,
              reverse=False,
              range_mode=RotaryIRQ.RANGE_UNBOUNDED)
val_old = r.value()
while True:
    try:
        val_new = r.value()
        if SW.value()==0 and n==0:
            print("Button Pressed")
            print("Selected Number is : ",val_new)
            n=1
            while SW.value()==0:
                continue
        n=0
        if val_old != val_new:
            val_old = val_new
            print('result =', val_new)
        time.sleep_ms(50)
    except KeyboardInterrupt:
        break
```


### Project 29: Servo Control

![](./media/165f16e47a832fc4dcaea6e4a1c11194.jpeg)

**1. Overview**

Servo motor is a position control rotary actuator. It mainly consists of a housing, a circuit board, a core-less motor, a gear and a position sensor. Its working principle is that the servo receives the signal sent by MCU or receiver and produces a reference signal with a period of 20ms and width of 1.5ms, then compares the acquired DC bias voltage to the voltage of the potentiometer and obtain the voltage difference output.

In general, servo has three lines in brown, red and orange. The brown wire is grounded, the red one is a positive pole line and the orange one is a signal line.

![](./media/4b15604cd8a82aeb39497c7544b39f93.emf)

![](./media/3366fe332bcf286659f9bf21a8cf880f.png)

**2. Working Principle**

When the motor speed is constant, the potentiometer is driven to rotate through the cascade reduction gear, which leads that the voltage difference is 0, and the motor stops rotating. Generally, the angle range of servo rotation is 0° --180 °

The rotation angle of servo motor is controlled by regulating the duty cycle of PWM (Pulse-Width Modulation) signal. The standard cycle of PWM signal is 20ms (50Hz). Theoretically, the width is distributed between 1ms-2ms, but in fact, it's between 0.5ms-2.5ms. The width corresponds the rotation angle from 0° to 180°. But note that for different brand motors, the same signal may have different rotation angles. 

![](./media/b4993212773e13b1a4424b3d7ef41ab6.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.12292in;height:0.44514in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.44375in;height:0.78819in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9a96e60ed3aee985db5d4dcaf9bf38b.png" style="width:1.05833in;height:1.05069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Servo*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/a3bd832d331618aa588e222b097ab0e5.png)

**5. Run the Test Code**

Find **Servo test 1\.py** and **Servo test 2\.py** , double-click to open them. Then click ![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the code.

![](./media/8e32f071c4b4bc412b35b5e27ac75e9f.png)

**6. Code Explanation**

Code 1:

Convert to duty cycle according to the angle of the signal pulse width, the formula is: 2.5+angle/180\*10, taking the pin resolution of PWM of Pico as an example, 2^16 = 65535, when converted to 0 degree, the duty cycle value is 65535 \* 2.5% = 1638.375, when the angle is 180 degrees, its duty cycle value is 65535 \* 12.5% = 8191.875, these two values will be related to the program, considering the error and rotation angle, I will set the duty cycle at 1000 and 9000 to make servo rotate by 0\~180 degrees.

Code 2:

**convert(x, i\_m, i\_M, o\_m, o\_M)：X is the value we will map.**

i\_m, i\_M is the lower limit and upper limit of the current value；o\_m, o\_M is

the lower limit and upper limit of the object range.

For instance, **convert(degree, 0, 180, 1000, 9000)**

Rotation angle degree is in the range of 0° and 180°. The duty cycle we will map is in the range of 1000 and 9000.

**7. Test Result:**

Test Result 1:

Upload the code1，the servo will rotate 0°，90° and 180°.

Test Result 2:

Upload the code2, the servo will rotate from 0° to 180° and move 1° for each 10ms.

![](./media/cfa5e9e40f26e2094abc652d78750119.jpeg)

**8. Test Code**

Test Code1:


```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 29.1
 * Servo test 1
 * http://www.keyestudio.com
'''
from machine import Pin, PWM
import time
pwm = PWM(Pin(0))
pwm.freq(50)

'''
Duty cycle of some angles
0°----2.5%----1638
45°----5%----3276
90°----7.5%----4915
135°----10%----6553
180°----12.5%----8192
'''
angle_0 = 1638
angle_90 = 4915
angle_180 = 8192

while True:
    pwm.duty_u16(angle_0)
    time.sleep(1)
    pwm.duty_u16(angle_90)
    time.sleep(1)
    pwm.duty_u16(angle_180)
    time.sleep(1)
```


Test Code2:


```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 29.2
 * Servo test 2
 * http://www.keyestudio.com
'''
from utime import sleep
from machine import Pin
from machine import PWM

pwm = PWM(Pin(0))#Connect servo to pin GP0
pwm.freq(50)#the cycle is 20ms, so the frequency equals 50Hz
'''
Duty cycle of some angles
0°----2.5%----1638
45°----5%----3276
90°----7.5%----4915
135°----10%----6553
180°----12.5%----8192
In consideration of errors, allocate the duty cycle within 1000~9000, so that the servo is able to rotate from 0° to 180°
'''
# set the rotation angle of the servo
def setServoCycle (position):
    pwm.duty_u16(position)
    sleep(0.01)

# convert the angle into duty cycle
def convert(x, i_m, i_M, o_m, o_M):
    return max(min(o_M, (x - i_m) * (o_M - o_m) // (i_M - i_m) + o_m), o_m)

while True:
    for degree in range(0, 180, 1):#rotate from 0° to 180°
        pos = convert(degree, 0, 180, 1000, 9000)
        setServoCycle(pos)

    for degree in range(180, 0, -1):#rotate from 180° to 0°
        pos = convert(degree, 0, 180, 1000, 9000)
        setServoCycle(pos)
```

### Project 30: Ultrasonic Sensor

**1. Overview**

In this kit, there is a keyes HC-SR04 ultrasonic sensor, which can detect obstacles in front and the detailed distance between the sensor and the obstacle. Its principle is the same as that of bat flying. It can emit the ultrasonic signals that cannot be heard by humans. When these signals hit an obstacle and come back immediately. The distance between the sensor and the obstacle can be calculated by the time gap of emitting signals and receiving signals.

In the experiment, we use the sensor to detect the distance between the sensor and the obstacle, and print the test result.

**2. Working Principle**

The most common ultrasonic ranging method is the echo detection. As shown below; when the ultrasonic emitter emits the ultrasonic waves towards certain direction, the counter will count. The ultrasonic waves travel and reflect back once encountering the obstacle. Then the counter will stop counting when the receiver receives the ultrasonic waves coming back.

The ultrasonic wave is also sound wave, and its speed of sound V is related to temperature. Generally, it travels 340m/s in the air.
According to time t, we can calculate the distance s from the emitting spot to the obstacle.

s=340t/2.

The HC-SR04 ultrasonic ranging module can provide a non-contact distance sensing function of 2cm-400cm, and the ranging accuracy can reach as high as 3mm; the module includes an ultrasonic transmitter, receiver and control circuit. Basic working principle:

1\. First pull down the TRIG, and then trigger it with at least 10us high level signal;

2\. After triggering, the module will automatically transmit eight 40KHZ square waves, and automatically detect whether there is a signal to return.

3\. If there is a signal returned back, through the ECHO to output a high level, the duration time of high level is actually the time from emission to reception of ultrasonic.

![](./media/686176f637ba288e3b20d63bb1054477.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.40417in;height:0.76667in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/1a1dc36771654248ade08b9d9f115f57.png" style="width:0.92292in;height:0.50903in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio SR01 Ultrasonic Sensor*1</td>
<td>4P Dupont Wire*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/43d54e1cb123332f30da8af5240f4b28.png)

**5. Run the test code**

Find and double-click **ultrasonic\.py** to open it, then click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png)to run the code.

![](./media/274e42f006196beae249a65819115c22.png)

**6. Code Explanation**

HC-SR04 ultrasonic sensor can detect the maximum distance of 3 to 4m, the minimum is 2cm. The shell displays the distance between the sensor and the obstacle in cm.

**utime.ticks\_us()** returns the time the program has been running until now.

**7. Test Result**

Upload the code. The distance between the ultrasonic sensor and the obstacle is shown on Shell.

![](./media/53d036683d58fc57b75712c05bcebc3c.jpeg)

![](./media/fe8803ec6f12ae39ade8586c5627d48e.png)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 30
 * Ultrasonic
 * http://www.keyestudio.com
'''
from machine import Pin
import utime

# detect the distance by ultrasonic wave, unit: cm
def getDistance(trigger, echo):
    # generate a square wave of 10us
    trigger.low()   #begin with a short low level to ensure that the high pluse is clear
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)#After the power level is pulled up, wait 10ms, then set to low level immediately
    trigger.low()
    
    while echo.value() == 0: #while loop, detect whether the value is 0 at the echo pin, record the time
        start = utime.ticks_us()
    while echo.value() == 1: #while loop, detect whether the value is 1 at the echo pin, record the time
        end = utime.ticks_us()
    d = (end - start) * 0.0343 / 2 #distance = duration(from echo being detected to wave being sent) x velocity of sound (343.2 m/s, or 0.0343cm/ms) / 2, why devided by 2: the wave made a return
    return d

# set the pin
trigger = Pin(14, Pin.OUT)
echo = Pin(13, Pin.IN)
# major codes
while True:
    distance = getDistance(trigger, echo)
    print("The distance is ：{:.2f} cm".format(distance))
    utime.sleep(0.1)
```


### Project 31: IR Receiver Module

![](./media/80e8f8d8ddc35df9425032ec4ef783ee.png)

**1. Overview**

There is no doubt that infrared remote control is ubiquitous in daily life. It is used to control various household appliances, such as TVs, stereos, video recorders and satellite signal receivers. Infrared remote control is composed of infrared transmitting and infrared receiving systems, that is, an infrared remote control and infrared receiving module and a single-chip microcomputer capable of decoding.​    

In this experiment, we need to know how to use the infrared receiving sensor. The infrared receiving sensor mainly uses the VS1838B infrared receiving sensor element. It integrates receiving, amplifying, and demodulating. The internal IC has already completed the demodulation, and the output is a digital signal. It can receive 38KHz modulated remote control signal. In the experiment, we use the IR receiver to receive the infrared signal emitted by the external infrared transmitting device, and display the received signal in the shell.

**2. Working Principle**

![](./media/845973091e7fe407e7fa0e96fc1cf4f1.png)

The main part of the IR remote control system is modulation, transmission and reception. The modulated carrier frequency is generally between 30khz and 60khz, and most of them use a square wave of 38kHz and a duty ratio of 1/3. A 4.7K pull-up resistor R3 is added to the signal end of the infrared receiver.

![](./media/447c2e4321968e2134d6f960db8dc880.png)

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:0.88611in;height:0.35069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:0.97431in;height:0.53194in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/06218167222e41c71cdcec1c9dc08982.png" style="width:0.94444in;height:0.65139in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.97778in;height:0.52431in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/08f9ae39d0574640551287ef401e9cfc.png" style="width:0.87986in;height:0.425in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td><p>Keyestudio DIY</p>
<p>IR Receiver *1</p></td>
<td>3P Dupont Wire*1</td>
<td><p>Micro</p>
<p>USB Cable*1</p></td>
<td>Remote Control*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/308cd89f930bb7478d8ef9355bb1a844.png)

**5. Run the test code：**

Double-click **IR receive\.py**，and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png)to run the code

![](./media/8898f6242853747160e7adffeb8b13b2.png)

**6. Code Explanation：**

**read\_ircode(ird):** keys returning corresponds to keys on the remote control.

**7. Test Result：**

Get a remote control and pull out the insolation chip. Point at the IR receiver and press keys on the IR remote control. Then the LED on the IR receiver will flash, as shown below;

![](./media/f87982fa083af748526f99f3032b8735.jpeg)

![](./media/b39cc89ea61b4a680f90fd4be9cb07bc.png)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 31
 * IR Receiver
 * http://www.keyestudio.com
'''
import utime
from machine import Pin

ird = Pin(16,Pin.IN)

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
        start = utime.ticks_us()
        while ird.value() == 0:
            ms1 = utime.ticks_us()
        diff = utime.ticks_diff(ms1,start)
        seq0.append(diff)
        while ird.value() == 1 and complete == 0:
            ms2 = utime.ticks_us()
            diff = utime.ticks_diff(ms2,ms1)
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

while True:
    command = read_ircode(ird)
    print(command)
    utime.sleep(0.5)
```

### Project 32: DS18B20 Temperature Sensor

![](./media/29c66f83d6ea8bbc378b0508e78d5f3b.png)

**1. Description**

The DS18B20 is a 1-wire programmable Temperature sensor from maxim integrated. It is widely used to measure temperature in hard environments like in chemical solutions, mines or soil etc. The constriction of the sensor is rugged and also can be purchased with a waterproof option making the mounting process easy. It can measure a wide range of temperature from **-55°C to +125°** with a decent accuracy of **±5°C**. Each sensor has a unique address and requires only one pin of the MCU to transfer data so it a very good choice for measuring temperature at multiple points without compromising much of your digital pins on the microcontroller.

**2. Working Principle**

![](./media/eef2d84a2ad003d15575726341de52bf.png)

The hardware interface of the 1-Wire bus is very simple, just connect the data pin of the DS18B20 to an IO port of the microcontroller. The timing of the 1-Wire bus is relatively complex. Many students can’t understand the timing diagram independently here. We have encapsulated the complex timing operations in the library, and you can use the
library functions directly.

Schematic Diagram of DS18B20

This can save up to 12-bit temperature vale. In the register, save in code complement. As shown below;

![](./media/bffba8c519ff6e0310882d0712be9177.png)

A total of 2 bytes, LSB is the low byte, MSB is the high byte, where MSb is the high byte of the byte, LSb is the low byte of the byte. As you can see, the binary number, the meaning of the temperature represented by each bit, is expressed. Among them, S represents the sign bit, and the lower 11 bits are all powers of 2, which are used to represent the final temperature. The temperature measurement range of DS18B20 is from -55 degrees to +125 degrees, and the expression form of temperature
data, S represents positive and negative temperature, and the resolution is 2﹣⒋, which is 0.0625.

**3. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.44167in;height:0.78681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/d892bdfa25f3544ae28aa16d8b1b3c50.png" style="width:0.98056in;height:0.73542in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio DIY 18B20 Temperature Sensor*1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Connection Diagram**

![](./media/49142e4db454acf9dea15dc094038a0d.png)

**5. Run the test code**

Import the 18B20 module，save the test code in the pico and name **onewire\.py**.

```Python
# 1-Wire driver for MicroPython
# MIT license; Copyright (c) 2016 Damien P. George

import _onewire as _ow


class OneWireError(Exception):
    pass


class OneWire:
    SEARCH_ROM = 0xF0
    MATCH_ROM = 0x55
    SKIP_ROM = 0xCC

    def __init__(self, pin):
        self.pin = pin
        self.pin.init(pin.OPEN_DRAIN, pin.PULL_UP)

    def reset(self, required=False):
        reset = _ow.reset(self.pin)
        if required and not reset:
            raise OneWireError
        return reset

    def readbit(self):
        return _ow.readbit(self.pin)

    def readbyte(self):
        return _ow.readbyte(self.pin)

    def readinto(self, buf):
        for i in range(len(buf)):
            buf[i] = _ow.readbyte(self.pin)

    def writebit(self, value):
        return _ow.writebit(self.pin, value)

    def writebyte(self, value):
        return _ow.writebyte(self.pin, value)

    def write(self, buf):
        for b in buf:
            _ow.writebyte(self.pin, b)

    def select_rom(self, rom):
        self.reset()
        self.writebyte(self.MATCH_ROM)
        self.write(rom)

    def scan(self):
        devices = []
        diff = 65
        rom = False
        for i in range(0xFF):
            rom, diff = self._search_rom(rom, diff)
            if rom:
                devices += [rom]
            if diff == 0:
                break
        return devices

    def _search_rom(self, l_rom, diff):
        if not self.reset():
            return None, 0
        self.writebyte(self.SEARCH_ROM)
        if not l_rom:
            l_rom = bytearray(8)
        rom = bytearray(8)
        next_diff = 0
        i = 64
        for byte in range(8):
            r_b = 0
            for bit in range(8):
                b = self.readbit()
                if self.readbit():
                    if b:  # there are no devices or there is an error on the bus
                        return None, 0
                else:
                    if not b:  # collision, two devices with different bit meaning
                        if diff > i or ((l_rom[byte] & (1 << bit)) and diff != i):
                            b = 1
                            next_diff = i
                self.writebit(b)
                if b:
                    r_b |= 1 << bit
                i -= 1
            rom[byte] = r_b
        return rom, next_diff

    def crc8(self, data):
        return _ow.crc8(data)
```

Save the code in the pico，and name **ds18x20\.py** .

```Python
# DS18x20 temperature sensor driver for MicroPython.
# MIT license; Copyright (c) 2016 Damien P. George

from micropython import const

_CONVERT = const(0x44)
_RD_SCRATCH = const(0xBE)
_WR_SCRATCH = const(0x4E)


class DS18X20:
    def __init__(self, onewire):
        self.ow = onewire
        self.buf = bytearray(9)

    def scan(self):
        return [rom for rom in self.ow.scan() if rom[0] in (0x10, 0x22, 0x28)]

    def convert_temp(self):
        self.ow.reset(True)
        self.ow.writebyte(self.ow.SKIP_ROM)
        self.ow.writebyte(_CONVERT)

    def read_scratch(self, rom):
        self.ow.reset(True)
        self.ow.select_rom(rom)
        self.ow.writebyte(_RD_SCRATCH)
        self.ow.readinto(self.buf)
        if self.ow.crc8(self.buf):
            raise Exception("CRC error")
        return self.buf

    def write_scratch(self, rom, buf):
        self.ow.reset(True)
        self.ow.select_rom(rom)
        self.ow.writebyte(_WR_SCRATCH)
        self.ow.write(buf)

    def read_temp(self, rom):
        buf = self.read_scratch(rom)
        if rom[0] == 0x10:
            if buf[1]:
                t = buf[0] >> 1 | 0x80
                t = -((~t + 1) & 0xFF)
            else:
                t = buf[0] >> 1
            return t - 0.25 + (buf[7] - buf[6]) / buf[7]
        else:
            t = buf[1] << 8 | buf[0]
            if t & 0x8000:  # sign bit set
                t = -((t ^ 0xFFFF) + 1)
            return t / 16
```

You can view it below then run the **ds18b20\.py**. 

![](./media/992696791c54903b9cf7089ddafa9a8f.png)

**6. Code Explanation**

**time.sleep\_ms(750)** It takes at least 750ms to complete the conversion **ds\_sensor.read\_temp(rom)** is used to read the
temperature value, we set the pin to 3, and the unit of temperature is ℃.

**7. Test Result**

Run the test code, the shell displays the temperature of the current environment, as shown below.

![](./media/164c94bdc5b51b438d373a72b7b8c362.jpeg)

![](./media/b85dd96ba2bb7b6b4ef3f8cecc51a53f.png)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 32
 * DS18B20
 * http://www.keyestudio.com
'''
import machine, onewire, ds18x20, time

ds_pin = machine.Pin(3)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    #print(rom)
    print(ds_sensor.read_temp(rom))
  time.sleep(1)
```


### Project 33: XHT11 Temperature and Humidity Sensor

![](./media/1153b275e0f6c086c9e4225084acf246.png)

**1. Description**

This DHT11 temperature and humidity sensor is a composite sensor which contains a calibrated digital signal output of the temperature and humidity.

DHT11 temperature and humidity sensor uses the acquisition technology of the digital module and temperature and humidity sensing technology, ensuring high reliability and excellent long-term stability.

It includes a resistive element and a NTC temperature measuring device.

![](./media/ac0d6049bc0a5ae8cc515d23b85ecad0.png)

**2. Working Principle**

The communication and synchronization between the single-chip microcomputer and XHT11 adopts the single bus data format. The communication time is about 4ms. The data is divided into fractional part and integer part.

Operation process: A complete data transmission is 40bit, high bit first out. Data format: 8bit humidity integer data + 8bit humidity decimal data + 8bit temperature integer data + 8bit temperature decimal data + 8bit checksum.

8-bit checksum: 8-bit humidity integer data + 8-bit humidity decimal data + 8-bit temperature integer data + 8-bit temperature decimal data "Add the last 8 bits of the result.

**3. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.44167in;height:0.78681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/04f2996e6e2b0d8d4b5158728a23e905.png" style="width:0.88472in;height:0.66875in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio XHT11 Temperature and Humidity Sensor（compatible with DHT11)*1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Connection Diagram**

![](./media/3a4e83e206100aff0ddd3468787bea43.png)

**5. Run the test code**

Import the xht11 module, save it in pico and name **dht\.py** .

```Python
import array

import micropython
import utime
from machine import Pin
from micropython import const


class InvalidChecksum(Exception):
    pass


class InvalidPulseCount(Exception):
    pass


MAX_UNCHANGED = const(100)
MIN_INTERVAL_US = const(200000)
HIGH_LEVEL = const(50)
EXPECTED_PULSES = const(84)


class DHT11:
    _temperature: float
    _humidity: float

    def __init__(self, pin):
        self._pin = pin
        self._last_measure = utime.ticks_us()
        self._temperature = -1
        self._humidity = -1

    def measure(self):
        current_ticks = utime.ticks_us()
        if utime.ticks_diff(current_ticks, self._last_measure) < MIN_INTERVAL_US and (
            self._temperature > -1 or self._humidity > -1
        ):
            # Less than a second since last read, which is too soon according
            # to the datasheet
            return

        self._send_init_signal()
        pulses = self._capture_pulses()
        buffer = self._convert_pulses_to_buffer(pulses)
        self._verify_checksum(buffer)

        self._humidity = buffer[0] + buffer[1] / 10
        self._temperature = buffer[2] + buffer[3] / 10
        self._last_measure = utime.ticks_us()

    @property
    def humidity(self):
        self.measure()
        return self._humidity

    @property
    def temperature(self):
        self.measure()
        return self._temperature

    def _send_init_signal(self):
        self._pin.init(Pin.OUT, Pin.PULL_DOWN)
        self._pin.value(1)
        utime.sleep_ms(50)
        self._pin.value(0)
        utime.sleep_ms(18)

    @micropython.native
    def _capture_pulses(self):
        pin = self._pin
        pin.init(Pin.IN, Pin.PULL_UP)

        val = 1
        idx = 0
        transitions = bytearray(EXPECTED_PULSES)
        unchanged = 0
        timestamp = utime.ticks_us()

        while unchanged < MAX_UNCHANGED:
            if val != pin.value():
                if idx >= EXPECTED_PULSES:
                    raise InvalidPulseCount(
                        "Got more than {} pulses".format(EXPECTED_PULSES)
                    )
                now = utime.ticks_us()
                transitions[idx] = now - timestamp
                timestamp = now
                idx += 1

                val = 1 - val
                unchanged = 0
            else:
                unchanged += 1
        pin.init(Pin.OUT, Pin.PULL_DOWN)
        if idx != EXPECTED_PULSES:
            raise InvalidPulseCount(
                "Expected {} but got {} pulses".format(EXPECTED_PULSES, idx)
            )
        return transitions[4:]

    def _convert_pulses_to_buffer(self, pulses):
        """Convert a list of 80 pulses into a 5 byte buffer

        The resulting 5 bytes in the buffer will be:
            0: Integral relative humidity data
            1: Decimal relative humidity data
            2: Integral temperature data
            3: Decimal temperature data
            4: Checksum
        """
        # Convert the pulses to 40 bits
        binary = 0
        for idx in range(0, len(pulses), 2):
            binary = binary << 1 | int(pulses[idx] > HIGH_LEVEL)

        # Split into 5 bytes
        buffer = array.array("B")
        for shift in range(4, -1, -1):
            buffer.append(binary >> shift * 8 & 0xFF)
        return buffer

    def _verify_checksum(self, buffer):
        # Calculate checksum
        checksum = 0
        for buf in buffer[0:4]:
            checksum += buf
        if checksum & 0xFF != buffer[4]:
            raise InvalidChecksum()
```

Find and double-click **XHT11\.py**，and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/93c24575fff78274bb03d5167108137d.png)

We set the pin to GP22, read the temperature data and the humidity data.

**6. Test Result**

After running the test code, the shell displays the temperature and humidity data, as shown below.

![](./media/75ad83aa7287a0a2a4db0becdf1f833f.jpeg)

![](./media/9d7917c985cad136eceb26fde33f72c7.png)

**7. Test code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 33
 * xht11
 * http://www.keyestudio.com
'''
import machine
import utime
import dht

pin = machine.Pin(22, machine.Pin.OUT, machine.Pin.PULL_DOWN)
sensor = dht.DHT11(pin)

while True:
    print("temperature：{} ℃  humidity：{} %".format(sensor.temperature, sensor.humidity))
    utime.sleep(1)
```

### Project 34: DS1307 Clock Module

![](./media/949abbbea3c8d8b36463768a39a07b51.png)

**1. Overview**

The DS1307 serial real-time clock (RTC) is a low-power, full binary-coded decimal (BCD) clock/calendar plus 56 bytes of NV SRAM.
Address and data are transferred serially through an I2C, bidirectional bus.

The clock/calendar provides seconds, minutes, hours, day, date, month, and year information. The end of the month date is automatically adjusted for months with fewer than 31 days, including corrections for leap year. The clock operates in either the 24-hour or 12-hour format with AM/PM indicator. The DS1307 has a built-in power-sense circuit that detects power failures and automatically switches to the backup supply.

Timekeeping operation continues while the part operates from the backup supply.

**2. Working Principle**

![](./media/92b8dc82b0c2887539bd506639cfbfc0.png)

**3. Detailed address and data:**

Serial real-time clock records year, month, day, hour, minute, second and week; AM and PM indicate morning and afternoon respectively; 56 bytes of NVRAM store data; 2-wire serial port; programmable square wave output; power failure detection and automatic switching circuit; battery current is less than 500mA.

Pins description：

- X1, X2: 32.768kHz crystal terminal ;

- VBAT: +3V input;

- SDA: serial data;

- SCL: serial clock;

- SQW/OUT: square waves/output drivers

![](./media/abdebbfc01cae240e3e81fb188344cbe.png)

**4. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:0.98403in;height:0.39028in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.31042in;height:0.71528in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/44d6a0e867ad07a9a9733ce42a9d488a.png" style="width:0.99208in;height:0.54583in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio DS1307 Clock Module*1</td>
<td>4P Dupont Wire*1</td>
<td><p>Micro USB</p>
<p>Cable*1</p></td>
</tr>
</tbody>
</table>

<br>
<br>

**5. Wiring Diagram**

![](./media/2299493bd97bc28f2f97fb1f71977531.jpeg)

VUSB is 5V，hence the power we use can be connected to VUSB.

**6. Run the test code：**

Double-click **DS1307\.py** and run the test code.

We need to import the clock module.

Save the following code in the pico and name **urtc\.py** .

```Python
import ucollections
import utime


DateTimeTuple = ucollections.namedtuple("DateTimeTuple", ["year", "month",
    "day", "weekday", "hour", "minute", "second", "millisecond"])


def datetime_tuple(year, month, day, weekday=0, hour=0, minute=0,
                   second=0, millisecond=0):
    return DateTimeTuple(year, month, day, weekday, hour, minute,
                         second, millisecond)


def _bcd2bin(value):
    return value - 6 * (value >> 4)


def _bin2bcd(value):
    return value + 6 * (value // 10)


def tuple2seconds(datetime):
    return utime.mktime((datetime.year, datetime.month, datetime.day,
        datetime.hour, datetime.minute, datetime.second, datetime.weekday, 0))


def seconds2tuple(seconds):
    year, month, day, hour, minute, second, weekday, _yday = utime.localtime()
    return DateTimeTuple(year, month, day, weekday, hour, minute, second, 0)


class _BaseRTC:
    def __init__(self, i2c, address=0x68):
        self.i2c = i2c
        self.address = address

    def _register(self, register, buffer=None):
        if buffer is None:
            return self.i2c.readfrom_mem(self.address, register, 1)[0]
        self.i2c.writeto_mem(self.address, register, buffer)

    def _flag(self, register, mask, value=None):
        data = self._register(register)
        if value is None:
            return bool(data & mask)
        if value:
            data |= mask
        else:
            data &= ~mask
        self._register(register, bytearray((data,)))


    def datetime(self, datetime=None):
        buffer = bytearray(7)
        if datetime is None:
            self.i2c.readfrom_mem_into(self.address, self._DATETIME_REGISTER,
                                       buffer)
            return datetime_tuple(
                year=_bcd2bin(buffer[6]) + 2000,
                month=_bcd2bin(buffer[5]),
                day=_bcd2bin(buffer[4]),
                weekday=_bcd2bin(buffer[3]),
                hour=_bcd2bin(buffer[2]),
                minute=_bcd2bin(buffer[1]),
                second=_bcd2bin(buffer[0]),
            )
        datetime = datetime_tuple(*datetime)
        buffer[0] = _bin2bcd(datetime.second)
        buffer[1] = _bin2bcd(datetime.minute)
        buffer[2] = _bin2bcd(datetime.hour)
        buffer[3] = _bin2bcd(datetime.weekday)
        buffer[4] = _bin2bcd(datetime.day)
        buffer[5] = _bin2bcd(datetime.month)
        buffer[6] = _bin2bcd(datetime.year - 2000)
        self._register(self._DATETIME_REGISTER, buffer)

    def alarm_time(self, datetime=None):
        buffer = bytearray(4)
        if datetime is None:
            self.i2c.redfrom_mem_into(self.address, self._ALARM_REGISTER,
                                      buffer)
            return datetime_tuple(
                weekday=_bcd2bin(
                    buffer[3] & 0x7f) if buffer[0] & 0x80 else None,
                day=_bcd2bin(buffer[2] & 0x7f) if buffer[0] & 0x80 else None,
                hour=_bcd2bin(buffer[1] & 0x7f) if buffer[0] & 0x80 else None,
                minute=_bcd2bin(
                    buffer[0] & 0x7f) if buffer[0] & 0x80 else None,
            )
        datetime = datetime_tuple(*datetime)
        buffer[0] = (_bin2bcd(datetime.minute)
                     if datetime.minute is not None else 0x80)
        buffer[1] = (_bin2bcd(datetime.hour)
                     if datetime.hour is not None else 0x80)
        buffer[2] = (_bin2bcd(datetime.day)
                     if datetime.day is not None else 0x80)
        buffer[3] = (_bin2bcd(datetime.weekday) | 0b01000000
                     if datetime.weekday is not None else 0x80)
        self._register(self._ALARM_REGISTER, buffer)


class DS1307(_BaseRTC):
    _NVRAM_REGISTER = 0x08
    _DATETIME_REGISTER = 0x00
    _SQUARE_WAVE_REGISTER = 0x07

    def stop(self, value=None):
        return self._flag(0x00, 0b10000000, value)

    def memory(self, address, buffer=None):
        if buffer is not None and address + len(buffer) > 56:
            raise ValueError("address out of range")
        return self._register(self._NVRAM_REGISTER + address, buffer)

    def alarm_time(self, datetime=None):
        raise NotImplementedError("alarms not available")


class DS3231(_BaseRTC):
    _CONTROL_REGISTER = 0x0e
    _STATUS_REGISTER = 0x0f
    _DATETIME_REGISTER = 0x00
    _ALARM_REGISTER = 0x07
    _SQUARE_WAVE_REGISTER = 0x0e

    def lost_power(self):
        return self._flag(self._STATUS_REGISTER, 0b10000000)

    def alarm(self, value=None):
        return self._flag(self._STATUS_REGISTER, 0b00000011, value)

    def stop(self, value=None):
        return self._flag(self._CONTROL_REGISTER, 0b10000000, value)

    def datetime(self, datetime=None):
        if datetime is not None:
            status = self._register(self._STATUS_REGISTER) & 0b01111111
            self._register(self._STATUS_REGISTER, bytearray((status,)))
        return super().datetime(datetime)


class PCF8523(_BaseRTC):
    _CONTROL1_REGISTER = 0x00
    _CONTROL2_REGISTER = 0x01
    _CONTROL3_REGISTER = 0x02
    _DATETIME_REGISTER = 0x03
    _ALARM_REGISTER = 0x0a
    _SQUARE_WAVE_REGISTER = 0x0f

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init()

    def init(self):
        # Enable battery switchover and low-battery detection.
        self._flag(self._CONTROL3_REGISTER, 0b11100000, False)

    def reset(self):
        self._flag(self._CONTROL1_REGISTER, 0x58, True)
        self.init()

    def lost_power(self, value=None):
        return self._flag(self._CONTROL3_REGISTER, 0b00010000, value)

    def stop(self, value=None):
        return self._flag(self._CONTROL1_REGISTER, 0b00010000, value)

    def battery_low(self):
        return self._flag(self._CONTROL3_REGISTER, 0b00000100)

    def alarm(self, value=None):
        return self._flag(self._CONTROL2_REGISTER, 0b00001000, value)

    def datetime(self, datetime=None):
        if datetime is not None:
            self.lost_power(False) # clear the battery switchover flag
        return super().datetime(datetime)
```

Then run the file **DS1307\.py**：

![](./media/19257a6f787d30659ac19867e9dce418.png)

**7. Code Explanation：**

**rtc.datetime()** returns a array with time. When programming, set“ Enter Please”and run the code. Then we need to input time and date, after inputting, the data will be printed for each second.

**DateTimeTuple\[0\]: save years**

**DateTimeTuple\[1\]: save months**

**DateTimeTuple\[2\]: save days**

**DateTimeTuple\[3\]: save weeks**

**Rtc.GetDateTime().Month(): return months**

**DateTimeTuple\[4\]**: save hours

**DateTimeTuple\[5\]: save minutes**

**DateTimeTuple\[6\]: save seconds**

**8. Test Result：**

Upload the test code, we can see the displayed year, month, day, hour, minute, second and week on the shell, as shown below;

![](./media/d26117195530f8998067ac923eef44d9.jpeg)

![](./media/de5f692e53ac7e7b89a9b9fab8689d02.png)

**9. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 34
 * DS1307 Real Time Clock
 * http://www.keyestudio.com
'''
from machine import I2C, Pin
from urtc import DS1307
import utime

i2c = I2C(1,scl = Pin(15),sda = Pin(14),freq = 400000)
rtc = DS1307(i2c)

year = int(input("Year : "))
month = int(input("month (Jan --> 1 , Dec --> 12): "))
date = int(input("date : "))
day = int(input("day (1 --> monday , 2 --> Tuesday ... 0 --> Sunday): "))
hour = int(input("hour (24 Hour format): "))
minute = int(input("minute : "))
second = int(input("second : "))

now = (year,month,date,day,hour,minute,second,0)
rtc.datetime(now)

#(year,month,date,day,hour,minute,second,p1) = rtc.datetime()
while True:
    DateTimeTuple = rtc.datetime()
    print(DateTimeTuple[0], end = '-')
    print(DateTimeTuple[1], end = '-')
    print(DateTimeTuple[2], end = '  ')
    print(DateTimeTuple[4], end = ':')
    print(DateTimeTuple[5], end = ':')
    print(DateTimeTuple[6], end = '  week:')
    print(DateTimeTuple[3])
    utime.sleep(1)
```


### Project 35: TM1650 4-Digit Tube Display

![](./media/f698ea56391906278b7c8064fca42bb3.jpeg)

**1. Overview**

This module is mainly composed of a 0.36 inch red common anode 4-digit digital tube, and its driver chip is TM1650. When using it, we only need two signal lines to make the single-chip microcomputer control a 4-bit digit tube, which greatly saves the IO port resources of the control board.

TM1650 is a special circuit for LED (light emitting diode display) drive control. It integrates MCU input and output control digital interface, data latch, LED drivers, keyboard scanning, brightness adjustment and other circuits.

TM1650 has stable performance, reliable quality and strong anti-interference ability.

It can be applied to the application of long-term continuous working for 24 hours.

TM1650 uses 2-wire serial transmission protocol for communication (note that this data transmission protocol is not a standard I2C protocol). The chip can drive the digital tube and save MCU pin resources through two pins and MCU communication.

**2. Working Principle**

TM1650 adopts IIC treaty and SDA and SCL wire.

Data command setting is 0x48. This means that lighting up the tube display not perform its button scanning function.

![](./media/c7b895791863dfc2663800ce90f61c89.png)

**Data command setting**: 0x48 means that we light up the digital tube, instead of enable the function of key scanning

![](./media/09585b52bed3d4112d59a611c3c3f262.png)

**Command display setting:**

bit\[6:4\]：set the brightness of tube display, and 000 is brightest

bit\[3\]：set to show decimal points

bit\[0\]：start the display of the tube display

**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.29792in;height:0.70833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/f47b077303226cce504ea7734826dfc9.png" style="width:0.94514in;height:0.52569in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio TM1650 4-Digit Tube Display*1</td>
<td>4P Dupont Wire*1</td>
<td><p>Micro</p>
<p>USB Cable*1</p></td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/fa5d4a6dddd43851d68a6fa82b90d13e.png)

**5. Run the test code：**

Double-click **TM1650\.py** to open the code and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the code.

![](./media/d574e24f3dbc2909c9206b8a47ccf58d.png)

**6. Code Explanation：**

clkPin = 15、dioPin = 14:

the CLK pin is connected to GP15, and the DIO pin is connected to GOP14, we can set any two pins.

**displayBit(bit, num): show** bit(1\~4) and display numbers num(0\~9)

**clearBit(bit):** clear up 1-4 bit display

**setBrightness():** brightness setting

**displayOnOFF():** 0 is OFF，1 is ON

**displayDot(bit, OnOff):** show dismal, 0 is OFF and 1 is ON.

**ShowNum(num):** show the integer num，in the range of 0\~9999

**7. Test Result：**

Run the test code, wire up and power on. The 4-digit tube display will show numbers from 1, add by 1 for each 10ms and increase to 9999 then restart from 0.

![](./media/4c2b3c3bb6c08f4213b4b82d1ea65b13.jpeg)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 35
 * TM1650 Four digital tube
 * http://www.keyestudio.com
'''
from machine import Pin
import time

# definitions for TM1650
ADDR_DIS = 0x48  #mode command
ADDR_KEY = 0x49  #read key value command

# definitions for brightness
BRIGHT_DARKEST = 0
BRIGHT_TYPICAL = 2
BRIGHTEST      = 7

on  = 1
off = 0

# number:0~9
NUM = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f] 
# DIG = [0x68,0x6a,0x6c,0x6e]
DIG = [0x6e,0x6c,0x6a,0x68]
DOT = [0,0,0,0]

clkPin = 15
dioPin = 14
clk = machine.Pin(clkPin, machine.Pin.OUT)
dio = machine.Pin(dioPin, machine.Pin.OUT)

DisplayCommand = 0

def writeByte(wr_data):
    global clk,dio
    for i in range(8):
        if(wr_data & 0x80 == 0x80):
            dio.value(1)
        else:
            dio.value(0)
        clk.value(0)
        time.sleep(0.0001)
        clk.value(1)
        time.sleep(0.0001)
        clk.value(0)
        wr_data <<= 1
    return

def start():
    global clk,dio
    dio.value(1)
    clk.value(1)
    time.sleep(0.0001)
    dio.value(0)
    return
    
def ack():
    global clk,dio
    dy = 0
    clk.value(0)
    time.sleep(0.0001)
    dio = Pin(dioPin, machine.Pin.IN)
    while(dio.value() == 1):
        time.sleep(0.0001)
        dy += 1
        if(dy>5000):
            break
    clk.value(1)
    time.sleep(0.0001)
    clk.value(0)
    dio = Pin(dioPin, machine.Pin.OUT)
    return
    
def stop():
    global clk,dio
    dio.value(0)
    clk.value(1)
    time.sleep(0.0001)
    dio.value(1)
    return
    
def displayBit(bit, num):
    global ADDR_DIS
    if(num > 9 and bit > 4):
        return
    start()
    writeByte(ADDR_DIS)
    ack()
    writeByte(DisplayCommand)
    ack()
    stop()
    start()
    writeByte(DIG[bit-1])
    ack()
    if(DOT[bit-1] == 1):
        writeByte(NUM[num] | 0x80)
    else:
        writeByte(NUM[num])
    ack()
    stop()
    return
    
def clearBit(bit):
    if(bit > 4):
        return
    start()
    writeByte(ADDR_DIS)
    ack()
    writeByte(DisplayCommand)
    ack()
    stop()
    start()
    writeByte(DIG[bit-1])
    ack()
    writeByte(0x00)
    ack()
    stop()
    return
    
    
def setBrightness(b = BRIGHT_TYPICAL):
    global DisplayCommand,brightness
    DisplayCommand = (DisplayCommand & 0x0f)+(b<<4)
    return

def setMode(segment = 0):
    global DisplayCommand
    DisplayCommand = (DisplayCommand & 0xf7)+(segment<<3)
    return
    
def displayOnOFF(OnOff = 1):
    global DisplayCommand
    DisplayCommand = (DisplayCommand & 0xfe)+OnOff
    return

def displayDot(bit, OnOff):
    if(bit > 4):
        return
    if(OnOff == 1): 
        DOT[bit-1] = 1;
    else:
        DOT[bit-1] = 0;
    return
        
def InitDigitalTube():
    setBrightness(2)
    setMode(0)
    displayOnOFF(1)
    for _ in range(4):
        clearBit(_)
    return

def ShowNum(num): #0~9999
    displayBit(1,num%10)
    if(num < 10):
        clearBit(2)
        clearBit(3)
        clearBit(4)
    if(num > 9 and num < 100):
        displayBit(2,num//10%10)
        clearBit(3)
        clearBit(4)
    if(num > 99 and num < 1000):
        displayBit(2,num//10%10)
        displayBit(3,num//100%10)
        clearBit(4)
    if(num > 999 and num < 10000):
        displayBit(2,num//10%10)
        displayBit(3,num//100%10)
        displayBit(4,num//1000)

InitDigitalTube()

while True:
    #displayDot(1,on)     # on or off, DigitalTube.Display(bit,number); bit=1---4  number=0---9
    for i in range(0,9999):
        ShowNum(i)
        time.sleep(0.01)
```


### Project 36: HT16K33\_8X8 Dot Matrix Module

![](./media/431b6c4abd63b99219658a03d24de991.jpeg)

**1. Overview**

What is the dot matrix display?

The 8X8 dot matrix is composed of 64 light-emitting diodes, and each light-emitting diode is placed at the intersection of the row line and the column line. When the corresponding row is set to 1 level, and a certain column is set to 0 level, the corresponding diode will light up.

**2. Working Principle**

As the schematic diagram shown, to light up the LED at the first row and column, we only need to set C1 to high level and R1 to low level. To turn on LEDs at the first row, we set R1 to low level and C1-C8 to high level.

16 IO ports are needed, which will highly waste the MCU resources.

Therefore, we designed this module, using the HT16K33 chip to drive an 8\*8 dot matrix, which greatly saves the resources of the single-chip microcomputer.

There are three DIP switches on the module, all of which are set to I2C communication address. The setting method is shown below.

A0，A1and A2 are grounded, that is, the address is 0x70.

![Img](./media/img-20231026161025.png)


**3. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.34931in;height:0.73611in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/713307c9cb50d067a014dee9522afe15.png" style="width:0.99722in;height:0.49861in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td><p>Keyestudio HT16K33_</p>
<p>8X8 Dot Matrix*1</p></td>
<td>4P Dupont Wire*1</td>
<td><p>Micro USB</p>
<p>Cable*1</p></td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Wiring Diagram**

![](./media/7ff09d536446f1c87fcdcfb75eaf3119.png)

**5. Run the test code：**

Save the following code to pico, import modules, name it as **ht16k33\_matrix.py**：

**ht16k33\_matrix.py**：

```Python
import machine
showbytes = 0
class ht16k33_matrix:

    _HT16K33_BLINK_CMD = const(0x80)
    _HT16K33_BLINK_DISPLAYON = const(0x01)
    _HT16K33_CMD_BRIGHTNESS = const(0xE0)
    _HT16K33_OSCILATOR_ON = const(0x21)
    
    def __init__(self,dt,clk,bus,addr):
        self.addr = addr
        self.i2c = machine.I2C(bus,sda=machine.Pin(dt),scl=machine.Pin(clk))
        self.setup()
        
    def setup(self):
        self.reg_write(_HT16K33_OSCILATOR_ON,0x00) # 00100001 turn on multiplexing
        self.reg_write(_HT16K33_BLINK_CMD | _HT16K33_BLINK_DISPLAYON,0x00)
        self.set_brightness(15)
       
    def show_char(self, c):
        bytes = bytearray()  # Is mutable binary data (byte)
        global showbytes
        for item in c:
            temp = item
            for i in range(8):
                if temp & 0x01:
                    showbytes |= 0x01
                showbytes <<= 1
                temp >>= 1
            bytes.append( ((showbytes & 0xFE)<<0)|((showbytes & 0x01)>>7) )  # Move it to the right, and then say 01
            #bytes.append((item & 0x01)<<7)
            bytes.append(0x00)
        self.i2c.writeto_mem(self.addr, 0x00, bytes)       
    
    def set_brightness(self,brightness):
        self.reg_write(_HT16K33_CMD_BRIGHTNESS | brightness,0x00)

    def reg_write(self, reg, data):
        msg = bytearray()
        msg.append(data)
        self.i2c.writeto_mem(self.addr, reg, msg)
```

Save the code to pico，and name **matrix\_fonts.py** :

```Python
textFont1={
' ':[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    '!':[0x18, 0x3c, 0x3c, 0x18, 0x18, 0x00, 0x18, 0x00],
    '"':[0x66, 0x66, 0x24, 0x00, 0x00, 0x00, 0x00, 0x00],
    '#':[0x6c, 0x6c, 0xfe, 0x6c, 0xfe, 0x6c, 0x6c, 0x00],
    '%':[0x00, 0xc6, 0xcc, 0x18, 0x30, 0x66, 0xc6, 0x00],
    '&':[0x38, 0x6c, 0x38, 0x76, 0xdc, 0xcc, 0x76, 0x00],
    '\'':[0x18, 0x18, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00],
    '(':[0x0c, 0x18, 0x30, 0x30, 0x30, 0x18, 0x0c, 0x00],
    ')':[0x30, 0x18, 0x0c, 0x0c, 0x0c, 0x18, 0x30, 0x00],
    '*':[0x00, 0x66, 0x3c, 0xff, 0x3c, 0x66, 0x00, 0x00],
    '+':[0x00, 0x18, 0x18, 0x7e, 0x18, 0x18, 0x00, 0x00],
    '-':[0x00, 0x00, 0x00, 0x7e, 0x00, 0x00, 0x00, 0x00],
    '.':[0x00, 0x00, 0x00, 0x00, 0x00, 0x18, 0x18, 0x00],
    '/':[0x06, 0x0c, 0x18, 0x30, 0x60, 0xc0, 0x80, 0x00],
    '0':[0x7c, 0xc6, 0xce, 0xd6, 0xe6, 0xc6, 0x7c, 0x00],
    '1':[0x18, 0x38, 0x18, 0x18, 0x18, 0x18, 0x7e, 0x00],
    '2':[0x7c, 0xc6, 0x06, 0x1c, 0x30, 0x66, 0xfe, 0x00],
    '3':[0x7c, 0xc6, 0x06, 0x3c, 0x06, 0xc6, 0x7c, 0x00],
    '4':[0x1c, 0x3c, 0x6c, 0xcc, 0xfe, 0x0c, 0x1e, 0x00],
    '5':[0xfe, 0xc0, 0xc0, 0xfc, 0x06, 0xc6, 0x7c, 0x00],
    '6':[0x38, 0x60, 0xc0, 0xfc, 0xc6, 0xc6, 0x7c, 0x00],
    '7':[0xfe, 0xc6, 0x0c, 0x18, 0x30, 0x30, 0x30, 0x00],
    '8':[0x7c, 0xc6, 0xc6, 0x7c, 0xc6, 0xc6, 0x7c, 0x00],
    '9':[0x7c, 0xc6, 0xc6, 0x7e, 0x06, 0x0c, 0x78, 0x00],
    ':':[0x00, 0x18, 0x18, 0x00, 0x00, 0x18, 0x18, 0x00],
    ';':[0x7c, 0xc6, 0x0c, 0x18, 0x18, 0x00, 0x18, 0x00],
    '<':[0x06, 0x0c, 0x18, 0x30, 0x18, 0x0c, 0x06, 0x00],
    '=':[0x00, 0x00, 0x7e, 0x00, 0x00, 0x7e, 0x00, 0x00],
    '>':[0x60, 0x30, 0x18, 0x0c, 0x18, 0x30, 0x60, 0x00],
    '?':[0x7c, 0xc6, 0x0c, 0x18, 0x18, 0x00, 0x18, 0x00],
    '@':[0x7c, 0xc6, 0xde, 0xde, 0xde, 0xc0, 0x78, 0x00],
    'A':[0x38, 0x6c, 0xc6, 0xfe, 0xc6, 0xc6, 0xc6, 0x00],
    'B':[0xfc, 0x66, 0x66, 0x7c, 0x66, 0x66, 0xfc, 0x00],
    'C':[0x3c, 0x66, 0xc0, 0xc0, 0xc0, 0x66, 0x3c, 0x00],
    'D':[0xf8, 0x6c, 0x66, 0x66, 0x66, 0x6c, 0xf8, 0x00],
    'E':[0xfe, 0x62, 0x68, 0x78, 0x68, 0x62, 0xfe, 0x00],
    'F':[0xfe, 0x62, 0x68, 0x78, 0x68, 0x60, 0xf0, 0x00],
    'G':[0x3c, 0x66, 0xc0, 0xc0, 0xce, 0x66, 0x3a, 0x00],
    'H':[0xc6, 0xc6, 0xc6, 0xfe, 0xc6, 0xc6, 0xc6, 0x00],
    'I':[0x3c, 0x18, 0x18, 0x18, 0x18, 0x18, 0x3c, 0x00],
    'J':[0x1e, 0x0c, 0x0c, 0x0c, 0xcc, 0xcc, 0x78, 0x00],
    'K':[0xe6, 0x66, 0x6c, 0x78, 0x6c, 0x66, 0xe6, 0x00],
    'L':[0xf0, 0x60, 0x60, 0x60, 0x62, 0x66, 0xfe, 0x00],
    'M':[0xc6, 0xee, 0xfe, 0xfe, 0xd6, 0xc6, 0xc6, 0x00],
    'N':[0xc6, 0xe6, 0xf6, 0xde, 0xce, 0xc6, 0xc6, 0x00],
    'O':[0x7c, 0xc6, 0xc6, 0xc6, 0xc6, 0xc6, 0x7c, 0x00],
    'P':[0xfc, 0x66, 0x66, 0x7c, 0x60, 0x60, 0xf0, 0x00],
    'Q':[0x7c, 0xc6, 0xc6, 0xc6, 0xc6, 0xce, 0x7c, 0x0e],
    'R':[0xfc, 0x66, 0x66, 0x7c, 0x6c, 0x66, 0xe6, 0x00],
    'S':[0x7c, 0xc6, 0x60, 0x38, 0x0c, 0xc6, 0x7c, 0x00],
    'T':[0x7e, 0x7e, 0x5a, 0x18, 0x18, 0x18, 0x3c, 0x00],
    'U':[0xc6, 0xc6, 0xc6, 0xc6, 0xc6, 0xc6, 0x7c, 0x00],
    'V':[0xc6, 0xc6, 0xc6, 0xc6, 0xc6, 0x6c, 0x38, 0x00],
    'W':[0xc6, 0xc6, 0xc6, 0xd6, 0xd6, 0xfe, 0x6c, 0x00],
    'X':[0xc6, 0xc6, 0x6c, 0x38, 0x6c, 0xc6, 0xc6, 0x00],
    'Y':[0x66, 0x66, 0x66, 0x3c, 0x18, 0x18, 0x3c, 0x00],
    'Z':[0xfe, 0xc6, 0x8c, 0x18, 0x32, 0x66, 0xfe, 0x00],
    '[':[0x3c, 0x30, 0x30, 0x30, 0x30, 0x30, 0x3c, 0x00],
    '\\':[0xc0, 0x60, 0x30, 0x18, 0x0c, 0x06, 0x02, 0x00],
    ']':[0x3c, 0x0c, 0x0c, 0x0c, 0x0c, 0x0c, 0x3c, 0x00],
    '^':[0x10, 0x38, 0x6c, 0xc6, 0x00, 0x00, 0x00, 0x00],
    '_':[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff],
    '`':[0x30, 0x18, 0x0c, 0x00, 0x00, 0x00, 0x00, 0x00],
    'a':[0x00, 0x00, 0x78, 0x0c, 0x7c, 0xcc, 0x76, 0x00],
    'b':[0xe0, 0x60, 0x7c, 0x66, 0x66, 0x66, 0xdc, 0x00],
    'c':[0x00, 0x00, 0x7c, 0xc6, 0xc0, 0xc6, 0x7c, 0x00],
    'd':[0x1c, 0x0c, 0x7c, 0xcc, 0xcc, 0xcc, 0x76, 0x00],
    'e':[0x00, 0x00, 0x7c, 0xc6, 0xfe, 0xc0, 0x7c, 0x00],
    'f':[0x3c, 0x66, 0x60, 0xf8, 0x60, 0x60, 0xf0, 0x00],
    'g':[0x00, 0x00, 0x76, 0xcc, 0xcc, 0x7c, 0x0c, 0xf8],
    'h':[0xe0, 0x60, 0x6c, 0x76, 0x66, 0x66, 0xe6, 0x00],
    'i':[0x18, 0x00, 0x38, 0x18, 0x18, 0x18, 0x3c, 0x00],
    'j':[0x06, 0x00, 0x06, 0x06, 0x06, 0x66, 0x66, 0x3c],
    'k':[0xe0, 0x60, 0x66, 0x6c, 0x78, 0x6c, 0xe6, 0x00],
    'l':[0x38, 0x18, 0x18, 0x18, 0x18, 0x18, 0x3c, 0x00],
    'm':[0x00, 0x00, 0xec, 0xfe, 0xd6, 0xd6, 0xd6, 0x00],
    'n':[0x00, 0x00, 0xdc, 0x66, 0x66, 0x66, 0x66, 0x00],
    'o':[0x00, 0x00, 0x7c, 0xc6, 0xc6, 0xc6, 0x7c, 0x00],
    'p':[0x00, 0x00, 0xdc, 0x66, 0x66, 0x7c, 0x60, 0xf0],
    'q':[0x00, 0x00, 0x76, 0xcc, 0xcc, 0x7c, 0x0c, 0x1e],
    'r':[0x00, 0x00, 0xdc, 0x76, 0x60, 0x60, 0xf0, 0x00],
    's':[0x00, 0x00, 0x7e, 0xc0, 0x7c, 0x06, 0xfc, 0x00],
    't':[0x30, 0x30, 0xfc, 0x30, 0x30, 0x36, 0x1c, 0x00],
    'u':[0x00, 0x00, 0xcc, 0xcc, 0xcc, 0xcc, 0x76, 0x00],
    'v':[0x00, 0x00, 0xc6, 0xc6, 0xc6, 0x6c, 0x38, 0x00],
    'w':[0x00, 0x00, 0xc6, 0xd6, 0xd6, 0xfe, 0x6c, 0x00],
    'x':[0x00, 0x00, 0xc6, 0x6c, 0x38, 0x6c, 0xc6, 0x00],
    'y':[0x00, 0x00, 0xc6, 0xc6, 0xc6, 0x7e, 0x06, 0xfc],
    'z':[0x00, 0x00, 0x7e, 0x4c, 0x18, 0x32, 0x7e, 0x00],
    '{':[0x0e, 0x18, 0x18, 0x70, 0x18, 0x18, 0x0e, 0x00],
    '|':[0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x00],
    '}':[0x70, 0x18, 0x18, 0x0e, 0x18, 0x18, 0x70, 0x00],
    '~':[0x76, 0xdc, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
}

eyes={
    'straight':[0x3c,0x7e,0xff,0xe7,0xe7,0xff,0x7e,0x3c],
    'straightX2':[0x3c,0x7e,0xe7,0xc3,0xc3,0xe7,0x7e,0x3c],
    'straightX3':[0x3c,0x66,0xc3,0x81,0x81,0xc3,0x66,0x3c],
    'straightX4':[0x3c,0x42,0x81,0x81,0x81,0x81,0x42,0x3c],
    'straightX2Left1':[0x3c,0x7e,0xcf,0x87,0x87,0xcf,0x7e,0x3c],
    'straightX2Left2':[0x3c,0x7e,0x9f,0x0f,0x0f,0x9f,0x7e,0x3c],
    'straightX2Left3':[0x3c,0x7e,0x3f,0x1f,0x1f,0x3f,0x7e,0x3c],
    'straightX2Left4':[0x3c,0x7e,0x7f,0x3f,0x3f,0x7f,0x7e,0x3c],
    'straightX2Left5':[0x3c,0x7e,0xff,0x7f,0x7f,0xff,0x7e,0x3c],
    'straightR2':[0x3c,0x7e,0xe7,0xdb,0xdb,0xe7,0x7e,0x3c],
    'noEyeball':[0x3c,0x7e,0xff,0xff,0xff,0xff,0x7e,0x3c],
    'straightBlink1':[0x00,0x7e,0xff,0xe7,0xe7,0xff,0x7e,0x00],
    'straightBlink2':[0x00,0x00,0xff,0xe7,0xe7,0xff,0x00,0x00],
    'straightBlink3':[0x00,0x00,0x00,0xe7,0xe7,0x00,0x00,0x00],
    'straightBlinkLine':[0x00,0x00,0x00,0xff,0xff,0x00,0x00,0x00],
    'all_off':[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    'up1':[0x3c,0x7e,0xe7,0xe7,0xff,0xff,0x7e,0x3c],
    'up2':[0x3c,0x66,0xe7,0xff,0xff,0xff,0x7e,0x3c],
    'up3':[0x24,0x66,0xff,0xff,0xff,0xff,0x7e,0x3c],
    'up4':[0x24,0x7e,0xff,0xff,0xff,0xff,0x7e,0x3c],
    'upLeft':[0x3c,0x4e,0xcf,0xff,0xff,0xff,0x7e,0x3c],
    'upLeft1':[0x3c,0x7e,0x9f,0x9f,0xff,0xff,0x7e,0x3c],
    'upLeft2':[0x3c,0x1e,0x9f,0xff,0xff,0xff,0x7e,0x3c],
    'upRight1':[0x3c,0x7e,0xf9,0xf9,0xff,0xff,0x7e,0x3c],
    'upRight':[0x3c,0x72,0xf3,0xff,0xff,0xff,0x7e,0x3c],
    'down1':[0x3c,0x7e,0xff,0xff,0xe7,0xe7,0x7e,0x3c],
    'down2':[0x3c,0x7e,0xff,0xff,0xff,0xe7,0x66,0x3c],
    'down3':[0x3c,0x7e,0xff,0xff,0xff,0xe7,0x66,0x3c],
    'down4':[0x3c,0x7e,0xff,0xff,0xff,0xff,0x7e,0x24],
    'downRight':[0x3c,0x7e,0xff,0xff,0xf9,0xf9,0x7e,0x3c],
    'downRight1':[0x3c,0x7e,0xff,0xff,0xff,0xf3,0x72,0x3c],
    'downRight2':[0x3c,0x7e,0xff,0xff,0xff,0xf9,0x78,0x3c],
    'downLeft':[0x3c,0x7e,0xff,0xff,0xff,0xcf,0x4e,0x3c],
    'downLeftB':[0x3c,0x7e,0xff,0xff,0x9f,0x9f,0x7e,0x3c],
    'downLeft1':[0x3c,0x7e,0xff,0xff,0xcf,0xcf,0x7e,0x3c],
    'downLeft1Blink1':[0x00,0x7e,0xff,0xff,0xcf,0xcf,0x7e,0x00],
    'downLeft1Blink2':[0x00,0x00,0xff,0xff,0xcf,0xcf,0x00,0x00],
    'downLeft1Blink3':[0x00,0x00,0x00,0xff,0xcf,0x00,0x00,0x00],
    'downLeft2':[0x3c,0x7e,0xff,0xff,0xff,0x9f,0x1e,0x3c],
    'left1':[0x3c,0x7e,0xff,0xcf,0xcf,0xff,0x7e,0x3c],
    'left2':[0x3c,0x7e,0xff,0x9f,0x9f,0xff,0x7e,0x3c],
    'left3':[0x3c,0x7e,0xff,0x3f,0x3f,0xff,0x7e,0x3c],
    'left4':[0x3c,0x7e,0xff,0x7f,0x7f,0xff,0x7e,0x3c],
    'right1':[0x3c,0x7e,0xff,0xf3,0xf3,0xff,0x7e,0x3c],
    'right2':[0x3c,0x7e,0xff,0xf9,0xf9,0xff,0x7e,0x3c],
    'right3':[0x3c,0x7e,0xff,0xfc,0xfc,0xff,0x7e,0x3c],
    'right4':[0x3c,0x7e,0xff,0xfe,0xfe,0xff,0x7e,0x3c],
    'ghost1':[0x3c,0x56,0x93,0xdb,0xff,0xff,0xdd,0x89],
    'ghost2':[0x38,0x7c,0x92,0x92,0xfe,0xfe,0xfe,0xaa],
    
}

shapes={
    'smile':[0x3c, 0x42, 0xa5, 0x81, 0xa5, 0x99, 0x42, 0x3c],
    'smileL':[0x3c, 0x42, 0xa9, 0xa9, 0x85, 0xb9, 0x42, 0x3c],
    'empty':[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    'all_on':[0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff],
    'arrow':[0x18,0x24,0x42,0xff,0x18,0x18,0x18,0x18],
    'invader1':[0x18,0x3c,0x7e,0xdb,0xff,0x24,0x5a,0xa5],
    'invader2':[0x18,0x3c,0x7e,0xdb,0xff,0x24,0x5a,0x42],
    'tree1':[0x18, 0x18, 0x3c, 0x3c, 0x7e, 0xff, 0x18, 0x18],
    'tree1lit1':[0x18, 0x18, 0x3c, 0x3c, 0x7e, 0xff, 0x18, 0x18],
    'tree1lit2':[0x5a,0x99,0x3c,0xbd,0x7e,0xff,0x18,0x18],
    'tree2':[0x18, 0x18, 0x3c, 0x3c, 0x7e, 0x7e, 0xff, 0x18],
    'bunny1':[0x66, 0x66, 0x66, 0xff, 0x81, 0xa5, 0x99, 0x7e],
    'bunny2':[0x66, 0xe7, 0x66, 0xff, 0x81, 0xa5, 0x99, 0x7e],
    'bunny3':[0x66, 0x66, 0xff, 0x81, 0xa5, 0x81, 0x99, 0x7e],
    'danbo':[0x00, 0xff, 0x81, 0xa5, 0x81, 0x81, 0xff, 0x00],
    'clock1':[0x3c, 0x42, 0x91, 0x91, 0x9d, 0x81, 0x42, 0x3c],
    'heart1F':[0x00, 0x66, 0xff, 0xff, 0x7e, 0x3c, 0x18, 0x00],
    'heart1':[0x00, 0x66, 0x99, 0x81, 0x42, 0x24, 0x18, 0x00],
    'heart2':[0x00, 0x66, 0x99, 0x81, 0x81, 0x42, 0x24, 0x18],
    'heart2F':[0x00, 0x66, 0xff, 0xff, 0xff, 0x7e, 0x3c, 0x18],
    'santaHat':[0x00, 0x3c, 0x7e, 0x4f, 0xef, 0xef, 0xef, 0x0f],
    'santaHat2':[0x00,0x00,0x3c,0x7e,0x4f,0xef,0xef,0xef],
    'star1':[0x00,0x00,0x00,0x18,0x18,0x00,0x00,0x00],
    'star2':[0x00,0x00,0x24,0x18,0x18,0x24,0x00,0x00],
    'star3':[0x00,0x42,0x24,0x18,0x18,0x24,0x42,0x00],
    'star4':[0x81,0x42,0x24,0x18,0x18,0x24,0x42,0x81],
    'star5':[0x02,0x84,0x48,0x38,0x1c,0x12,0x21,0x40],
    'star6':[0x06,0x8c,0xd8,0x7c,0x3e,0x1b,0x31,0x60],
    'star7':[0x04,0x08,0x90,0x5c,0x3a,0x09,0x10,0x20],
    'star8':[0x08,0x10,0x10,0x9e,0x79,0x08,0x08,0x10],
    'star9':[0x10,0x10,0x10,0x1f,0xf8,0x08,0x08,0x08],
    'star10':[0x20,0x10,0x11,0x1e,0x78,0x88,0x08,0x04],
    'star11':[0x40,0x21,0x12,0x1c,0x38,0x48,0x84,0x02],

}

```

Double-click **matrix dot\.py** and click ![](./media/d1dbbae869194ef12c2d684636f1ce4b.png)to run the test code.

![](./media/9e431dc8ec023e64cde23b4ed8de7613.png)

**6. Code Explanation**：

show\_char(): show characters, for example, show\_char(matrix\_fonts.textFont1\['A'\]) means showing A.

scroll\_message(font,message='hello',delay=0.05): scroll to display, 0.05 is the speed to scroll.

Massage means displayed character strings, font is a model file.

**7. Test Result：**

Wire up and upload the test code. Then the dot matrix display will show “A”,“B”and“C”then“Hello World”.

![](./media/48a2ad35b392d91576eacfaa14a36e93.jpeg)

**8. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 36
 * HT16K33 8*8 dot matrix
 * http://www.keyestudio.com
'''
import machine
import time
import json
import matrix_fonts
from ht16k33_matrix import ht16k33_matrix
## Tool To Make Sprites https://gurgleapps.com/tools/matrix
#i2c config
clock_pin = 21
data_pin = 20
bus = 0
i2c_addr_left = 0x70
use_i2c = True

def scan_for_devices():
    i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))
    devices = i2c.scan()
    if devices:
        for d in devices:
            print(hex(d))
    else:
        print('no i2c devices')

if use_i2c:
    scan_for_devices()
    left_eye = ht16k33_matrix(data_pin, clock_pin, bus, i2c_addr_left)

def show_char(left):
    if use_i2c:
        left_eye.show_char(left)
        
def scroll_message(font,message='hello',delay=0.05):
    left_message = '   ' + message
    right_message = message + '   '
    length=len(right_message)
    char_range=range(length-1)
    for char_pos in char_range:
      right_left_char=font[right_message[char_pos]]
      right_right_char=font[right_message[char_pos+1]]
      left_left_char=font[left_message[char_pos]]
      left_right_char=font[left_message[char_pos+1]]
      for shift in range(8):
        left_bytes=[0,0,0,0,0,0,0,0]
        right_bytes=[0,0,0,0,0,0,0,0]
        for col in range(8):
          left_bytes[col]=left_bytes[col]|left_left_char[col]<<shift
          left_bytes[col]=left_bytes[col]|left_right_char[col]>>8-shift;
          right_bytes[col]=right_bytes[col]|right_left_char[col]<<shift
          right_bytes[col]=right_bytes[col]|right_right_char[col]>>8-shift;
        if use_i2c:
                left_eye.show_char(left_bytes)
        time.sleep(delay)


while True:
    show_char(matrix_fonts.textFont1['A'])
    time.sleep(1)
    show_char(matrix_fonts.textFont1['B'])
    time.sleep(1)
    show_char(matrix_fonts.textFont1['C'])
    time.sleep(1)
    scroll_message(matrix_fonts.textFont1, ' Hello World ')
```

### Project 37: RFID Module 

![](./media/75003b61112e3495f213629e49f26185.jpeg)

**1. Description**

RFIDRFID-RC522 radio frequency module adopts a Philips MFRC522 original chip to design card reading circuit, easy to use and low cost, suitable for equipment development and card reader development and so on.

RFID or Radio Frequency Identification system consists of two main components, a transponder/tag attached to an object to be identified, and a Transceiver also known as interrogator/Reader.

In the experiment, the data read by the card swipe module is 4 hexadecimal numbers, and we print these four hexadecimal numbers as strings. For example, we read the data of the IC card below: 0x8d, 0xfe, 0x6c, 0x4d, and the information string displayed in the shell is 8dfe6c4d; the data read from the keychain is: 0xbc, 0x33, 0x76, 0x6e, and the information is displayed in the shell The string is bc33766e. Sometimes I see that there are only 7 bits because there is a 0 in the front omitted, such as 0a, it displays a.

**2. Working Principle**

RFID (Radio Frequency Identification)

Radio frequency identification, the card reader is composed of a radio frequency module and a high-level magnetic field. The Tag transponder is a sensing device, and this device does not contain a battery. It only contains tiny integrated circuit chips and media for storing data and antennas for receiving and transmitting signals. To read the data in the tag, first put it into the reading range of the card reader. The reader will generate a magnetic field, and because the magnetic energy generates electricity according to Lenz's law, the RFID tag will supply power, thereby activating the device.

![](./media/8f1b325813b0fe4f6b0fd1e6f02a9405.png)

**3. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.34931in;height:0.73611in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/530cb53e5b1e1b140de487cfc46be453.png" style="width:1.18194in;height:0.65972in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio DIY RFID Module*1</td>
<td>4P Dupont Wire*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/decf08b83c5594f7f1e51f6e93051f4b.png" style="width:1.30208in;height:0.69722in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/2a40c5c68dc7802d29bcf719bb688f64.png" style="width:1.3in;height:0.81806in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Micro USB Cable*1</td>
<td>Key*1</td>
<td>IC Card*1</td>
<td></td>
</tr>
</tbody>
</table>

<br>
<br>

**4. Connection Diagram**

![](./media/ebdaf69914ef2018af5127f51f3b0a52.png)

**5. Run the test code**

Find and double-click **mfrc522\.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/6ae130a771c4db8703bda21a7277e744.png)

We need to save the following code in the pico before running the code, and name **mfrc522\_config.py** (save in the library)

```Python
class Uid:
    size    = 0                  # Number of bytes in the UID. 4, 7 or 10.
    uidByte = [0,0,0,0,0,0,0,0,0,0]
    sak     = 0                  # The SAK (Select acknowledge) byte returned from the PICC after successful selection.
    

class mfrc522Config(Uid):
    # MFRC522 registers. Described in chapter 9 of the datasheet.
    # PCD_Register
    # Page 0: Command and status
    #                 0x00 #reserved for future use
    CommandReg      = 0x01 #starts and stops command execution
    ComIEnReg       = 0x02 #enable and disable interrupt request control bits
    DivIEnReg       = 0x03 #enable and disable interrupt request control bits
    ComIrqReg       = 0x04 #interrupt request bits
    DivIrqReg       = 0x05 #interrupt request bits
    ErrorReg        = 0x06 #error bits showing the error status of the last command executed
    Status1Reg      = 0x07 #communication status bits
    Status2Reg      = 0x08 #receiver and transmitter status bits
    FIFODataReg     = 0x09 #input and output of 64 byte FIFO buffer
    FIFOLevelReg    = 0x0A #number of bytes stored in the FIFO buffer
    WaterLevelReg   = 0x0B #level for FIFO underflow and overflow warning
    ControlReg      = 0x0C #miscellaneous control registers
    BitFramingReg   = 0x0D #adjustments for bit-oriented frames
    CollReg         = 0x0E #bit position of the first bit-collision detected on the RF interface
    #                 0x0F #reserved for future use

    # Page 1: Command
    #                 0x10 #reserved for future use
    ModeReg         = 0x11 #defines general modes for transmitting and receiving
    TxModeReg       = 0x12 #defines transmission data rate and framing
    RxModeReg       = 0x13 #defines reception data rate and framing
    TxControlReg    = 0x14 #controls the logical behavior of the antenna driver pins TX1 and TX2
    TxASKReg        = 0x15 #controls the setting of the transmission modulation
    TxSelReg        = 0x16 #elects the internal sources for the antenna driver
    RxSelReg        = 0x17 #selects internal receiver settings
    RxThresholdReg  = 0x18 #selects thresholds for the bit decoder
    DemodReg        = 0x19 #defines demodulator settings
    #                 0x1A #reserved for future use
    #                 0x1B #eserved for future use
    MfTxReg         = 0x1C #controls some MIFARE communication transmit parameters
    MfRxReg         = 0x1D #controls some MIFARE communication receive parameters
    #                 0x1E #reserved for future use
    SerialSpeedReg  = 0x1F #selects the speed of the serial UART interface

    # Page 2: Configuration
    #   0x20 reserved for future use
    CRCResultRegH   = 0x21 #shows the MSB and LSB values of the CRC calculation
    CRCResultRegL   = 0x22 #
    #                 0x23 #reserved for future use
    ModWidthReg     = 0x24 #controls the ModWidth setting?
    #                 0x25 #reserved for future use
    RFCfgReg        = 0x26 #onfigures the receiver gain
    GsNReg          = 0x27 #selects the conductance of the antenna driver pins TX1 and TX2 for modulation
    CWGsPReg        = 0x28 #defines the conductance of the p-driver output during periods of no modulation
    ModGsPReg       = 0x29 #defines the conductance of the p-driver output during periods of modulation
    TModeReg        = 0x2A #defines settings for the internal timer
    TPrescalerReg   = 0x2B #the lower 8 bits of the TPrescaler value. The 4 high bits are in TModeReg.
    TReloadRegH     = 0x2C #efines the 16-bit timer reload value
    TReloadRegL     = 0x2D #
    TCounterValueRegH   = 0x2E #shows the 16-bit timer value
    TCounterValueRegL   = 0x2F #

    # Page 3: Test Registers
    #                 0x30 #reserved for future use
    TestSel1Reg     = 0x31 #general test signal configuration
    TestSel2Reg     = 0x32 #eneral test signal configuration
    TestPinEnReg    = 0x33 #enables pin output driver on pins D1 to D7
    TestPinValueReg = 0x34 #defines the values for D1 to D7 when it is used as an I/O bus
    TestBusReg      = 0x35 #shows the status of the internal test bus
    AutoTestReg     = 0x36 #controls the digital self test
    VersionReg      = 0x37 #shows the software version
    AnalogTestReg   = 0x38 #controls the pins AUX1 and AUX2
    TestDAC1Reg     = 0x39 #defines the test value for TestDAC1
    TestDAC2Reg     = 0x3A #defines the test value for TestDAC2
    TestADCReg      = 0x3B #shows the value of ADC I and Q channels
    #                 0x3C #reserved for production tests
    #                 0x3D #reserved for production tests
    #                 0x3E #reserved for production tests
    #                 0x3F #reserved for production tests 
    
    # MFRC522 commands. Described in chapter 10 of the datasheet.
    # PCD_Command
    PCD_Idle             = 0x00 #no action, cancels current command execution
    PCD_Mem              = 0x01 #stores 25 bytes into the internal buffer
    PCD_GenerateRandomID = 0x02 #generates a 10-byte random ID number
    PCD_CalcCRC          = 0x03 #activates the CRC coprocessor or performs a self test
    PCD_Transmit         = 0x04 #transmits data from the FIFO buffer
    PCD_NoCmdChange      = 0x07 #no command change, can be used to modify the CommandReg register bits without affecting the command, for example, the PowerDown bit
    PCD_Receive          = 0x08 #activates the receiver circuits
    PCD_Transceive       = 0x0C #transmits data from FIFO buffer to antenna and automatically activates the receiver after transmission
    PCD_MFAuthent        = 0x0E #performs the MIFARE standard authentication as a reader
    PCD_SoftReset        = 0x0F #resets the MFRC522

    # MFRC522 RxGain[2:0] masks, defines the receiver's signal voltage gain factor (on the PCD).
    # Described in 9.3.3.6 / table 98 of the datasheet at http://www.nxp.com/documents/data_sheet/MFRC522.pdf
    # PCD_RxGain
    RxGain_18dB          = 0x00 << 4 #000b - 18 dB, minimum
    RxGain_23dB          = 0x01 << 4 #001b - 23 dB
    RxGain_18dB_2        = 0x02 << 4 #010b - 18 dB, it seems 010b is a duplicate for 000b
    RxGain_23dB_2        = 0x03 << 4 #011b - 23 dB, it seems 011b is a duplicate for 001b
    RxGain_33dB          = 0x04 << 4 #100b - 33 dB, average, and typical default
    RxGain_38dB          = 0x05 << 4 #101b - 38 dB
    RxGain_43dB          = 0x06 << 4 #110b - 43 dB
    RxGain_48dB          = 0x07 << 4 #111b - 48 dB, maximum
    RxGain_min           = 0x00 << 4 #000b - 18 dB, minimum, convenience for RxGain_18dB
    RxGain_avg           = 0x04 << 4 #100b - 33 dB, average, convenience for RxGain_33dB
    RxGain_max           = 0x07 << 4 #111b - 48 dB, maximum, convenience for RxGain_48dB    
    
    # Commands sent to the PICC.
    # The commands used by the PCD to manage communication with several PICCs (ISO 14443-3, Type A, section 6.4)
    PICC_CMD_REQA           = 0x26 #REQuest command, Type A. Invites PICCs in state IDLE to go to READY and prepare for anticollision or selection. 7 bit frame.
    PICC_CMD_WUPA           = 0x52 #Wake-UP command, Type A. Invites PICCs in state IDLE and HALT to go to READY(*) and prepare for anticollision or selection. 7 bit frame.
    PICC_CMD_CT             = 0x88 #Cascade Tag. Not really a command, but used during anti collision.
    PICC_CMD_SEL_CL1        = 0x93 #Anti collision/Select, Cascade Level 1
    PICC_CMD_SEL_CL2        = 0x95 #Anti collision/Select, Cascade Level 2
    PICC_CMD_SEL_CL3        = 0x97 #Anti collision/Select, Cascade Level 3
    PICC_CMD_HLTA           = 0x50 #HaLT command, Type A. Instructs an ACTIVE PICC to go to state HALT.
    # The commands used for MIFARE Classic (from http://www.nxp.com/documents/data_sheet/MF1S503x.pdf, Section 9)
    # Use PCD_MFAuthent to authenticate access to a sector, then use these commands to read/write/modify the blocks on the sector.
    # The read/write commands can also be used for MIFARE Ultralight.
    PICC_CMD_MF_AUTH_KEY_A  = 0x60 #Perform authentication with Key A
    PICC_CMD_MF_AUTH_KEY_B  = 0x61 #Perform authentication with Key B
    PICC_CMD_MF_READ        = 0x30 #Reads one 16 byte block from the authenticated sector of the PICC. Also used for MIFARE Ultralight.
    PICC_CMD_MF_WRITE       = 0xA0 #Writes one 16 byte block to the authenticated sector of the PICC. Called "COMPATIBILITY WRITE" for MIFARE Ultralight.
    PICC_CMD_MF_DECREMENT   = 0xC0 #Decrements the contents of a block and stores the result in the internal data register.
    PICC_CMD_MF_INCREMENT   = 0xC1 #Increments the contents of a block and stores the result in the internal data register.
    PICC_CMD_MF_RESTORE     = 0xC2 #Reads the contents of a block into the internal data register.
    PICC_CMD_MF_TRANSFER    = 0xB0 #Writes the contents of the internal data register to a block.
    # The commands used for MIFARE Ultralight (from http://www.nxp.com/documents/data_sheet/MF0ICU1.pdf, Section 8.6)
    # The PICC_CMD_MF_READ and PICC_CMD_MF_WRITE can also be used for MIFARE Ultralight.
    PICC_CMD_UL_WRITE       = 0xA2 #Writes one 4 byte page to the PICC.

    # MIFARE constants that does not fit anywhere else
    #  MIFARE_Misc
    MF_ACK                  = 0xA #The MIFARE Classic uses a 4 bit ACK/NAK. Any other value than 0xA is NAK.
    MF_KEY_SIZE             = 6   #A Mifare Crypto1 key is 6 bytes.
    
    # PICC types we can detect. Remember to update PICC_GetTypeName() if you add more.
    # PICC_Type
    PICC_TYPE_UNKNOWN       = 0
    PICC_TYPE_ISO_14443_4   = 1 #PICC compliant with ISO/IEC 14443-4
    PICC_TYPE_ISO_18092     = 2 #PICC compliant with ISO/IEC 18092 (NFC)
    PICC_TYPE_MIFARE_MINI   = 3 #MIFARE Classic protocol, 320 bytes
    PICC_TYPE_MIFARE_1K     = 4 #MIFARE Classic protocol, 1KB
    PICC_TYPE_MIFARE_4K     = 5 #MIFARE Classic protocol, 4KB
    PICC_TYPE_MIFARE_UL     = 6 #MIFARE Ultralight or Ultralight C
    PICC_TYPE_MIFARE_PLUS   = 7 #MIFARE Plus
    PICC_TYPE_TNP3XXX       = 8 #Only mentioned in NXP AN 10833 MIFARE Type Identification Procedure
    ICC_TYPE_NOT_COMPLETE   = 255 #SAK indicates UID is not complete.
    
    # Return codes from the functions in this class. Remember to update GetStatusCodeName() if you add more.
    # StatusCode
    STATUS_OK               = 1 #Success
    STATUS_ERROR            = 2 #Error in communication
    STATUS_COLLISION        = 3 #Collission detected
    STATUS_TIMEOUT          = 4 #Timeout in communication.
    STATUS_NO_ROOM          = 5 #A buffer is not big enough.
    STATUS_INTERNAL_ERROR   = 6 #Internal error in the code. Should not happen ;-)
    STATUS_INVALID          = 7 #Invalid argument.
    STATUS_CRC_WRONG        = 8 #The CRC_A does not match
    STATUS_MIFARE_NACK      = 9 #A MIFARE PICC responded with NAK.
    
    # Size of the MFRC522 FIFO
    FIFO_SIZE               = 64 #The FIFO is 64 bytes.
    
    uid = Uid
```

Then save the following code to pico as **soft_iic\.py**.

```Python
from machine import Pin
import time

class softIIC:

    def __init__(self, scl_, sda_, addr_):
        self.addr = addr_
        self.scl  = scl_
        self.sda  = sda_
        
        
    def IIC_start(self):
        Pin_scl = Pin(self.scl, Pin.OUT, value=1)    # create output pin
        Pin_sda = Pin(self.sda, Pin.OUT, value=1)    # create output pin                   
        #Pin_sda.value(1)
        #Pin_scl.value(1)
        time.sleep_us(5)
        #time.sleep(1)
        Pin_sda.value(0)                    
        time.sleep_us(5)
        Pin_scl.value(0)         
        #time.sleep(1)
        

    def IIC_stop(self):
        Pin_scl = Pin(self.scl, Pin.OUT, value=0)    # create output pin
        Pin_sda = Pin(self.sda, Pin.OUT, value=0)    # create output pin
        #Pin_scl.value(0) 
        #Pin_sda.value(0)                  
        time.sleep_us(5)
        Pin_scl.value(1)
        Pin_sda.value(1)
        time.sleep_us(5)  


    def IIC_master_ack(self):
        Pin_scl = Pin(self.scl, Pin.OUT, value=0)    # create output pin
        Pin_sda = Pin(self.sda, Pin.OUT, value=0)    # create output pin
        #Pin_scl.value(0)
        #Pin_sda.value(0)
        time.sleep_us(5)
        
        Pin_scl.value(1)
        time.sleep_us(5)
        Pin_scl.value(0)
        #Pin_sda.value(1)                      


    def IIC_master_notack(self):
        Pin_scl = Pin(self.scl, Pin.OUT, value=0)    # create output pin
        Pin_sda = Pin(self.sda, Pin.OUT, value=1)    # create output pin
        #Pin_scl.value(0)
        #Pin_sda.value(1)
        time.sleep_us(5)
        Pin_scl.value(1)                  
        time.sleep_us(5)
        Pin_scl.value(0)


    def IIC_slave_ack(self):
        i=0
        Pin_scl = Pin(self.scl, Pin.OUT, value=0)    # create output pin
        Pin_sda = Pin(self.sda, Pin.IN, Pin.PULL_UP)     # create input pin       
        Pin_scl.value(1)
        time.sleep_us(5)
        while Pin_sda.value() == 1:
            time.sleep_us(1)
            i = i+1
            if i>20:
                while 1 :
                    print("IIC slave device not ack")
                    time.sleep(1)
                #return
                    

    def IIC_read_byte(self):
        dat = 0
        Pin_scl = Pin(self.scl, Pin.OUT, value=0)    # create input pin
        Pin_sda = Pin(self.sda, Pin.IN, Pin.PULL_UP)     # create input pin        
        for i in range(8):
            Pin_scl.value(0)
            time.sleep_us(3)
            Pin_scl.value(1)
            time.sleep_us(2)
            #print(Pin_sda.value())
            if Pin_sda.value() == 1:
                dat = dat<<1 | 1
            else:
                dat = dat<<1
            time.sleep_us(5)
        return dat


    def IIC_write_byte(self, dat):
        Pin_scl = Pin(self.scl, Pin.OUT, value=0)    # create output pin
        Pin_sda = Pin(self.sda, Pin.OUT, value=0)    # create output pin        
        for i in range(8):
            if 0x80 & dat == 0x80:
                Pin_sda.value(1)
                #print(1)
            else:
                Pin_sda.value(0)
                #print(0)
            Pin_scl.value(1)
            time.sleep_us(5)
            Pin_scl.value(0)
            time.sleep_us(5)
            dat = dat<<1
        #print("--------------------")
 
 
    def Read(self, _adr, _reg):
        self.IIC_start()
        self.IIC_write_byte(_adr<<1)
        self.IIC_slave_ack()
        #print("--------------1")
        self.IIC_write_byte(_reg)
        self.IIC_slave_ack()
        self.IIC_stop()
        #print("--------------2")
        self.IIC_start()
        self.IIC_write_byte((_adr<<1)|1)
        self.IIC_slave_ack()
        #print("--------------3")
        dat = self.IIC_read_byte()
        self.IIC_master_notack()
        self.IIC_stop()
        return dat


    def Write(self, _adr, _reg, _dat):
        self.IIC_start()
        self.IIC_write_byte(_adr<<1)
        self.IIC_slave_ack()
        
        self.IIC_write_byte(_reg)
        self.IIC_slave_ack()
 
        self.IIC_write_byte(_dat)
        self.IIC_slave_ack()
        self.IIC_stop()

```

Finally, save the following code to pico as **mfrc522_i2c\.py**.

```Python
from machine import Pin
import time
from mfrc522_config import mfrc522Config
from soft_iic import softIIC

class mfrc522(mfrc522Config,softIIC):
   
    def __init__(self, scl_, sda_, addr_):
        # Invoke the parent class's constructor
        softIIC.__init__(self, scl_, sda_, addr_)


    # Writes a byte to the specified register in the MFRC522 chip.
    # The interface is described in the datasheet section 8.1.2. 
    def PCD_WriteRegister(self,  
                          _reg,  #The register to write to. One of the PCD_Register enums.
                          _dat   #The value to write.
                          ):
        self.Write(self.addr, _reg, _dat)

    # Writes a number of bytes to the specified register in the MFRC522 chip.
    # The interface is described in the datasheet section 8.1.2.
    def PCD_WriteRegister_(self,  
                           reg,    #The register to write to. One of the PCD_Register enums.
                           count,  #The number of bytes to write to the register
                           lst     #The values to write. Byte array.
                           ):
        self.IIC_start()
        self.IIC_write_byte(self.addr<<1)
        self.IIC_slave_ack()
        
        self.IIC_write_byte(reg)
        self.IIC_slave_ack()
        
        for i in range(count):
            self.IIC_write_byte(lst[i])
            self.IIC_slave_ack()
        self.IIC_stop()
 

    # Reads a byte from the specified register in the MFRC522 chip.
    # The interface is described in the datasheet section 8.1.2.
    def PCD_ReadRegister(self, _reg):     # The register to read from. One of the PCD_Register enums.
        return self.Read(self.addr,_reg)
        # End PCD_ReadRegister()


    # Reads a number of bytes from the specified register in the MFRC522 chip.
    # The interface is described in the datasheet section 8.1.2.
    # self.PCD_ReadRegister_(self.FIFODataReg, n, backData, rxAlign)
    def PCD_ReadRegister_(self,
                          reg,       # The register to read from. One of the PCD_Register enums.
                          count,     # The number of bytes to read
                          values,    # Byte array to store the values in.
                          rxAlign = 0    # Only bit positions rxAlign..7 in values[0] are updated.
                          ):
        if count == 0:
            return
        self.IIC_start()
        self.IIC_write_byte(self.addr<<1)
        self.IIC_slave_ack()
        #print("--------------1")
        self.IIC_write_byte(reg)
        self.IIC_slave_ack()
        self.IIC_stop()
        #print("--------------2")
        self.IIC_start()
        self.IIC_write_byte((self.addr<<1)|1)
        self.IIC_slave_ack()
        #print("--------------3")
        
        for i in range(count):
            if i == 0 and rxAlign != 0:         # Only update bit positions rxAlign..7 in values[0]
                # Create bit mask for bit positions rxAlign..7
                mask = 0
                for i in range(rxAlign, 8):
                    mask |= (1<<i)
                # Read value and tell that we want to read the same address again.
                value = self.IIC_read_byte()
                # Apply mask to both current value of values[0] and the new data in value.
                values[0] = (values[i] & ~mask) | (value & mask)
            else:   # Normal case
                values[i] = self.IIC_read_byte()
            
            if i < count - 1:
                self.IIC_master_ack()
            else:
                self.IIC_master_notack()
                self.IIC_stop()
        #print(values)     
        # End PCD_ReadRegister()
        
        
    def PCD_Init(self):
        self.PCD_Reset()

        # When communicating with a PICC we need a timeout if something goes wrong.
        # f_timer = 13.56 MHz / (2*TPreScaler+1) where TPreScaler = [TPrescaler_Hi:TPrescaler_Lo].
        # TPrescaler_Hi are the four low bits in TModeReg. TPrescaler_Lo is TPrescalerReg.
        self.PCD_WriteRegister(self.TModeReg, 0x80)      # TAuto=1; timer starts automatically at the end of the transmission in all communication modes at all speeds
        self.PCD_WriteRegister(self.TPrescalerReg, 0xA9) # TPreScaler = TModeReg[3..0]:TPrescalerReg, ie 0x0A9 = 169 => f_timer=40kHz, ie a timer period of 25�s.
        self.PCD_WriteRegister(self.TReloadRegH, 0x03)   # Reload timer with 0x3E8 = 1000, ie 25ms before timeout.
        self.PCD_WriteRegister(self.TReloadRegL, 0xE8)   

        self.PCD_WriteRegister(self.TxASKReg, 0x40)      # Default 0x00. Force a 100 % ASK modulation independent of the ModGsPReg register setting
        self.PCD_WriteRegister(self.ModeReg, 0x3D)       # Default 0x3F. Set the preset value for the CRC coprocessor for the CalcCRC command to 0x6363 (ISO 14443-3 part 6.2.4)
        self.PCD_AntennaOn()                        # Enable the antenna driver pins TX1 and TX2 (they were disabled by the reset)
        # End PCD_Init()

        
    # Performs a soft reset on the MFRC522 chip and waits for it to be ready again.
    def PCD_Reset(self):
        # Issue the SoftReset command.
        self.PCD_WriteRegister(self.CommandReg, self.PCD_SoftReset)
        time.sleep(1)
        
        if self.PCD_ReadRegister(self.CommandReg) & (1<<4):
            print("Reset error!")


    # Turns the antenna on by enabling pins TX1 and TX2.
    # After a reset these pins are disabled.
    def PCD_AntennaOn(self):
        value = self.PCD_ReadRegister(self.TxControlReg)
        #print("AntennaOn data:" + str(value))
        if value & 0x03 != 0x03:
            self.PCD_WriteRegister(self.TxControlReg, value | 0x03)
        #End PCD_AntennaOn()
 
 
    # Turns the antenna off by disabling pins TX1 and TX2.
    def PCD_AntennaOff(self):
        self.PCD_ClearRegisterBitMask(self.TxControlReg, 0x03)

    
    # Sets the bits given in mask in register reg.
    def PCD_SetRegisterBitMask(self,
                               reg,              # The register to update. One of the PCD_Register enums.
                               mask              # The bits to set.
                               ):
        tmp = self.PCD_ReadRegister(reg)
        self.PCD_WriteRegister(reg, tmp | mask)  # set bit mask
        # End PCD_SetRegisterBitMask()
    
    
    # Clears the bits given in mask from register reg.
    def PCD_ClearRegisterBitMask(self,
                                 reg,   # The register to update. One of the PCD_Register enums.
                                 mask   # The bits to clear.
                                 ):
        tmp = self.PCD_ReadRegister(reg)
        self.PCD_WriteRegister(reg, tmp & (~mask))  #clear bit mask
        #  End PCD_ClearRegisterBitMask()
        
        
    # Use the CRC coprocessor in the MFRC522 to calculate a CRC_A.  
    #
    # @return STATUS_OK on success, STATUS_??? otherwise.
    def PCD_CalculateCRC(self,
                         data,   #In: Pointer to the data to transfer to the FIFO for CRC calculation.
                         length, #In: The number of bytes to transfer.
                         result  #Out: Pointer to result buffer. Result is written to result[0..1], low byte first.
                         ):
        self.PCD_WriteRegister(self.CommandReg, self.PCD_Idle)      # Stop any active command.
        self.PCD_WriteRegister(self.DivIrqReg, 0x04)                # Clear the CRCIRq interrupt request bit
        self.PCD_SetRegisterBitMask(self.FIFOLevelReg, 0x80)        # FlushBuffer = 1, FIFO initialization
        self.PCD_WriteRegister_(self.FIFODataReg, length, data)      # Write data to the FIFO
        self.PCD_WriteRegister(self.CommandReg, self.PCD_CalcCRC)   # Start the calculation
        # Wait for the CRC calculation to complete. Each iteration of the while-loop takes 17.73�s.
        while True:
            n = self.PCD_ReadRegister(self.DivIrqReg)    # DivIrqReg[7..0] bits are: Set2 reserved reserved MfinActIRq reserved CRCIRq reserved reserved
            if (n & 0x04):                               # CRCIRq bit set - calculation done
                break
            if (--i == 0):                               # The emergency break. We will eventually terminate on this one after 89ms. Communication with the MFRC522 might be down.
                return self.STATUS_TIMEOUT
        self.PCD_WriteRegister(self.CommandReg, self.PCD_Idle)     # Stop calculating CRC for new content in the FIFO. 
        
        # Transfer the result from the registers to the result buffer
        result[0] = self.PCD_ReadRegister(self.CRCResultRegL)
        result[1] = self.PCD_ReadRegister(self.CRCResultRegH)
        return self.STATUS_OK        
        # End PCD_CalculateCRC()


    # Executes the Transceive command.
    # CRC validation can only be done if backData and backLen are specified.
    # 
    # @return STATUS_OK on success, STATUS_??? otherwise.
    def PCD_TransceiveData(self,
                           sendData,   # Pointer to the data to transfer to the FIFO.
                           sendLen,    # Number of bytes to transfer to the FIFO.
                           backData,   # NULL or pointer to buffer if data should be read back after executing the command.
                           backLen,    # In: Max number of bytes to write to *backData. Out: The number of bytes returned.
                           validBits,  # In/Out: The number of valid bits in the last byte. 0 for 8 valid bits. Default NULL.
                           rxAlign,    # In: Defines the bit position in backData[0] for the first bit received. Default 0.
                           checkCRC    # In: True => The last two bytes of the response is assumed to be a CRC_A that must be validated.
                           ):
        waitIRq = 0x30
        return self.PCD_CommunicateWithPICC(self.PCD_Transceive, waitIRq, sendData, sendLen, backData, backLen, validBits, rxAlign, checkCRC)
        # End PCD_TransceiveData()
        
        
    # Transfers data to the MFRC522 FIFO, executes a command, waits for completion and transfers data back from the FIFO.
    # CRC validation can only be done if backData and backLen are specified.
    #
    # @return STATUS_OK on success, STATUS_??? otherwise.
    # result = self.PCD_TransceiveData(buffer, bufferUsed, responseBuffer, responseLength, tLB, rxAlign, 0)
    def PCD_CommunicateWithPICC(self,
                                command,        # The command to execute. One of the PCD_Command enums.
                                waitIRq,        # The bits in the ComIrqReg register that signals successful completion of the command.
                                sendData,       # Pointer to the data to transfer to the FIFO.
                                sendLen,        # Number of bytes to transfer to the FIFO.
                                backData,       # NULL or pointer to buffer if data should be read back after executing the command.
                                backLen,        # In: Max number of bytes to write to *backData. Out: The number of bytes returned.
                                validBits,      # In/Out: The number of valid bits in the last byte. 0 for 8 valid bits.
                                rxAlign,        # In: Defines the bit position in backData[0] for the first bit received. Default 0.
                                checkCRC        # In: True => The last two bytes of the response is assumed to be a CRC_A that must be validated.
                                ):
        txLastBits = validBits[0] if validBits != None else 0
        bitFraming = (rxAlign << 4) + txLastBits    # RxAlign = BitFramingReg[6..4]. TxLastBits = BitFramingReg[2..0]
        
        self.PCD_WriteRegister(self.CommandReg, self.PCD_Idle)        # Stop any active command.
        self.PCD_WriteRegister(self.ComIrqReg, 0x7F)                  # Clear all seven interrupt request bits
        self.PCD_SetRegisterBitMask(self.FIFOLevelReg, 0x80)          # FlushBuffer = 1, FIFO initialization
        self.PCD_WriteRegister_(self.FIFODataReg, sendLen, sendData)  # Write sendData to the FIFO
        self.PCD_WriteRegister(self.BitFramingReg, bitFraming)        # Bit adjustments
        self.PCD_WriteRegister(self.CommandReg, command)              # Execute the command
        if command == self.PCD_Transceive:
            self.PCD_SetRegisterBitMask(self.BitFramingReg, 0x80)     # StartSend=1, transmission of data starts

        # Wait for the command to complete.
        # In PCD_Init() we set the TAuto flag in TModeReg. This means the timer automatically starts when the PCD stops transmitting.
        # Each iteration of the do-while-loop takes 17.86�s.
        i = 2000
        while True:
            n = self.PCD_ReadRegister(self.ComIrqReg)    #ComIrqReg[7..0] bits are: Set1 TxIRq RxIRq IdleIRq HiAlertIRq LoAlertIRq ErrIRq TimerIRq
            if n & waitIRq:
                break
            if n & 0x01:
                return self.STATUS_TIMEOUT
            if --i == 0:
                return self.STATUS_TIMEOUT
        
        # Stop now if any errors except collisions were detected.
        errorRegValue = self.PCD_ReadRegister(self.ErrorReg)    # ErrorReg[7..0] bits are: WrErr TempErr reserved BufferOvfl CollErr CRCErr ParityErr ProtocolErr
        if errorRegValue & 0x13:                                # BufferOvfl ParityErr ProtocolErr
            return self.STATUS_ERROR
        
        # If the caller wants data back, get it from the MFRC522.
        if backData != None and backLen != None :
            n = self.PCD_ReadRegister(self.FIFOLevelReg)    # Number of bytes in the FIFO
            if n> backLen[0]:
                return self.STATUS_NO_ROOM
            backLen[0] = n                                     # Number of bytes returned
            # Note: Use list mutable types in Python
            self.PCD_ReadRegister_(self.FIFODataReg, n, backData, rxAlign)  # Get received data from FIFO
            #print("backData:")
            #print(backData)
            _validBits = self.PCD_ReadRegister(self.ControlReg) & 0x07  # RxLastBits[2:0] indicates the number of valid bits in the last received byte. If this value is 000b, the whole byte is valid.
            if validBits != None:
                validBits[0] = _validBits
                
        # Tell about collisions
        if errorRegValue & 0x08: # collErr
            return self.STATUS_COLLISION
        
        # Perform CRC_A validation if requested.
        if backData != None and  backLen != None  and checkCRC != 0:
            # In this case a MIFARE Classic NAK is not OK.
            if backLen[0] == 1 and _validBits[0] == 4:
                return self.STATUS_MIFARE_NACK
            # We need at least the CRC_A value and all 8 bits of the last byte must be received.
            if backLen[0] < 2 or _validBits != 0:
                return self.STATUS_CRC_WRONG
            # Verify CRC_A - do our own calculation and store the control in controlBuffer.
            controlBuffer = [0, 0]
            n = self.PCD_CalculateCRC(backData[0], backLen[0] - 2, controlBuffer[0])
            if n != self.STATUS_OK:
                return n
            if (backData[backLen[0] - 2] != controlBuffer[0]) or (backData[backLen[0] - 1] != controlBuffer[1]):
                return self.STATUS_CRC_WRONG
        return self.STATUS_OK;
        # End PCD_CommunicateWithPICC()
        
            
    # Transmits a REQuest command, Type A. Invites PICCs in state IDLE to go to READY and prepare for anticollision or selection. 7 bit frame.
    # Beware: When two PICCs are in the field at the same time I often get STATUS_TIMEOUT - probably due do bad antenna design.
    # 
    # @return STATUS_OK on success, STATUS_??? otherwise.
    def PICC_RequestA(self,
                      bufferATQA,  # The buffer to store the ATQA (Answer to request) in
                      bufferSize   # Buffer size, at least two bytes. Also number of bytes returned if STATUS_OK.
                      ):
        cmd    = [self.PICC_CMD_REQA]
        return self.PICC_REQA_or_WUPA(cmd, bufferATQA, bufferSize)
        # End PICC_RequestA()
        
 
    # Transmits REQA or WUPA commands.
    # Beware: When two PICCs are in the field at the same time I often get STATUS_TIMEOUT - probably due do bad antenna design.
    # 
    # @return STATUS_OK on success, STATUS_??? otherwise.
    def PICC_REQA_or_WUPA(self,
                          command,     # The command to send - PICC_CMD_REQA or PICC_CMD_WUPA
                          bufferATQA,  # The buffer to store the ATQA (Answer to request) in
                          bufferSize   # Buffer size, at least two bytes. Also number of bytes returned if STATUS_OK.
                          ):
        if bufferATQA == None or bufferSize[0] < 2:   # The ATQA response is 2 bytes long.
            return self.STATUS_NO_ROOM
        self.PCD_ClearRegisterBitMask(self.CollReg, 0x80) # ValuesAfterColl=1 => Bits received after collision are cleared.
        validBits = [7]  # For REQA and WUPA we need the short frame format - transmit only 7 bits of the last (and only) byte. TxLastBits = BitFramingReg[2..0]
        status = self.PCD_TransceiveData(command, 1, bufferATQA, bufferSize, validBits, 0, 0)
        if status != self.STATUS_OK:
            return status
        if bufferSize[0] != 2 or validBits[0] != 0:
            return self.STATUS_ERROR
        return self.STATUS_OK
        # End PICC_REQA_or_WUPA()
    

    # Transmits SELECT/ANTICOLLISION commands to select a single PICC.
    # Before calling this function the PICCs must be placed in the READY(*) state by calling PICC_RequestA() or PICC_WakeupA().
    # On success:
    #       - The chosen PICC is in state ACTIVE(*) and all other PICCs have returned to state IDLE/HALT. (Figure 7 of the ISO/IEC 14443-3 draft.)
    #       - The UID size and value of the chosen PICC is returned in *uid along with the SAK.
    # 
    # A PICC UID consists of 4, 7 or 10 bytes.
    # Only 4 bytes can be specified in a SELECT command, so for the longer UIDs two or three iterations are used:
    #       UID size    Number of UID bytes    Cascade levels    Example of PICC
    #       ========    ===================    ==============    ===============
    #       single               4                   1           MIFARE Classic
    #       double               7                   2           MIFARE Ultralight
    #       triple              10                   3           Not currently in use?
    # 
    # @return STATUS_OK on success, STATUS_??? otherwise.
    def PICC_Select(self,
                    uid,           # Pointer to Uid struct. Normally output, but can also be used to supply a known UID.
                    validBits      # The number of known UID bits supplied in *uid. Normally 0. If set you must also supply uid->size.
                    ):
        uidComplete = False
        selectDone = False
        useCascadeTag = False
        cascadeLevel = 1
        result = 0
        count = 0
        index = 0
        uidIndex = 0                     # The first index in uid->uidByte[] that is used in the current Cascade Level.
        currentLevelKnownBits = 0        # The number of known UID bits in the current Cascade Level.
        buffer = [0,0,0,0,0,0,0,0,0]     # The SELECT/ANTICOLLISION commands uses a 7 byte standard frame + 2 bytes CRC_A
        bufferUsed = 0                   # The number of bytes used in the buffer, ie the number of bytes to transfer to the FIFO.
        rxAlign = 0                      # Used in BitFramingReg. Defines the bit position for the first bit received.
        txLastBits = 0                   # Used in BitFramingReg. The number of valid bits in the last transmitted byte.
        responseBuffer = [0]
        responseLength = [0]
        # Description of buffer structure:
        #       Byte 0: SEL                 Indicates the Cascade Level: PICC_CMD_SEL_CL1, PICC_CMD_SEL_CL2 or PICC_CMD_SEL_CL3
        #       Byte 1: NVB                 Number of Valid Bits (in complete command, not just the UID): High nibble: complete bytes, Low nibble: Extra bits.
        #       Byte 2: UID-data or CT      See explanation below. CT means Cascade Tag.
        #       Byte 3: UID-data
        #       Byte 4: UID-data
        #       Byte 5: UID-data
        #       Byte 6: BCC                 Block Check Character - XOR of bytes 2-5
        #       Byte 7: CRC_A
        #       Byte 8: CRC_A
        #  The BCC and CRC_A is only transmitted if we know all the UID bits of the current Cascade Level.
        # 
        #  Description of bytes 2-5: (Section 6.5.4 of the ISO/IEC 14443-3 draft: UID contents and cascade levels)
        #       UID size    Cascade level   Byte2   Byte3   Byte4   Byte5
        #       ========    =============   =====  =====    =====   =====
        #        4 bytes        1           uid0    uid1    uid2    uid3
        #        7 bytes        1           CT      uid0    uid1    uid2
        #                       2           uid3    uid4    uid5    uid6
        #       10 bytes        1           CT      uid0    uid1    uid2
        #                       2           CT      uid3    uid4    uid5
        #                       3           uid6    uid7    uid8    uid9
    
        # Sanity checks
        if validBits > 80:
            return self.STATUS_INVALID
    
        # Prepare MFRC522
        self.PCD_ClearRegisterBitMask(self.CollReg, 0x80)    # ValuesAfterColl=1 => Bits received after collision are cleared.

        # Repeat Cascade Level loop until we have a complete UID.
        uidComplete = False
        while uidComplete == False:
            # Set the Cascade Level in the SEL byte, find out if we need to use the Cascade Tag in byte 2.    
            if cascadeLevel == 1:
                buffer[0] = self.PICC_CMD_SEL_CL1
                uidIndex = 0
                useCascadeTag = validBits and uid.size > 4    # When we know that the UID has more than 4 bytes
            elif cascadeLevel == 2:
                buffer[0] = self.PICC_CMD_SEL_CL2
                uidIndex = 3
                useCascadeTag = validBits and uid.size > 7    # When we know that the UID has more than 7 bytes
            elif cascadeLevel == 3:
                buffer[0] = self.PICC_CMD_SEL_CL3
                uidIndex = 6
                useCascadeTag = False                         # Never used in CL3.           
            else:
                return self.STATUS_INTERNAL_ERROR
    
            # How many UID bits are known in this Cascade Level?
            currentLevelKnownBits = validBits - (8 * uidIndex)
            if currentLevelKnownBits < 0:
                currentLevelKnownBits = 0
        
            # Copy the known bits from uid->uidByte[] to buffer[]
            index = 2  # destination index in buffer[]
            #print(useCascadeTag);
            if useCascadeTag:
                index = index+1
                buffer[index] = self.PICC_CMD_CT
            # The number of bytes needed to represent the known bits for this level.
            bytesToCopy = 1 if currentLevelKnownBits % 8 > 0 else 0 # (currentLevelKnownBits % 8 ? 1 : 0) 
            bytesToCopy = currentLevelKnownBits // 8 + bytesToCopy
            if bytesToCopy:
                maxBytes = 3 if useCascadeTag else 4  # maxBytes = useCascadeTag ? 3 : 4
                if bytesToCopy > maxBytes:
                    bytesToCopy = maxBytes
                for i in range(bytesToCopy):
                    index = index+1
                    buffer[index] = uid.uidByte[uidIndex + i]
            # Now that the data has been copied we need to include the 8 bits in CT in currentLevelKnownBits
            if useCascadeTag:
                currentLevelKnownBits = currentLevelKnownBits + 8
        
            # Repeat anti collision loop until we can transmit all UID bits + BCC and receive a SAK - max 32 iterations.
            selectDone = False            
            while selectDone == False:
                # Find out how many bits and bytes to send and receive. 
                if currentLevelKnownBits >= 32:  # All UID bits in this Cascade Level are known. This is a SELECT.
                    # Serial.print(F("SELECT: currentLevelKnownBits=")); Serial.println(currentLevelKnownBits, DEC);
                    buffer[1] = 0x70 # NVB - Number of Valid Bits: Seven whole bytes
                    # Calculate BCC - Block Check Character
                    buffer[6] = buffer[2] ^ buffer[3] ^ buffer[4] ^ buffer[5]
                    # Calculate CRC_A
                    tmpBuffer = [buffer[7], buffer[8]]
                    result = self.PCD_CalculateCRC(buffer, 7, tmpBuffer)
                    buffer[7] = tmpBuffer[0]
                    buffer[8] = tmpBuffer[1]
                    
                    if result != self.STATUS_OK:
                        return result
                    txLastBits  = 0   # 0 => All 8 bits are valid.
                    bufferUsed  = 9
                    # Store response in the last 3 bytes of buffer (BCC and CRC_A - not needed after tx)
                    responseBuffer = [0].copy()
                    responseBuffer[0] = buffer[6]
                    responseBuffer = responseBuffer + buffer[7:]
                    responseLength[0] = 3
                    bufferFlag = 6
                    
                else: # This is an ANTICOLLISION.
                    # Serial.print(F("ANTICOLLISION: currentLevelKnownBits=")); Serial.println(currentLevelKnownBits, DEC);
                    txLastBits      = currentLevelKnownBits % 8
                    count           = currentLevelKnownBits // 8      # Number of whole bytes in the UID part.
                    index           = 2 + count                           # Number of whole bytes: SEL + NVB + UIDs
                    buffer[1]       = (index << 4) + txLastBits           # NVB - Number of Valid Bits
                
                    bufferUsed      = 1 if txLastBits else 0
                    bufferUsed      = index + bufferUsed
                    
                    responseBuffer = [0].copy()
                    # Store response in the unused part of buffer
                    responseBuffer[0]  = buffer[index]
                    responseBuffer     = responseBuffer + buffer[index+1:]
                    responseLength[0]  = len(buffer) - index
                    bufferFlag = index

                # Set bit adjustments
                rxAlign = txLastBits              # Having a seperate variable is overkill. But it makes the next line easier to read.
                self.PCD_WriteRegister(self.BitFramingReg, (rxAlign << 4) + txLastBits)   # RxAlign = BitFramingReg[6..4]. TxLastBits = BitFramingReg[2..0]
    
                #Transmit the buffer and receive the response.
                tLB = [txLastBits]
                result = self.PCD_TransceiveData(buffer, bufferUsed, responseBuffer, responseLength, tLB, rxAlign, 0)
                for i in range(bufferFlag, bufferFlag+responseLength[0]):
                    buffer[i] = responseBuffer[i-bufferFlag]

                if result == self.STATUS_COLLISION:    # More than one PICC in the field => collision.
                    result = self.PCD_ReadRegister(CollReg) # CollReg[7..0] bits are: ValuesAfterColl reserved CollPosNotValid CollPos[4:0]
                    if result & 0x20:
                        return self.STATUS_COLLISION   # Without a valid collision position we cannot continue
                    collisionPos = result & 0x1F       # Values 0-31, 0 means bit 32.
                    if collisionPos == 0:
                        collisionPos = 32
                    if collisionPos <= currentLevelKnownBits:  # No progress - should not happen
                        return self.STATUS_INTERNAL_ERROR
                    # Choose the PICC with the bit set.
                    currentLevelKnownBits = collisionPos
                    count = (currentLevelKnownBits - 1) % 8    # The bit to modify
                    index = 1 if count else 0
                    index = 1 + (currentLevelKnownBits / 8) + index  # First byte is index 0.
                    buffer[index] = buffer[index] | (1 << count)
                elif result != self.STATUS_OK:
                    return result
                else: # STATUS_OK
                    if currentLevelKnownBits >= 32:  # This was a SELECT.
                        selectDone = True            # No more anticollision
                        # We continue below outside the while.
                    else:  # This was an ANTICOLLISION.
                        # We now have all 32 bits of the UID in this Cascade Level
                        currentLevelKnownBits = 32
                        # Run loop again to do the SELECT.
            # End of while (!selectDone)
    
            # We do not check the CBB - it was constructed by us above.
            # Copy the found UID bytes from buffer[] to uid->uidByte[]
            index = 3 if buffer[2] == self.PICC_CMD_CT else 2  # source index in buffer[]
            bytesToCopy = 3 if buffer[2] == self.PICC_CMD_CT else 4
            for i in range(bytesToCopy):
                uid.uidByte[uidIndex + i] = buffer[index]
                index = index+1
              
            # Check response SAK (Select Acknowledge)
            if responseLength[0] != 3 or txLastBits != 0: # SAK must be exactly 24 bits (1 byte + CRC_A).
                return self.STATUS_ERROR
            # Verify CRC_A - do our own calculation and store the control in buffer[2..3] - those bytes are not needed anymore.          
            CRCbuffer = [buffer[2]]
            CRCbuffer = CRCbuffer + buffer[3:]
            result = self.PCD_CalculateCRC(responseBuffer, 1, CRCbuffer)
            buffer[2] = CRCbuffer[0]
            buffer[3] = CRCbuffer[1]
            
            if result != self.STATUS_OK:
                return result
            
            if (buffer[2] != responseBuffer[1]) or (buffer[3] != responseBuffer[2]):
                return self.STATUS_CRC_WRONG
            if responseBuffer[0] & 0x04: # Cascade bit set - UID not complete yes
                cascadeLevel = cascadeLevel+1
            else:
                uidComplete = True
                uid.sak = responseBuffer[0] 
        # End of while (!uidComplete)
            
        # Set correct uid->size
        uid.size = 3 * cascadeLevel + 1       
        return self.STATUS_OK
        #  End PICC_Select()
                
                
    # Returns true if a PICC responds to PICC_CMD_REQA.
    # Only "new" cards in state IDLE are invited. Sleeping cards in state HALT are ignored.
    # 
    # @return bool
    def PICC_IsNewCardPresent(self):
        bufferATQA = [0, 0]
        bufferSize = [len(bufferATQA)]
        result = self.PICC_RequestA(bufferATQA, bufferSize)
        return result == self.STATUS_OK or result == self.STATUS_COLLISION
        #  End PICC_IsNewCardPresent()
        

    # Simple wrapper around PICC_Select.
    # Returns true if a UID could be read.
    # Remember to call PICC_IsNewCardPresent(), PICC_RequestA() or PICC_WakeupA() first.
    # The read UID is available in the class variable uid.
    # 
    # @return bool
    def PICC_ReadCardSerial(self):
        result = self.PICC_Select(self.uid, 0)
        return (result == self.STATUS_OK)
        # End PICC_ReadCardSerial()
        
        
    # Show details of PCD - MFRC522 Card Reader details.
    def ShowReaderDetails(self):
        v = self.PCD_ReadRegister(self.VersionReg)
        version = str(v)
        if v == 0x91:
            version = version + " = v1.0"
        elif v == 0x92:
            version = version + " = v2.0"
        else:
            version = version + "unknown"   
        print("MFRC522 Software Version:" + version)
```

After saving, we can see the module under mycropython device where we saved in pico.
![Img](./media/img-20231008110538.png)


**6. Code Explanation**

**mfrc522\_config.py;** this is a configuration file that defines some parameters and commands.

**mfrc522\_i2c.py;** are some initialization, reading and writing functions

**Soft\_iic.py;** we use the io analog portI2C

**7. Test Result**

Run the test code and wire up, power on, open the shell and set the baud rate to 9600. When we make the RFID module close to the IC card and the blue key, the information read by the module will be printed out, as shown in the figure below.

![](./media/9907ee0bd64d64c75184312223c88538.jpeg)
![Img](./media/img-20231107093406.png)

**8. Test code**

```c
/* 
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 37
 * mfrc522
 * http://www.keyestudio.com
*/
#include <Wire.h>
#include "MFRC522_I2C.h"
MFRC522 mfrc522(0x28);
String rfid_str = "";
void setup() {
  Serial.begin(115200);
  Wire.begin();
  mfrc522.PCD_Init();
}

void loop() {
  if ( ! mfrc522.PICC_IsNewCardPresent() || ! mfrc522.PICC_ReadCardSerial() ) {
    delay(50);
    return;
  }
  rfid_str = "";
  Serial.print(F("Card UID:"));
  for (byte i = 0; i < mfrc522.uid.size; i++) {// UID
    rfid_str = rfid_str + String(mfrc522.uid.uidByte[i], HEX);
  }
  Serial.println(rfid_str);
}
```

### Project 38: Breathing LED

![](./media/25107e92a36e701f271b2371359f2679.jpeg)

**1. Overview**

A“breathing LED”is a phenomenon where an LED's brightness smoothly changes from dark to bright and back to dark, continuing to do so and giving the illusion of an LED“breathing.”This phenomenon is similar to a lung breathing in and out. So how to control LED’s brightness? We need to take advantage of PWM.

**2. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.27083in;height:0.69306in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/f0ef7a5a2e7eebb09e91f73cb2a6caf3.png" style="width:0.94931in;height:0.6528in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio White LED Module*1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

**3. Wiring Diagram**

![](./media/d13028e8c6c0a663aa884d6b74a6900e.png)

**4. Run the test code：**

Double-click **Breath\.py**，and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png)to run the code.

![](./media/923d67a1506581a7244e45f6ffc7c810.png)

**5. Code Explanation：**

The bigger the duty cycle is set, the brighter the LED. The maximum is 65535. When duty increases from 0 to 255, up 1 and delay 10ms for each time, then LED will gradually get bright. When PWM is 255\*255, i decreases from 255 to 0, down by1 and delay 10ms for each time, then the LED will get dimmer, like human breathe.

Also, we can change the time of getting dimmer or brighter in the code. Another way is changing step length like direction = -2 or direction =2.

**6. Test Result：**

Run the test code, the LED on the module gradually gets dimmer then brighter, cyclically, like human breathe.

![](./media/36c4999e9852feffd9150d081d8c676b.jpeg)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 38
 * Breath
 * http://www.keyestudio.com
'''
import machine
import time

pwm = machine.PWM(machine.Pin(15))
pwm.freq(1000)

duty = 0
direction = 1
while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.01)
```

## 3. Comprehensive Experiments

The previous projects are related to single sensor or module. In the following part, we will combine various sensors and modules to create some comprehensive experiments to perform special functions.


### Project 39: Button-controlled LED

![](./media/50740b22d16151d490b8494b0bff4f6e.jpeg)

**1. Overview**

In this lesson, we will make an extension experiment with a button and an LED. When the button is pressed and low levels are output, the LED will light up; when the button is released, the LED will go off. Then we can control a module with another module.

**2. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:0.88611in;height:0.35069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:0.97222in;height:0.53125in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/f0ef7a5a2e7eebb09e91f73cb2a6caf3.png" style="width:0.87014in;height:0.5972in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/052aafd4dcb48c7cc39a456309a766a8.png" style="width:0.90347in;height:0.67222in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.99375in;height:0.53264in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio White LED Module*1</td>
<td>Keyestudio DIY Button Module*1</td>
<td>3P Dupont Wire*2</td>
<td><p>Micro</p>
<p>USB Cable*1</p></td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Wiring Diagram**

![](./media/c91cc54b02a47f17fa18e8cef0dcd74b.png)

**4. Run the test code：**

Double-click **button control LED\.py** and click
![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the test code.

![](./media/907a9ca2148a4ce6ad4c205588211547.png)

**5. Code Explanation：**

The trigger mode of the function button.irq(trigger = Pin.IRQ\_FALLING, handler = toggle\_handle) is when high levels turn into low levels, the trigger will interrupt, the interrupt function **toggle\_handle** will be used.

**6. Test Result：**

Run the test code, when buttons are pressed, the LED module will light up; if pressed again, the LED module will go off.

![](./media/bf5041b53722e7f438273f80fc16a2dc.jpeg)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 39
 * button control LED
 * http://www.keyestudio.com
'''
from machine import Pin
import time

button = Pin(16, Pin.IN)
LED = Pin(15, Pin.OUT)
touch = False

def toggle_handle(pin):
    global touch
    touch = not touch

button.irq(trigger = Pin.IRQ_FALLING, handler = toggle_handle)

while True:
    LED.value(touch)
    time.sleep(0.01)
```


### Project 40: Alarm Experiment

![](./media/6db3cb7d3a91e700a3b651c1f0edb7a5.jpeg)

**1. Overview**

In the previous experiment, we control an output module though an input module. In this lesson, we will make an experiment that the active buzzer will emit sounds once an obstacle appears.

**2. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:0.88611in;height:0.35069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.05764in;height:0.57778in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/ac83d2c470cd6c345f17feed3bce5358.png" style="width:0.96042in;height:0.60556in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0058c1fe09d89532921e3a54ec95d62f.png" style="width:0.93056in;height:0.60764in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.86528in;height:0.35972in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Obstacle Avoidance Sensor*1</td>
<td>Keyestudio Active Buzzer*1</td>
<td>3P Dupont Wire*2</td>
<td><p>Micro</p>
<p>USB Cable*1</p></td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Wiring Diagram**

![](./media/1fc50389eb7dfa837dd682e01c792f97.png)

**4. Run the test code**

Click **Avoiding alarm\.py** and double-click the code，and click ![](./media/d1dbbae869194ef12c2d684636f1ce4b.png)to run the test code.

**5. Code Explanation：**

The function sensor.value() will return a low level if an obstacle is detected.

**6. Test Result：**

Upload the test code, if the obstacle is detected, the external active buzzer will chime; if not, it won’t beep

![](./media/7e76674a2d89cbf737ae02ff91d8cdb9.jpeg)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 40
 * Avoiding alarm
 * http://www.keyestudio.com
'''
from machine import Pin
import time

buzzer = Pin(16, Pin.OUT)
sensor = Pin(15, Pin.IN)
while True:
    buzzer.value(not(sensor.value()))
    time.sleep(0.01)
```

### Project 41: Ultraviolet Alarm

**1. Description**

We can use a UV sensor to control the buzzer to achieve the effect of UV alarm.

**2. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.45417in;height:0.79306in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/4380c0a29b5226e64113a5b4e7f7a62d.png" style="width:0.82361in;height:0.61389in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/a5e355d0fd3c9b18c7684a9a2b99f0a5.png" style="width:0.90625in;height:0.64167in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.94722in;height:0.41875in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio ultraviolet Sensor*1</td>
<td>Keyestudio Active Buzzer*1</td>
<td>3P Dupont Wire*2</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Connection Diagram**

![](./media/755ba4ebbd018cbb31b895039e2d7164.png)

**4. Run the test code**

Find and double-click **UV\_alarm.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/e985093146350f230771c864d18f2f1c.png)

**5. Code Explanation**

The code settings in the experiment are similar to the previous experiments. This time, the module we input is used as an analog sensor. By setting a threshold, the alarm exceeds the threshold.

**6. Test Result**

Wire up and run the test code. When detecting ultraviolet rays through the ultraviolet sensor and reaching the strength we set, the active buzzer will emit sound

![](./media/d1d5abbc61067877a4ffa4f1bd357186.jpeg)

![](./media/6a322bb608b656d893b14999e1d33e16.png)

**7. Test Code**


```Python
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
```

### Project 42: PIR Motion Sensor

![](./media/b7828b9e5ee615a151567e20d35db90f.png)

**1. Introduction**

In this experiment, we will control an active buzzer and an on-board LED through a PIR motion sensor.

**2. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:0.88611in;height:0.35069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.15in;height:0.62778in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/256a8301b740dfb2981a635a4b575ba0.png" style="width:0.87431in;height:0.66458in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/845ed4e0af474d135a2194d021471570.png" style="width:0.99028in;height:0.6875in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.89722in;height:0.37292in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio PIR Motion Sensor*1</td>
<td>Keyestudio Active Buzzer*1</td>
<td>3P Dupont Wire*2</td>
<td><p>MicroUSB</p>
<p>Cable*1</p></td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Connection Diagram**

![](./media/233a63d63f3aa4fa4113b459173ecd5a.png)

**4. Run the test code：**

Double-click **PIR alarm\.py,** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png)to run the code.

![](./media/567006970f6da6c87821ecfa33d8bac8.png)

**5. Code Explanation：**

**sensor\_pir.irq(trigger=machine.Pin.IRQ\_RISING, handler=pir\_handler)** is the interrupt function. When low levels become high levels trigger, the buzzer will chimp and LED will flash quickly.

**6. Test Result：**

Run the test code, the LED light will flash slowly, and the interrupt trigger mode is IRQ\_RISING. When there are people appear, the PIR motion sensor outputs levels becoming from 0 to 1. The pir\_handler() function is used, and the buzzer will chime, and the LED will flash quickly.

![](./media/1cf0e463659a9c45c5130180071cedc5.jpeg)

![](./media/602557040ec617060709f4214ea3986e.png)

**7. Test Code**


```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 42
 * PIR alarm
 * http://www.keyestudio.com
'''
import machine
import utime

sensor_pir = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(25, machine.Pin.OUT)
buzzer = machine.Pin(16, machine.Pin.OUT)

def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("Warning! Intrusion detected！")
        buzzer.value(1)
        for i in range(20):
            led.toggle()
            utime.sleep_ms(100)

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True:
    led.toggle()
    buzzer.value(0)
    utime.sleep(2)
```


### Project 43: Speaker Module

![](./media/7009513ee4deade529bb95ea74dfe58e.jpeg)

**1. Introduction**

We learned about controlling the speaker module to make sounds, play beats and adjust its volume. In fact, each song is a combination of specific beats and tones (frequencies). In this experiment, we use this speaker module to play a song.

The frequency of each tone is shown below.

Bass:

![Img](./media/img-20231026161432.png)

![Img](./media/img-20231026161448.png)


Midrange :

![Img](./media/img-20231026161521.png)

![Img](./media/img-20231026161544.png)


Treble:

![Img](./media/img-20231026161621.png)

![Img](./media/img-20231026161632.png)


Beats are the time delay for each note. The larger the number, the longer the delay time. A note without a line in the spectrum is a beat, with a delay of 1s. while a beat with an underline is 1/2 of a beat without a line, with a delay of 0.5s, and a beat with two underlines is 1/4 of a beat without a line, with a delay of 0.25s. The 1/8 of a beat is with a delay of 0.125s.

We will take Happy Birthday Song as an example.

**2. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:0.88611in;height:0.35069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.08403in;height:0.59167in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/5de59b8678bdb9244fab05b92cfa796b.png" style="width:0.88542in;height:0.44444in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.89722in;height:0.37292in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio 8002b Audio Power Amplifier*1</td>
<td>3P Dupont Wire*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Connection Diagram**

![](./media/7d9dc904e51e6ce924fa7b14818254f0.png)

**4. Run the test code**

Find and double-click **play music\.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/13b08ed217033f5b4afdc2c748d07b8a.png)

**5. Code Explanation**

We list frequencies of all D keys. Then list the frequencies and beats according to the musical notation. The beat we use is 500ms and can be adjusted. The corresponding beat are looped to become a song.

**6. Test Result**

Connect the components according to the connection diagram and run the test code, the audio power amplifier module will play a birthday song.

![](./media/6887e21a082a2edf42e3060395002f4c.jpeg)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 43
 * play music
 * http://www.keyestudio.com
'''
from machine import Pin, PWM
from utime import sleep
buzzer = PWM(Pin(15))

tones = {
"D1": 262,
"D2": 293,
"D3": 329,
"D4": 349,
"D5": 392,
"D6": 440,
"D7": 494,
"M1": 523,
"M2": 586,
"M3": 658,
"M4": 697,
"M5": 783,
"M6": 879,
"M7": 987,
"H1": 1045,
"H2": 1171,
"H3": 1316,
"H4": 1393,
"H5": 1563,
"H6": 1755,
"H7": 1971
}

song = ["D5","D5","D6","D5","M1","D7",
        "D5","D5","D6","D5","M2","M1",
        "D5","D5","M5","M3","M1","D7","D6",
        "M4","M4","M3","M1","M2","M1"
]

durt = [0.25, 0.25, 0.5, 0.5, 0.5, 1,
       0.25, 0.25, 0.5, 0.5, 0.5, 1,
       0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5,
       0.25, 0.25, 0.5, 0.5, 0.5, 1
]

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)

def playsong(mysong):
    for i in range(len(mysong)):
        playtone(tones[mysong[i]])
        sleep(durt[i])
    bequiet()
playsong(song)
```


### Project 44: Rotary Potentiometer

![](./media/f71165ab140ae6b2aac093dc75785c96.jpeg)

**1. Introduction**

In the previous courses, we did experiments of breathing light and controlling LED with button. In this course, we do these two experiments by controlling the brightness of LED through an adjustable potentiometer. The brightness of LED is controlled by PWM values, and the range of analog values is the same as the PWM’s, from 0 to 65535.

After the code is set successfully, we can control the brightness of the LED on the module by rotating the potentiometer.

**2. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:0.88611in;height:0.35069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.00694in;height:0.55in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/f0ef7a5a2e7eebb09e91f73cb2a6caf3.png" style="width:0.8375in;height:0.64931in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/a0eebfcd8f84c3fbac526e9910e66692.png" style="width:0.91667in;height:0.70292in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.18819in;height:0.63681in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio White LED Module*1</td>
<td>Keyestudio Rotary Potentiometer*1</td>
<td>3P Dupont Wire*2</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Connection Diagram**

![](./media/7a22c3f5cc7105696684fa461594016e.jpeg)

**4. Run the test code：**

Double-click adjust the **light\.py**，and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png)to run the test code.

![](./media/9d0a957a7a1cb73a7e5f26d69867ced8.png)

**5. Code Explanation：**

MicroPython make the value range of ADC between 0 and 65535, just assign the value directly, which is simple and convenient.

**6. Test Result：**

Run the test code and turn the potentiometer on the module to adjust the brightness of the LED module.

![](./media/fb539b0ef1a98d292aa6e3de177af86a.jpeg)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 44
 * Encoder control RGB
 * http://www.keyestudio.com
'''
import time
from rotary_irq_rp2 import RotaryIRQ
from machine import Pin, PWM

pwm_r = PWM(Pin(9))
pwm_g = PWM(Pin(10))
pwm_b = PWM(Pin(11))

pwm_r.freq(1000)
pwm_g.freq(1000)
pwm_b.freq(1000)

def light(red, green, blue):
    pwm_r.duty_u16(red)
    pwm_g.duty_u16(green)
    pwm_b.duty_u16(blue)

SW=Pin(20,Pin.IN,Pin.PULL_UP)
r = RotaryIRQ(pin_num_clk=18,
              pin_num_dt=19,
              min_val=0,
              reverse=False,
              range_mode=RotaryIRQ.RANGE_UNBOUNDED)

while True:
    val = r.value()
    print(val%3)
    if val%3 == 0:
        light(65535, 0, 0)
    elif val%3 == 1:
        light(0, 65535, 0)
    elif val%3 == 2:
        light(0, 0, 65535)
    time.sleep(0.1)
```

### Project 45: Smart Windows

![](./media/fd7384d737b0393e91d42523f4d65b07.jpeg)

**1. Description**

In life, we can see all kinds of smart products, such as smart home. Smart homes include smart curtains, smart windows, smart TVs, smart lights, and more. In this experiment, we use a steam sensor to detect rainwater, and then achieve the effect of closing and opening the window by a servo.

**2. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.45417in;height:0.79306in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b64cdb5749df7d2b7dd3719216c7aff3.png" style="width:0.91458in;height:0.65417in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9a96e60ed3aee985db5d4dcaf9bf38b.png" style="width:1.05833in;height:1.05069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.94722in;height:0.41875in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio Steam Sensor*1</td>
<td>Servo*1</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Connection Diagram**

![](./media/5b7ef53f84cb0dc5bafb9b1fc6f72958.png)

**4. Run the test code**

Find and double-click **button control LED\.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/a4d7d2fc689d303f680fc21d8036589f.png)

**5. Code Explanation**

We can control a servo to rotate by a threshold.

**6. Test Result**

Wire up and run the test code. When the sensor detects a certain amount of water, the servo rotates to achieve the effect of closing or opening windows.

![](./media/d9aa58963d4cad639b9b77adb718446c.jpeg)

**7. Test Code**


```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 45
 * adjust the light
 * http://www.keyestudio.com
'''
import machine
import utime

potentiometer = machine.ADC(26)

pwm = machine.PWM(machine.Pin(15))
pwm.freq(1000)

while True:
    pot_value = potentiometer.read_u16()
    pwm.duty_u16(pot_value)
    utime.sleep(0.1)
```


### Project 46: Sound Activated Light

![](./media/f3ddb58e83a92a888d3e1d66f7456170.png)

**1. Introduction**

In this lesson, we will make a smart sound activated light using a sound sensor and an LED module. When we make a sound, the light will automatically turn on; when there is no sound, the lights will automatically turn off. How it works? Because the sound-controlled light is equipped with a sound sensor, and this sensor converts the intensity of external sound into a corresponding value. Then set a threshold, when the threshold is exceeded, the light will turn on, and when it is not exceeded, the light will go out.

**2. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:0.88611in;height:0.35069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:0.97431in;height:0.53194in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/cf7b54ba090f4e34025101cf9ece26d1.png" style="width:0.90903in;height:0.7125in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/f0ef7a5a2e7eebb09e91f73cb2a6caf3.png" style="width:0.92153in;height:0.62847in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.94583in;height:0.44375in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Sound Sensor*1</td>
<td>Keyestudio White LED Module*1</td>
<td>3P Dupont Wire*2</td>
<td><p>MicroUSB</p>
<p>Cable*1</p></td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Connection Diagram**

![](./media/596547cf8d0b9124d6a38bed32b87487.jpeg)

**4. Run the Test Code：**

Double-click **sound-controlled lights\.py** and clock![](./media/d1dbbae869194ef12c2d684636f1ce4b.png)to run the test code.

![](./media/5e0640558ff2629f345c16d6b3be41bc.png)

**5. Code Explanation：**

In the experiment, we set a threshold of 5000. If the analog value is more than 5000, the LED will be turned on if it exceeds 5000, otherwise it will be turned off.

**6. Test Result：**

Run the test code, the shell displays the corresponding volume analog value. When the value of sound is greater than 5000, the LED module will light up, otherwise it will go out.

![](./media/c8fb96fecf40d3b7e5c71d67ce314722.jpeg)

**7. Test Code**


```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 46
 * Smart_window
 * http://www.keyestudio.com
'''
import utime
from machine import Pin
from machine import PWM

pwm = PWM(Pin(9))#Connect servo to pin GP9
pwm.freq(50)#the cycle is 20ms, so the frequency equals 50Hz
sensor = machine.ADC(26)#ADC0
'''
Duty cycle of some angles
0°----2.5%----1638
45°----5%----3276
90°----7.5%----4915
135°----10%----6553
180°----12.5%----8192
In consideration of errors, allocate the duty cycle within 1000~9000, so that the servo is able to rotate from 0° to 180°
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
```

### Project 47: Fire Alarm

![](./media/e6971103aaa858036b51f3165e0ccb32.jpeg)

**1. Description**

In this experiment, we will make a fire alarm system. Just use a flame sensor to control an active buzzer to emit sounds.

**2. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.45417in;height:0.79306in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/a5e355d0fd3c9b18c7684a9a2b99f0a5.png" style="width:0.90625in;height:0.74167in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/4ecedf84c69e9264059ffd14b02592bd.png" style="width:1.25278in;height:0.70153in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio DIY Active Buzzer*1</td>
<td>keyestudio DIY Flame Sensor*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.94722in;height:0.41875in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Micro USB Cable*1</td>
<td>3P Dupont Wire*1</td>
<td>4P Dupont Wire*1</td>
<td></td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Connection Diagram**

![](./media/949b1d4ea2ce2839c0327456dc803230.png)

**4. Run the test code**

Find and double-click **Flame\_alarm.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/20029e24e31b16de1d58e6c5621c8951.png)

**5. Code Explanation**

This flame sensor uses an analog pin and a digital pin. When a flame is detected, the digital pin outputs a low level. In this experiment we will use the digital port.

**6. Test Result**

Wire up, run the test code and power on. The sensor detects the flame, and the external active buzzer will emit sounds, otherwise the active buzzer will not emit sounds.

![](./media/5e65c74f7e8df9e95e743036381bac47.jpeg)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 47
 * sound-controlled lights
 * http://www.keyestudio.com
'''
import machine
import time

MicroPhone = machine.ADC(26)

led = machine.Pin(15,machine.Pin.OUT)

while True:
    value = MicroPhone.read_u16()
    print(value)
    if value > 5000:
        led.value(1)
        time.sleep(3)
    else:
        led.value(0)
    time.sleep(0.1)
```

### Project 48: Smoke Alarm

![](./media/a1f72c7aa7fd3609401a1f1176b426ec.jpeg)

**1. Description**

In this experiment, we will make a smoke alarm by a TM16504-Digit segment module, a gas sensor and an active buzzer.

**2. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.45417in;height:0.79306in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/a5e355d0fd3c9b18c7684a9a2b99f0a5.png" style="width:0.90625in;height:0.74167in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/f47b077303226cce504ea7734826dfc9.png" style="width:0.94514in;height:0.52569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio Active Buzzer*1</td>
<td>Keyestudio TM16504-Digit Segment Module*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/ee4483f37a6f3609acdb661095f4b706.png" style="width:1.04167in;height:0.52708in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.94722in;height:0.41875in" /></td>
</tr>
<tr class="even">
<td>keyestudio Analog Gas Senso*1</td>
<td>3P Dupont Wire*1</td>
<td>4P Dupont Wire*2</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Connection Diagram**

![](./media/6a3162e64cbf27036ef9df7364466c83.png)

**4. Run the test code**

Find and double-click **smoke\_alarm.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/eb30da8c5ae0cf0455edcd60abac3ced.png)

**5. Code Explanation**

Define an integer variable val to store the analog value of the smoke sensor, and then we display the analog value in the four-digit digital tube, and then set a threshold, and when the threshold is reached, the buzzer will sound.

**6. Test Result**

Run the test code, wire up and power on. When the concentration of combustible gas exceeds the standard, the active buzzer module will give an alarm, and the four-digit digital tube will display the concentration value.

![](./media/1faab116c722135abb1af911f07bb04e.jpeg)

**7. Test Code**

```Python
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
```

### Project 49: Fire Alarm

![](./media/e6971103aaa858036b51f3165e0ccb32.jpeg)

**1. Description**

In this experiment, we will make a fire alarm system. Just use a flame sensor to control an active buzzer to emit sounds.

**2. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.45417in;height:0.79306in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/a5e355d0fd3c9b18c7684a9a2b99f0a5.png" style="width:0.90625in;height:0.70167in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/4ecedf84c69e9264059ffd14b02592bd.png" style="width:0.95278in;height:0.57153in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Keyestudio DIY Active Buzzer*1</td>
<td>keyestudio DIY Flame Sensor*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.94722in;height:0.41875in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Micro USB Cable*1</td>
<td>3P Dupont Wire*1</td>
<td>4P Dupont Wire*1</td>
<td></td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Wiring Diagram**

![](./media/949b1d4ea2ce2839c0327456dc803230.png)

**4. Run the test code**

Find and double-click **Flame\_alarm.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/20029e24e31b16de1d58e6c5621c8951.png)

**5. Code Explanation**

This flame sensor uses an analog pin and a digital pin. When a flame is detected, the digital pin outputs a low level. In this experiment we will use the digital port.

**6. Test Result**

Wire up, run the test code and power on. The sensor detects the flame, and the external active buzzer will emit sounds, otherwise the active buzzer will not emit sounds.

![](./media/5e65c74f7e8df9e95e743036381bac47.jpeg)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 49
 * smoke_alarm
 * http://www.keyestudio.com
'''
from machine import Pin
import time

mq2 = machine.ADC(26)
buzzer = Pin(3, Pin.OUT)
# definitions for TM1650
ADDR_DIS = 0x48  #mode command
ADDR_KEY = 0x49  #read key value command

# definitions for brightness
BRIGHT_DARKEST = 0
BRIGHT_TYPICAL = 2
BRIGHTEST      = 7

on  = 1
off = 0

# number:0~9
NUM = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f] 
# DIG = [0x68,0x6a,0x6c,0x6e]
DIG = [0x6e,0x6c,0x6a,0x68]
DOT = [0,0,0,0]

clkPin = 15
dioPin = 14
clk = machine.Pin(clkPin, machine.Pin.OUT)
dio = machine.Pin(dioPin, machine.Pin.OUT)

DisplayCommand = 0

def writeByte(wr_data):
    global clk,dio
    for i in range(8):
        if(wr_data & 0x80 == 0x80):
            dio.value(1)
        else:
            dio.value(0)
        clk.value(0)
        time.sleep(0.0001)
        clk.value(1)
        time.sleep(0.0001)
        clk.value(0)
        wr_data <<= 1
    return

def start():
    global clk,dio
    dio.value(1)
    clk.value(1)
    time.sleep(0.0001)
    dio.value(0)
    return
    
def ack():
    global clk,dio
    dy = 0
    clk.value(0)
    time.sleep(0.0001)
    dio = Pin(dioPin, machine.Pin.IN)
    while(dio.value() == 1):
        time.sleep(0.0001)
        dy += 1
        if(dy>5000):
            break
    clk.value(1)
    time.sleep(0.0001)
    clk.value(0)
    dio = Pin(dioPin, machine.Pin.OUT)
    return
    
def stop():
    global clk,dio
    dio.value(0)
    clk.value(1)
    time.sleep(0.0001)
    dio.value(1)
    return
    
def displayBit(bit, num):
    global ADDR_DIS
    if(num > 9 and bit > 4):
        return
    start()
    writeByte(ADDR_DIS)
    ack()
    writeByte(DisplayCommand)
    ack()
    stop()
    start()
    writeByte(DIG[bit-1])
    ack()
    if(DOT[bit-1] == 1):
        writeByte(NUM[num] | 0x80)
    else:
        writeByte(NUM[num])
    ack()
    stop()
    return
    
def clearBit(bit):
    if(bit > 4):
        return
    start()
    writeByte(ADDR_DIS)
    ack()
    writeByte(DisplayCommand)
    ack()
    stop()
    start()
    writeByte(DIG[bit-1])
    ack()
    writeByte(0x00)
    ack()
    stop()
    return
    
    
def setBrightness(b = BRIGHT_TYPICAL):
    global DisplayCommand,brightness
    DisplayCommand = (DisplayCommand & 0x0f)+(b<<4)
    return

def setMode(segment = 0):
    global DisplayCommand
    DisplayCommand = (DisplayCommand & 0xf7)+(segment<<3)
    return
    
def displayOnOFF(OnOff = 1):
    global DisplayCommand
    DisplayCommand = (DisplayCommand & 0xfe)+OnOff
    return

def displayDot(bit, OnOff):
    if(bit > 4):
        return
    if(OnOff == 1): 
        DOT[bit-1] = 1;
    else:
        DOT[bit-1] = 0;
    return
        
def InitDigitalTube():
    setBrightness(2)
    setMode(0)
    displayOnOFF(1)
    for _ in range(4):
        clearBit(_)
    return

def ShowNum(num): #0~9999
    displayBit(1,num%10)
    if(num < 10):
        clearBit(2)
        clearBit(3)
        clearBit(4)
    if(num > 9 and num < 100):
        displayBit(2,num//10%10)
        clearBit(3)
        clearBit(4)
    if(num > 99 and num < 1000):
        displayBit(2,num//10%10)
        displayBit(3,num//100%10)
        clearBit(4)
    if(num > 999 and num < 10000):
        displayBit(2,num//10%10)
        displayBit(3,num//100%10)
        displayBit(4,num//1000)

InitDigitalTube()

while True:
    value = mq2.read_u16()//16
    print(value)
    ShowNum(value)
    if value > 1000:
        buzzer.value(1)
    else:
        buzzer.value(0)
    time.sleep(0.1)
```

### Project 50: 6812 RGB Module

![](./media/33c9dd3932993a801689ce26543d76bd.png)

**1. Introduction**

We learned how to use the 6812 RGB module, we knew that this module can light up each LED through a pin. In this experiment, we will control the RGB module to display different colors. 
(<span style="color: rgb(255, 76, 65);">Note:</span> do not look directly at the LEDs for a long time to avoid damage to our eyes.)

**2. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.36597in;height:0.74514in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/35a3f7cd8ec0d409ea3b18f2982a36e9.png" style="width:1.07222in;height:0.68889in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.94583in;height:0.44375in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio 6812 RGB Module*1</td>
<td>3P Dupont Wire*1</td>
<td>MicroUSB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Connection Diagram**

![](./media/a91e603228402e2e94b4a595897da842.jpeg)

**4. Run the test code：**

Double-click **6812\.py** and click ![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the test code.

![](./media/25c713ffc37d880e57804c0322e8f169.png)

**5. Code Explanation：**

**color\_chase(color, wait):** show the color of the water flowing light.

**rainbow\_cycle(0)**：show rainbow effect.

**6. Test Result：**

Wire up and run the code, the 6812RGB module will show black, red, yellow, green, blue, purple and white afterwards

![](./media/edf1b4bd96e8dc5857d193c2ed109557.jpeg)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 50
 * SK6812 RGB
 * http://www.keyestudio.com
'''
# Example using PIO to drive a set of WS2812 LEDs.

import array, time
from machine import Pin
import rp2

# Configure the number of WS2812 LEDs.
NUM_LEDS = 4
PIN_NUM = 15
brightness = 0.2

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()


# Create the StateMachine with the ws2812 program, outputting on pin
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

##########################################################################
def pixels_show():
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g<<16) + (r<<8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(10)

def pixels_set(i, color):
    ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

def color_chase(color, wait):
    for i in range(NUM_LEDS):
        pixels_set(i, color)
        time.sleep(wait)
        pixels_show()
    time.sleep(0.2)
 
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
 
 
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(NUM_LEDS):
            rc_index = (i * 256 // NUM_LEDS) + j
            pixels_set(i, wheel(rc_index & 255))
        pixels_show()
        time.sleep(wait)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

print("chases")
for color in COLORS:       
    color_chase(color, 0.05)

print("rainbow")
rainbow_cycle(0)
```

### Project 51: Ultrasonic Sensor

![](./media/19a7c30e24f0ec39da94912c5535b791.png)

**1. Introduction**

![](./media/38037219a4908755dbedc422be1ab61b.jpeg)

We know that bats use echoes to determine the direction and the location of their preys. In real life, sonar is used to detect sounds in the water. Since the attenuation rate of electromagnetic waves in water is very high, it cannot be used to detect signals, however, the attenuation rate of sound waves in the water is much smaller, so sound waves are most commonly used underwater for observation and measurement. In this experiment, we will use a speaker module, an RGB module and a 4-digit tube display to make a device for detection through ultrasonic.

![](./media/28b75880c1486825f05c902167aba1f2.png)

**2. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.13264in;height:0.61806in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/4a358f0f161b2e4dcae43f9315902ef3.png" style="width:1.03056in;height:0.56806in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/5de59b8678bdb9244fab05b92cfa796b.png" style="width:1.02986in;height:0.61667in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/1dad5a0bec5bc43e3a70df0495f2c5d0.png" style="width:0.93542in;height:0.68264in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>keyes brick HC-SR04 Ultrasonic Sensor*1</td>
<td>Keyestudio Speaker Module*1</td>
<td>Keyestudio Common Cathode RGB Module*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/8f646a7dfa38852a8eccb5e85eb7341a.png" style="width:1.02917in;height:0.57222in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:1.02361in;height:0.39861in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.94583in;height:0.44375in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Keyestudio TM1650 4-Digit Tube Display*1</td>
<td>4P Dupont Wire*3</td>
<td>3P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
<td></td>
</tr>
</tbody>
</table>

**3. Connection Diagram**

![](./media/db145113660a57a8035372f321eb8412.jpeg)

**4. Run the test code：**

Double-click **Ultrasonic radar\.py**，and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png)to run the test code.

![](./media/1434d0037f8159c0fd16d6c47318cd2c.png)

**5. Code Explanation：**

We set the sound frequency and light color by adjusting different distance ranges. We can also adjust the distance range in the above code.

**6. Test Result：**

Wire up according to the connection diagram and run the code. When the ultrasonic sensor detects an obstacle at different distances, the buzzer on the speaker module will produce different frequencies of sound, the RGB will show different colors, and the measured distances will be displayed on the 4-digit tube display.

![](./media/1f3599fe54a1f53bf6eae6eab27c600d.jpeg)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 51
 * Ultrasonic radar
 * http://www.keyestudio.com
'''
from machine import Pin, PWM
import utime

# definitions for TM1650
ADDR_DIS = 0x48  #mode command
ADDR_KEY = 0x49  #read key value command

# definitions for brightness
BRIGHT_DARKEST = 0
BRIGHT_TYPICAL = 2
BRIGHTEST      = 7

on  = 1
off = 0

# number:0~9
NUM = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f] 
# DIG = [0x68,0x6a,0x6c,0x6e]
DIG = [0x6e,0x6c,0x6a,0x68]
DOT = [0,0,0,0]

clkPin = 15
dioPin = 14
clk = machine.Pin(clkPin, machine.Pin.OUT)
dio = machine.Pin(dioPin, machine.Pin.OUT)

DisplayCommand = 0

def writeByte(wr_data):
    global clk,dio
    for i in range(8):
        if(wr_data & 0x80 == 0x80):
            dio.value(1)
        else:
            dio.value(0)
        clk.value(0)
        utime.sleep(0.0001)
        clk.value(1)
        utime.sleep(0.0001)
        clk.value(0)
        wr_data <<= 1
    return

def start():
    global clk,dio
    dio.value(1)
    clk.value(1)
    utime.sleep(0.0001)
    dio.value(0)
    return
    
def ack():
    global clk,dio
    dy = 0
    clk.value(0)
    utime.sleep(0.0001)
    dio = Pin(dioPin, machine.Pin.IN)
    while(dio.value() == 1):
        utime.sleep(0.0001)
        dy += 1
        if(dy>5000):
            break
    clk.value(1)
    utime.sleep(0.0001)
    clk.value(0)
    dio = Pin(dioPin, machine.Pin.OUT)
    return
    
def stop():
    global clk,dio
    dio.value(0)
    clk.value(1)
    utime.sleep(0.0001)
    dio.value(1)
    return
    
def displayBit(bit, num):
    global ADDR_DIS
    if(num > 9 and bit > 4):
        return
    start()
    writeByte(ADDR_DIS)
    ack()
    writeByte(DisplayCommand)
    ack()
    stop()
    start()
    writeByte(DIG[bit-1])
    ack()
    if(DOT[bit-1] == 1):
        writeByte(NUM[num] | 0x80)
    else:
        writeByte(NUM[num])
    ack()
    stop()
    return
    
def clearBit(bit):
    if(bit > 4):
        return
    start()
    writeByte(ADDR_DIS)
    ack()
    writeByte(DisplayCommand)
    ack()
    stop()
    start()
    writeByte(DIG[bit-1])
    ack()
    writeByte(0x00)
    ack()
    stop()
    return
    
    
def setBrightness(b = BRIGHT_TYPICAL):
    global DisplayCommand,brightness
    DisplayCommand = (DisplayCommand & 0x0f)+(b<<4)
    return

def setMode(segment = 0):
    global DisplayCommand
    DisplayCommand = (DisplayCommand & 0xf7)+(segment<<3)
    return
    
def displayOnOFF(OnOff = 1):
    global DisplayCommand
    DisplayCommand = (DisplayCommand & 0xfe)+OnOff
    return

def displayDot(bit, OnOff):
    if(bit > 4):
        return
    if(OnOff == 1): 
        DOT[bit-1] = 1;
    else:
        DOT[bit-1] = 0;
    return
        
def InitDigitalTube():
    setBrightness(2)
    setMode(0)
    displayOnOFF(1)
    for _ in range(4):
        clearBit(_)
    return

def ShowNum(num): #0~9999
    displayBit(1,num%10)
    if(num < 10):
        clearBit(2)
        clearBit(3)
        clearBit(4)
    if(num > 9 and num < 100):
        displayBit(2,num//10%10)
        clearBit(3)
        clearBit(4)
    if(num > 99 and num < 1000):
        displayBit(2,num//10%10)
        displayBit(3,num//100%10)
        clearBit(4)
    if(num > 999 and num < 10000):
        displayBit(2,num//10%10)
        displayBit(3,num//100%10)
        displayBit(4,num//1000)

pwm_r = PWM(Pin(9))
pwm_g = PWM(Pin(10))
pwm_b = PWM(Pin(11))

pwm_r.freq(1000)
pwm_g.freq(1000)
pwm_b.freq(1000)

def light(red, green, blue):
    pwm_r.duty_u16(red)
    pwm_g.duty_u16(green)
    pwm_b.duty_u16(blue)

# Detect the distance through ultrasonic wave, unit: cm
def getDistance(trigger, echo):
    # generate a square wave of 10us
    trigger.low()   #begin with a short low level, to ensure that the high pluse is clear
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)#after the power level is pulled up, wait 10ms, set to a low level immediately
    trigger.low()
    
    while echo.value() == 0: #while loop, detect whether the value is 0 at the echo pin, record the time
        start = utime.ticks_us()
    while echo.value() == 1: #while loop, detect whether the value is 1 at the echo pin, record the time
        end = utime.ticks_us()
    d = (end - start) * 0.0343 / 2 #distance = duration (from the echo being detected to the wave being sene) x velocity of sound  (343.2 m/s, or 0.0343cm/ms) / 2, why devided by 2: the wave made a return
    return d

# Set the pins
trigger = Pin(20, Pin.OUT)
echo = Pin(19, Pin.IN)

buzzer = PWM(Pin(16))

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)
    
# major codes
InitDigitalTube()
while True:
    distance = int(getDistance(trigger, echo))
    ShowNum(distance)
    if distance <= 10:
        playtone(880)
        utime.sleep(0.1)
        bequiet()
        light(65535, 0, 0)
    elif distance <= 20:
        playtone(532)
        utime.sleep(0.2)
        bequiet()
        light(0, 0, 65535)
    else:
        light(0, 65535, 0)
```

### Project 52: IR Remote Control

![](./media/6e823de7db355fde0bc5fcb7c1cdc705.jpeg)

**1. Introduction**

In the previous experiments, we learned to turn on or turn off the LED, adjust the brightness of a light through PWM, and how to use the infrared receiver module. So in this experiment, we use an infrared remote control to control an LED module.

When we receive a value, we set the PWM value by the corresponding button value, thus you can adjust the brightness. Control the LED to turn on or turn off is in the same way. If we want to use the same button to control the LED to turn on or turn off, we can achieve it through the code.

**2. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.30694in;height:0.51806in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.4in;height:0.76389in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/f0ef7a5a2e7eebb09e91f73cb2a6caf3.png" style="width:0.97361in;height:0.69792in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/6df3c3284a300414a237993c97fd5974.png" style="width:0.97639in;height:0.69375in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td><p>Raspberry Pi Pico</p>
<p>Shield*1</p></td>
<td>Keyestudio White LED Module*1</td>
<td><p>Keyestudio</p>
<p>IR Receiver*1</p></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.94583in;height:0.44375in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/10ccf14d80feba64bba0c1eacd02b09d.png" style="width:1.3in;height:0.62847in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td></td>
</tr>
<tr class="even">
<td>MicroUSB Cable*1</td>
<td>Remote Control*1</td>
<td>3P Dupont Wire*2</td>
<td></td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Connection Diagram**

![](./media/3151c2409f0d69871f3b23237ac1014c.jpeg)

**4. Run the test code：**

Double-click **IR control LED\.py**，and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png)to run the code.

![](./media/a7142d9f612addf31ea50f501ea41dad.png)

**5. Code Explanation：**

We define a Boolean variable, values of the Boolean variable are true(True) or false (False).

When we press the OK button, at this time we need to set a Boolean variable flag. When the flag is true (True), the LED will be turned on, and when it is false (False), it will be turned off.

**6. Test Result：**

Wire up, run the code and look at the Shell. Press keys on the IR remote control, the Shell will show values. Press“OK”to turn on the LED, and press it again to turn off the LED.

![](./media/0f071962cee9a34e237184e40e6a96ab.jpeg)

![](./media/61d486deeb8a3daee6e8975b7e51c335.png)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 52
 * IR control LED
 * http://www.keyestudio.com
'''
import time
from machine import Pin

led = Pin(14, Pin.OUT)
ird = Pin(16,Pin.IN)

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

flag = False
while True:
#     global flag
    command = read_ircode(ird)
    print(command, end = "  ")
    print(flag, end = "  ")
    if command == "Ok":
        if flag == True:
            led.value(1)
            flag = False
            print("led on")
        else:
            led.value(0)
            flag = True
            print("led off")
    time.sleep(0.1)
```

### Project 53: Heat Dissipation Device

![](./media/24a7a2d97a50c2f3fc4ab893d3aee394.jpeg)

**1. Description**

We will use a temperature sensor and some modules to make a smart cooling device in this experiment. When the ambient temperature is higher than a certain value, the motor is turned on, thereby reducing the ambient temperature and achieving the heat dissipation effect. Then display the temperature value in the four-digit segment display.

**2. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.45417in;height:0.79306in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/6c2548137a8c675141b83227beeb2eb9.png" style="width:0.82917in;height:0.70694in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/f47b077303226cce504ea7734826dfc9.png" style="width:0.94514in;height:0.52569in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>keyestudio 130 Motor*1</td>
<td>Keyestudio TM1650 4-Digit Segment Display*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/d892bdfa25f3544ae28aa16d8b1b3c50.png" style="width:0.98056in;height:0.73542in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:0.98958in;height:0.36042in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.94722in;height:0.41875in" /></td>
</tr>
<tr class="even">
<td>Keyestudio 18B20 Temperature Sensor*1</td>
<td>3P Dupont Wire*1</td>
<td>4P Dupont Wire*2</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Connection Diagram**

![](./media/3bd1268a47335659a58b4e6ad4ff4a06.png)

**4. Run the test code**

Find and double-click **heat\_abstractor.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png).

![](./media/ccd55885d18003d1acb52e4a7168b4e5.png)

**5. Code Explanation**

The setting of variables and the storage of detection values are the same as what we learned earlier. We also set a temperature threshold and control the rotation of the motor when the threshold is exceeded, and then we use the digital tube to display the temperature value.

**6. Test Result**

Wire up and run the test code. We can see the temperature of the current environment (unit is Celsius) on the four-digit segment display, as shown in the figure below. If this value exceeds the value we set, the fan will rotate to dissipate heat.

![](./media/88055998b773de30de5faa2b4c954cdf.jpeg)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 53
 * heat_abstractor
 * http://www.keyestudio.com
'''
import machine, onewire, ds18x20, time

ds_pin = machine.Pin(3)

ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()

#Set the two pins of the motor
INA = machine.Pin(20, machine.Pin.OUT)
INB = machine.Pin(21, machine.Pin.OUT)
# definitions for TM1650
ADDR_DIS = 0x48  #mode command
ADDR_KEY = 0x49  #read key value command

# definitions for brightness
BRIGHT_DARKEST = 0
BRIGHT_TYPICAL = 2
BRIGHTEST      = 7

on  = 1
off = 0

# number:0~9
NUM = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f] 
# DIG = [0x68,0x6a,0x6c,0x6e]
DIG = [0x6e,0x6c,0x6a,0x68]
DOT = [0,0,0,0]

clkPin = 15
dioPin = 14
clk = machine.Pin(clkPin, machine.Pin.OUT)
dio = machine.Pin(dioPin, machine.Pin.OUT)

DisplayCommand = 0

def writeByte(wr_data):
    global clk,dio
    for i in range(8):
        if(wr_data & 0x80 == 0x80):
            dio.value(1)
        else:
            dio.value(0)
        clk.value(0)
        time.sleep(0.0001)
        clk.value(1)
        time.sleep(0.0001)
        clk.value(0)
        wr_data <<= 1
    return

def start():
    global clk,dio
    dio.value(1)
    clk.value(1)
    time.sleep(0.0001)
    dio.value(0)
    return
    
def ack():
    global clk,dio
    dy = 0
    clk.value(0)
    time.sleep(0.0001)
    dio = machine.Pin(dioPin, machine.Pin.IN)
    while(dio.value() == 1):
        time.sleep(0.0001)
        dy += 1
        if(dy>5000):
            break
    clk.value(1)
    time.sleep(0.0001)
    clk.value(0)
    dio = machine.Pin(dioPin, machine.Pin.OUT)
    return
    
def stop():
    global clk,dio
    dio.value(0)
    clk.value(1)
    time.sleep(0.0001)
    dio.value(1)
    return
    
def displayBit(bit, num):
    global ADDR_DIS
    if(num > 9 and bit > 4):
        return
    start()
    writeByte(ADDR_DIS)
    ack()
    writeByte(DisplayCommand)
    ack()
    stop()
    start()
    writeByte(DIG[bit-1])
    ack()
    if(DOT[bit-1] == 1):
        writeByte(NUM[num] | 0x80)
    else:
        writeByte(NUM[num])
    ack()
    stop()
    return
    
def clearBit(bit):
    if(bit > 4):
        return
    start()
    writeByte(ADDR_DIS)
    ack()
    writeByte(DisplayCommand)
    ack()
    stop()
    start()
    writeByte(DIG[bit-1])
    ack()
    writeByte(0x00)
    ack()
    stop()
    return
    
    
def setBrightness(b = BRIGHT_TYPICAL):
    global DisplayCommand,brightness
    DisplayCommand = (DisplayCommand & 0x0f)+(b<<4)
    return

def setMode(segment = 0):
    global DisplayCommand
    DisplayCommand = (DisplayCommand & 0xf7)+(segment<<3)
    return
    
def displayOnOFF(OnOff = 1):
    global DisplayCommand
    DisplayCommand = (DisplayCommand & 0xfe)+OnOff
    return

def displayDot(bit, OnOff):
    if(bit > 4):
        return
    if(OnOff == 1): 
        DOT[bit-1] = 1;
    else:
        DOT[bit-1] = 0;
    return
        
def InitDigitalTube():
    setBrightness(2)
    setMode(0)
    displayOnOFF(1)
    for _ in range(4):
        clearBit(_)
    return

def ShowNum(num): #0~9999
    displayBit(1,num%10)
    if(num < 10):
        clearBit(2)
        clearBit(3)
        clearBit(4)
    if(num > 9 and num < 100):
        displayBit(2,num//10%10)
        clearBit(3)
        clearBit(4)
    if(num > 99 and num < 1000):
        displayBit(2,num//10%10)
        displayBit(3,num//100%10)
        clearBit(4)
    if(num > 999 and num < 10000):
        displayBit(2,num//10%10)
        displayBit(3,num//100%10)
        displayBit(4,num//1000)

InitDigitalTube()
print('Found DS devices: ', roms)

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        value = ds_sensor.read_temp(rom)
        print(value)
        ShowNum(int(value))
        if value > 28:
            INA.value(0)
            INB.value(1)
        else:
            INA.value(0)
            INB.value(0)
```

### Project 54: Intelligent Entrance Guard System

![](./media/6dbae618241cc2dd3060dc4abf94f3a6.jpeg)

**1. Description**

In this project, we use the RFID522 card swiping module and the servo to set up an intelligent access control system. The principle is very simple.We use RFID522 swipe card module, an IC card or key card to unlock.

**2. Required Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:1.02986in;height:0.40833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.45417in;height:0.79306in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/decf08b83c5594f7f1e51f6e93051f4b.png" style="width:1.30208in;height:0.69722in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/2a40c5c68dc7802d29bcf719bb688f64.png" style="width:1.19722in;height:0.75347in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Key*1</td>
<td>IC Card*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/530cb53e5b1e1b140de487cfc46be453.png" style="width:1.18194in;height:0.65972in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9a96e60ed3aee985db5d4dcaf9bf38b.png" style="width:1.05833in;height:1.05069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:0.91458in;height:0.35625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:0.94722in;height:0.41875in" /></td>
</tr>
<tr class="even">
<td>Keyestudio RFID Module*1</td>
<td>Servo*1</td>
<td>4P Dupont Wire*1</td>
<td>Micro USB Cable*1</td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Wiring Diagram**

![](./media/767a8adc302e88943bd4bd9a07b91895.png)

**4. Run the code:**

Find **Intelligent access control\.py** and double-click it and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png)to run the code.

![](./media/caf6ad40fb359850f7b72945ef25ac38.png)

**5. Code Explanation**

In the previous experiment, our card swipe module has tested the information of IC card and key. Then we use this corresponding information to control the door.

**6. Test Result**

Upload the test code, wire up and power up with a USB cable, open the shell and set the baud rate to 9600; the shell displays information.

When we use the IC card or blue key to swipe the card, the shell displays the card information and "open the door", as shown in the figure below, the servo rotates to the corresponding angle to simulate opening the door.

![](./media/ba07989a5df2bb430f79f6fe486a4fa9.jpeg)

**7. Test Code**

```Python
'''
 * Keyestudio 37 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 54
 * Intelligent access control
 * http://www.keyestudio.com
'''
from machine import Pin, PWM
import time
from mfrc522_i2c import mfrc522

pwm = PWM(Pin(10))
pwm.freq(50)

'''
Duty cycle of some angles
0°----2.5%----1638
45°----5%----3276
90°----7.5%----4915
135°----10%----6553
180°----12.5%----8192
'''
angle_0 = 1638
angle_90 = 4915
angle_180 = 8192

#i2c config
addr = 0x28
scl = 5
sda = 4
    
rc522 = mfrc522(scl, sda, addr)
rc522.PCD_Init()
rc522.ShowReaderDetails()            # Show details of PCD - MFRC522 Card Reader details

uid1 = [29, 75, 135, 90]
uid2 = [76, 115, 76, 99]

pwm.duty_u16(angle_180)
time.sleep(1)

while True:
    if rc522.PICC_IsNewCardPresent():
        #print("Is new card present!")
        if rc522.PICC_ReadCardSerial() == True:
            print("Card UID:", end=' ')
            print(rc522.uid.uidByte[0 : rc522.uid.size])
            if rc522.uid.uidByte[0 : rc522.uid.size] == uid1 or rc522.uid.uidByte[0 : rc522.uid.size] == uid2:
                pwm.duty_u16(angle_0)
            else :
                pwm.duty_u16(angle_180)
            time.sleep(500)
```

### Project 55: Comprehensive Experiment

![](./media/c92bfcbd1ecd7fe91198066d0c9a4df6.jpeg)

**1. Introduction**

We did a lot of experiments, and for each one we needed to re-upload the code, so can we achieve different functions through an experiment? In this experiment, we will use an external button module to achieve different functions.

**2. Components**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/c4bec8956b5785f9b6c98b310e182d18.png" style="width:0.94097in;height:0.37292in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/b9233c67c93c243214388d668afe2eab.png" style="width:1.02431in;height:0.55903in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/f0ef7a5a2e7eebb09e91f73cb2a6caf3.png" style="width:0.97292in;height:0.69722in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/61562768f0c149f53eece4c54ec8c250.png" style="width:0.97708in;height:0.70347in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/a0eebfcd8f84c3fbac526e9910e66692.png" style="width:0.96319in;height:0.68472in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico Board*1</td>
<td>Raspberry Pi Pico Shield*1</td>
<td>Keyestudio Purple LED Module*1</td>
<td>Keyestudio Button Module*1</td>
<td>Keyestudio Rotary Potentiometer*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/6df3c3284a300414a237993c97fd5974.png" style="width:0.95069in;height:0.65972in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/fb4fa5fdd5689ded9c213ba5ceb34c0d.png" style="width:1.04097in;height:0.61319in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/4a358f0f161b2e4dcae43f9315902ef3.png" style="width:0.97847in;height:0.53958in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/35a3f7cd8ec0d409ea3b18f2982a36e9.png" style="width:0.91458in;height:0.64583in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/edbfec59fe015bd9987e4b4d542b466d.png" style="width:1.07361in;height:0.42778in" /></td>
</tr>
<tr class="even">
<td><p>Keyestudio</p>
<p>IR Receiver*1</p></td>
<td>Keyestudio Joystick Module*1</td>
<td>HC-SR04 Ultrasoic Sensor*1</td>
<td>Keyestudio 6812 RGB Module*1</td>
<td>MicroUSB Cable*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/0d81e07a0f67700c5a396fc7e1e614e1.jpeg" style="width:1.10069in;height:0.40069in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/269c154eda332be03643bada56070124.jpeg" style="width:1.14722in;height:0.44722in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/fc3fd9c0110b04d1af77a2ff8c01a10a.png" style="width:1.10417in;height:0.46319in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/master/media/10ccf14d80feba64bba0c1eacd02b09d.png" style="width:0.90903in;height:0.43958in" /></td>
<td></td>
</tr>
<tr class="even">
<td>3P Dupont Wire*5</td>
<td>4P Dupont Wire*1</td>
<td>5P Dupont Wire*1</td>
<td>Remote Control*1</td>
<td></td>
</tr>
</tbody>
</table>

<br>
<br>

**3. Connection Diagram**

![](./media/c3b005ad32585755f42b3fc283101f78.jpeg)

**4. Run the Test Code：**

Double-click **Comprehensive experiment\.py** and click![](./media/d1dbbae869194ef12c2d684636f1ce4b.png) to run the code.

![](./media/e89463a21f4fdc102f30ac559514b45e.png)

Calculate how many times the button is pressed, divide it by 7, and get the remainder which is 0, 1 2, 3, 4, 5 or 6. According to different remainders, construct five unique functions to control the experiment and realize different functions.

**5. Test Result**

![](./media/7f553375104897d12ae882016855d1ee.jpeg)

Upload the test code, wire up and power on with a USB cable.

At the beginning, the number of the button is 0 and remainder is 0.

Four beads on the 6812RGB module flash random colors. Open the serial monitor.

![](./media/f8cf9846de9f63d38b8668eab39110e8.png)

Press the button for a while, 6812 stops flashing, press once, the remainder is 1. If we point at IR receiver with the infrared remote control and press the button,the serial monitor will display as follows.

![](./media/b6a51e823623e27830604fabc6c282ce.png)

Press the key twice, the time of pressing buttons is 2 and the remainder is 2. Read temperature and humidity values. As shown below;

<span style="color: rgb(255, 76, 65);">Note:</span> we need to press any a key, because the IR reception function waits for signals.

![](./media/c2150666be7b44ae30d33af53ca2b86b.png)

Press a key again, the time of pressing buttons is 3 and the remainder is 3. Read digital values at x, y and z axis of the joystick module. As shown below;

![](./media/092c97bb75654c3c81f340d76ee6e527.png)

Press the key for the fourth time, the remainder is 4. Then the potentiometer can adjust the PWM value at the GP14 port to control LED brightness of the purple LED

![](./media/49bd493b9e0f180f393f5865acfc4227.png)

Press the key for the fifth time, the remainder is 5. Then the obstacle avoidance sensor can detect obstacles, as shown below;

![](./media/10bd0a8d0796a74ee14731c52bbde4a5.png)

Press the key for the sixth time, the remainder is 6. Then the ultrasonic sensor can detect distance away from obstacles, as shown below;

![](./media/7454488d35a1150665cf6b11ff22e942.png)

Press the key for seventh time and the remainder is 0. Then the RGB will flash. If you press keys incessantly, remainders will change in loop way. So does functions.

**6. Test Code**

```Python
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
# Set the two pins of ultrasonic sensor
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


# Detect the distance through ultrasonic wave, unit: cm
def getDistance(trigger, echo):
    # generate a square wave of 10us
    trigger.low()   #begin with a short low level, to ensure that the high pluse is clear
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)#after the power level is pulled up, wait 10ms, set to a low level immediately
    trigger.low()
    
    while echo.value() == 0: #while loop, detect whether the value is 0 at the echo pin, record the time
        start = time.ticks_us()
    while echo.value() == 1: #while loop, detect whether the value is 1 at the echo pin, record the time
        end = time.ticks_us()
    d = (end - start) * 0.0343 / 2 #distance = duration (from the echo being detected to the wave being sene) x velocity of sound  (343.2 m/s, or 0.0343cm/ms) / 2, why devided by 2: the wave made a return
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
    nums = keys % 7  #button pressed times devided by 7, record its remainder numbers: they are 0, 1, 2, 3, 4, 5 and 6
    if nums == 0:  #show RGB
        showRGB()
    elif nums == 1:  #show the value received by the IR receiver
        IRreceive()
    elif nums == 2:  #display the temperature and humidity value
        showxht11()
    elif nums == 3:  #show the value of the joystick
        showJoystick()
    elif nums == 4:  #light up the LED on the potentiometer
        adjustLight()
    elif nums == 5:  #display the information about obstacles
        showAvoid()
    elif nums == 6:  #print the distance value detected by the ultrasonic sensor
        showDistance()

```













