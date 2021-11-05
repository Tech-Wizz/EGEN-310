from gpiozero import LED
from time import sleep
import keyboard

led = LED(17)

while True:
    while keyboard.is_pressed("l"):
        led.on()
        print("ON")
    led.off()
    print("OFF")
    
