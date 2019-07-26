
"""
Names: Mirissa Naidu
Student Number: NDXMIR002
Prac: 1
Date: 22/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time 
from time import sleep

# Define Variables

L0 = None                # LSB displayed 
L1 = None                # bit displayed
L2 = None                # MSB bit displayed
SW0 = None
SW1 = None
binary = None            # shows the integer number to be displayed on LED 
current_number = 0

# GPIO configuration/Pin set-up
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)                                         # setup pins using board config

GPIO.setup(7, GPIO.OUT, initial = GPIO.LOW)                    # sets LED to output with initial value output low
GPIO.setup(11, GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(15, GPIO.OUT,initial = GPIO.LOW)

GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)  # setup button on pin 16 using pull-down resistor
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)  # setup button on pin 18 using pull-down resistor


# Function that sets the value of the LED to HIGH or LOW

def setLED(L2, L1, L0):

        if (L0 == 0):
                GPIO.output(7, GPIO.LOW)
        else:
                GPIO.output(7, GPIO.HIGH)

        if (L1 == 0):
                GPIO.output(11, GPIO.LOW)
        else:
                GPIO.output(11, GPIO.HIGH)

        if (L2 == 0):
                GPIO.output(15, GPIO.LOW)
        else:
                GPIO.output(15, GPIO.HIGH)

# Function that sets LED output to a integer value

def displayLED(binary):

        if (binary == 0):
                   setLED(0,0,0)

        if (binary == 1):
                   setLED(0,0,1)

        if (binary == 2):
                   setLED(0,1,0)

        if (binary == 3):
                   setLED(0,1,1)

        if (binary == 4):
                   setLED(1,0,0)

        if (binary == 5):
                   setLED(1,0,1)

        if (binary == 6):
                   setLED(1,1,0)

        if (binary == 7):
                   setLED(1,1,1)

# Function that increases the current number and displays it
 
def increase():
	
        global current_number
	current_number += 1
	if current_number > 7 :
	   current_number = 0
       
        displayLED(current_number)

# Function that decreases the current number and displays it 

def decrease():
	
	global current_number
	current_number -= 1
	if current_number < 0:
	   current_number = 7

	displayLED(current_number)


def main():

	while True:
	
	      if not 'event' in locals():
		event = GPIO.add_event_detect(18, GPIO.FALLING, callback = lambda x: increase(), bouncetime = 300)

	      if not 'event2' in locals():
		event2 = GPIO.add_event_detect(16, GPIO.FALLING, callback = lambda x: decrease(), bouncetime = 300)

	      else:
		sleep(0.4)



# Only run the functions if
if __name__ == "__main__":

    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")

        # Turn off your GPIOs here
        GPIO.cleanup()

    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)

