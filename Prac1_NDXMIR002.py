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
"""
global int LED_0 = 7;             # LSB pin 
global int LED_1 = 11;
global int LED_2 = 15;	     # MSB pin 	

global int button_increase=16                     # BUTTON PIN CONFIGURATIONS
global int button_decrease=18
"""
L0 = None                # bit displayed 
L1 = None                # bit displayed
L2 = None                # bit displayed
binary = None            # shows the integer number displayed on LED 

# Pin set-up
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)                                         # setup pins using board config

GPIO.setup(7, GPIO.OUT)                    # sets initial condition to output low
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
"""
GPIO.setup(button_increase, GPIO.IN, pull_up_down = GPIO.PUD_UP)  # setup button using pull-up resistor
GPIO.setup(button_decrease, GPIO.IN, pull_up_down = GPIO.PUD_UP)  # setup button using pull-up resistor
"""

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


def main():
	for current_number in range(0, 8): 
 	      
             displayLED(current_number);
	     sleep(2);



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

