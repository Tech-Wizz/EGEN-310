import sys
sys.path.insert(0, '/home/pi/.local/lib/python3.7/site-packages')
from gpiozero import LED
from time import sleep
import keyboard

rightMotor = LED(16)
leftMotor = LED(25)
pump = LED(24)
horn = LED(17)

horn.on()
sleep(1)
horn.off()


while True:

    while keyboard.is_pressed("w"):	
        rightMotor.on()
        leftMotor.on()
        print("Forward")

    while keyboard.is_pressed("a"):
        rightMotor.on()
        print("RIGHT")

    while keyboard.is_pressed("d"):
        leftMotor.on()
        print("LEFT")

    while keyboard.is_pressed("p"):
        pump.on()
        print("PUMP")

    while keyboard.is_pressed("h"):
        horn.on()
        print("Beep!")

    rightMotor.off()
    leftMotor.off()
    pump.off()
    horn.off()

