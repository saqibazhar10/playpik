import RPi.GPIO as GPIO

JOYSTICK_VRX_PIN = 17
JOYSTICK_VRY_PIN = 27
JOYSTICK_SW_PIN = 22


GPIO.setmode(GPIO.BCM)
GPIO.setup(JOYSTICK_VRX_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(JOYSTICK_VRY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(JOYSTICK_SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    if GPIO.input(JOYSTICK_VRX_PIN) == GPIO.LOW:
        print("Joystick moved left on X-axis")
    elif GPIO.input(JOYSTICK_VRX_PIN) == GPIO.HIGH:
        print("Joystick moved right on X-axis")

    if GPIO.input(JOYSTICK_VRY_PIN) == GPIO.LOW:
        print("Joystick moved down on Y-axis")
    elif GPIO.input(JOYSTICK_VRY_PIN) == GPIO.HIGH:
        print("Joystick moved up on Y-axis")

    if GPIO.input(JOYSTICK_SW_PIN) == GPIO.LOW:
        print("Joystick switch pressed")

GPIO.cleanup()
