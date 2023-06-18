import RPi.GPIO as GPIO
from email_new  import snd_email

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define pin numbers for VRX, VRY, and SW
VRX_PIN = 17
VRY_PIN = 27
SW_PIN = 22

import requests

def get_weather_and_humidity(country):
    api_key = 'ee5696d5565f9607a0ee20de76d5aea9'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {'q': country, 'appid': api_key, 'units': 'metric'}
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather = data['weather'][0]['description']
            humidity = data['main']['humidity']
            temp = data['main']['temp']
            wind = data['wind']['speed']
            icon= data['weather'][0]['icon']



            return weather, humidity ,temp ,wind,icon
        else:
            print('Error:', data['message'])
            return None
    except requests.RequestException as e:
        print('Request Error:', str(e))
        return None

# Set VRX and VRY pins as analog inputs
GPIO.setup(VRX_PIN, GPIO.IN)
GPIO.setup(VRY_PIN, GPIO.IN)

# Set SW pin as a digital input with a pull-up resistor
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define the available options
options= ['London-UK','Washington D.C.-US','Rome-Italy','Valletta-Malta','Berlin-Germany'
            ,'Paris-France','Madrid-Spain','Beijing-China','Moscow-Russia','Tokyo-Japan']
current_option = 0
move_forward = False
move_backward = False

def select_option(forward=True):
    global current_option
    if forward:
        current_option = (current_option + 1) % len(options)
    else:
        current_option = (current_option - 1) % len(options)
    print("Selected:", options[current_option])

try:
    while True:
        # Read the values from VRX, VRY, and SW pins
        vrx_value = GPIO.input(VRX_PIN)
        vry_value = GPIO.input(VRY_PIN)
        sw_value = GPIO.input(SW_PIN)

        # Print the joystick values
        

        # Check joystick movement for option selection
        if vrx_value == 0 and vry_value == 1:
#             print(f"VRX: {vrx_value}, VRY: {vry_value}, SW: {sw_value}")
            move_forward = True
            move_backward = False
        elif vrx_value == 1 and vry_value == 0:
            move_backward = True
            move_forward = False
        elif vrx_value == 1 and vry_value == 1:
            if move_forward:
                select_option(forward=True)
                move_forward = False
            elif move_backward:
                select_option(forward=False)
                move_backward = False
        if sw_value == 0:
            result=get_weather_and_humidity(options[current_option].split('-')[0])
            if result:
                weather, humidity ,temp,wind,icon= result
                print(f"Weather : {weather}")
                print(f"Humidity  : {humidity}%")
                print(f"Temperature  : {temp}°C")
                print(f"Wind  : {wind} m/s")
                snd_email(weather,humidity,temp,wind,str(icon),options[current_option])
            

except KeyboardInterrupt:
    GPIO.cleanup()

