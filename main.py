import RPi.GPIO as io
io.setmode(io.BCM)
# import sys, tty, termios, time

# Assuming we are using 2 DC motors, this code chunk configures the PWM settings.
# Defines the two GPIO pins used for the input, starts the PWM, initializes motor speed = 0
# NOTE: for

# motor 1
motor1_in1_pin = 4
motor1_in2_pin = 17
io.setup(motor1_in1_pin, io.OUT)
io.setup(motor1_in2_pin, io.OUT)
motor1 = io.PWM(4,100)
motor1.start(0)
motor1.ChangeDutyCycle(0)

# motor 2
motor2_in1_pin = 24
motor2_in2_pin = 25
io.setup(motor2_in1_pin, io.OUT)
io.setup(motor2_in2_pin, io.OUT)
motor2 = io.PWM(4,100)
motor2.start(0)
motor2.ChangeDutyCycle(0)

# determine which key has been pressed by user on the keyboard by accessing the system files
# returns the pressed key as a variable
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# defines the methods used to determine whether a motor needs to spin forward or backwards
# different directions are achieved by setting one of the GPIO pins to true and the other to false.
# If status of both pins match, motor will not turn.

def motor1_forward():
    io.output(motor1_in1_pin, True)
    io.output(motor1_in2_pin, False)

def motor1_reverse():
    io.output(motor1_in1_pin, False)
    io.output(motor1_in2_pin, True)

def motor2_forward():
    io.output(motor2_in1_pin, True)
    io.output(motor2_in2_pin, False)

def motor2_reverse():
    io.output(motor2_in1_pin, False)
    io.output(motor2_in2_pin, True)

# toggle the direction of the steering motor.
# determines whether user wants to turn left or right via key press, makes the appropriate adjustment
# toggle = **program cannot read multiple pressed keys at the same time**
# possible wheel positions: "right", "centre" and "left" (wheel is metaphorical, no actual wheel)
# finally, update the wheel status to access next time it is called

def toggleSteering(direction):

    global wheelStatus

    if(direction == "right"):
        if(wheelStatus == "center"):
            motor1_forward()
            motor1.ChangeDutyCycle(99)
            wheelStatus = "right"
        elif(wheelStatus == "left"):
            motor1.ChangeDutyCycle(0)
            wheelStatus = "center"

    if(direction == "left"):
        if(wheelStatus == "center"):
            motor1_reverse()
            motor1.ChangeDutyCycle(99)
            wheelStatus = "left"
        elif(wheelStatus == "right"):
            motor1.ChangeDutyCycle(0)
            wheelStatus = "center"

# Setting the PWM pins to false so the motors will not move
# until the user presses the first key
io.output(motor1_in1_pin, False)
io.output(motor1_in2_pin, False)
io.output(motor2_in1_pin, False)
io.output(motor2_in2_pin, False)

# Global variable for the status of  steering
wheelStatus = "center"

# FOR TESTING PROTOTYPE 1
# Instructions for when the user has an interface
print("w/s: acceleration")
print("a/d: steering")
print("x: exit")

# Infinite loop that will not end until the user presses the
# exit key
while True:
    # Keyboard character retrieval method is called and saved into variable
    char = getch()

    # The car will drive forward when the "w" key is pressed
    if(char == "w"):
        motor2_forward()
        motor2.ChangeDutyCycle(99)

    # The car will reverse when the "s" key is pressed
    if(char == "s"):
        motor2_reverse()
        motor2.ChangeDutyCycle(99)

    # The "a" key will toggle the steering left
    if(char == "a"):
        toggleSteering("left")

    # The "d" key will toggle the steering right
    if(char == "d"):
        toggleSteering("right")

    # The "x" key will break the loop and exit the program
    if(char == "x"):
        print("Program Ended")
        break

    # At the end of each loop the acceleration motor will stop and wait for its next command
    motor2.ChangeDutyCycle(0)

    # The keyboard character variable set to blank, saves the next pressed key
    char = ""

# Program will cease all GPIO activity before terminating
io.cleanup()
