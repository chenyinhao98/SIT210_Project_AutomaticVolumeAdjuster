import RPi.GPIO as GPIO
import time
 

soundsensor = 8

GPIO.setmode(GPIO.BOARD)
 
GPIO.setup(soundsensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def callback(soundsensor):
    if (GPIO.input(soundsensor)):
            print ("Noise Detected!")
    else:
            print("Noise Detected!")

GPIO.add_event_detect(soundsensor,GPIO.BOTH, bouncetime =300)
GPIO.add_event_callback(soundsensor,callback)
            
try:
    
    while 1:
        time.sleep(1)


except KeyboardInterrupt:

    GPIO.cleanup()