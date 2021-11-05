from gpiozero import LED
from time import sleep
import keyboard

rightMotor = LED(16)
leftMotor = LED(25)
pump = LED(24)

while True:
    while keyboard.is_pressed("s"):
        rightMotor.on()
        print("RIGHT")
    while keyboard.is_pressed("a"):
        leftMotor.on()
        print("LEFT")
    while keyboard.is_pressed("w"):
        leftMotor.on()
        print("RIGHT")
    rightMotor.off()
    leftMotor.off()
    pump.off()

    print("OFF")
    
