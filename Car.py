from gpiozero import LED
from time import sleep
import keyboard

rightMotor = LED(16)
leftMotor = LED(25)
pump = LED(24)

while True:
    while keyboard.is_pressed("w") or keyboard.is_pressed("W"):	
	rightMotor.on()
	leftMotor.on()
	print("Forward")
    while keyboard.is_pressed("s") or keyboard.is_pressed("S"):
        rightMotor.on()
        print("RIGHT")
    while keyboard.is_pressed("d") or keyboard.is_pressed("D"):
        leftMotor.on()
        print("LEFT")
    while keyboard.is_pressed("p") or keyboard.is_pressed("P"):
        pump.on()
        print("PUMP")
    rightMotor.off()
    leftMotor.off()
    pump.off()

