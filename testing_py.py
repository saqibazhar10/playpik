import RPi.GPIO as GPIO
from time import sleep

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
joystick_pins = [17, 27, 22]  # Modify these as per your joystick pin configuration

# Define joystick directions
joystick_up = False
joystick_down = False
joystick_left = False
joystick_right = False

# Callback function for joystick movement
def joystick_callback(channel):
    global joystick_up, joystick_down, joystick_left, joystick_right
    
    if channel == joystick_pins[0]:
        joystick_up = GPIO.input(channel)
    elif channel == joystick_pins[1]:
        joystick_down = GPIO.input(channel)
    elif channel == joystick_pins[2]:
        joystick_left = GPIO.input(channel)

    # Uncomment the line below if your joystick has a separate pin for right movement
    # elif channel == joystick_pins[3]:
    #     joystick_right = GPIO.input(channel)

# Set up GPIO pins for joystick input
for pin in joystick_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=joystick_callback)

# Main loop
try:
    while True:
        if joystick_up:
            print('Joystick Up')
        elif joystick_down:
            print('Joystick Down')
        elif joystick_left:
            print('Joystick Left')
        elif joystick_right:
            print('Joystick Right')
        else:
            print('No Joystick Movement')

        sleep(0.1)  # Adjust the delay as needed

except KeyboardInterrupt:
    GPIO.cleanup()
