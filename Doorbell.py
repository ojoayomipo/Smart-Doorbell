import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import blynklib
import time

BLYNK_AUTH = "ENTER YOUR BLYNK AUTH"
TARGET_EMAIL = "ENTER YOUR EMAIL ADDRESS"
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#Define a callback function for the button press.

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)



def button_callback(channel):
    print("Button was pushed!")
    blynk.notify('Someone is at the door')
    blynk.email(TARGET_EMAIL, 'Video DoorBell', "Someone is at the door!")
    #blynk.virtual_write(V1, 1)

#     @blynk.handle_event('write V1')
#     def write_handler(pin, value):
#         blynk.set_property(V1, "url", 1, "http://10.20.224.68:8080/photo.jpg")
#         blynk.virtualwrite(V1, 1)  


#attach event to button pin
GPIO.add_event_detect(10, GPIO.FALLING, callback=button_callback)

#GPIO.cleanup()
print("exited")
while True:
    blynk.run()
