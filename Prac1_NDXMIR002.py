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
global LED_0 = 7             # LED PIN CONFIGURATIONS
global LED_1 = 11
global LED_2 = 15

global button_increase = 16                     # BUTTON PIN CONFIGURATIONS
global button_decrease = 18

global led_on = 0             # decimal number
global bit = 0                # bit displayed
global current_number = ""    # binary 

# Pin Configurations
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)                                         # setup pins using board config

GPIO.setup(LED_0, GPIO.OUT, initial=GPIO.LOW)                    # sets initial condition to output low
GPIO.setup(LED_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_2, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(button_increase, GPIO.IN, pull_up_down = GPIO.PUD_UP)  # setup button using pull-up resistor
GPIO.setup(button_decrease, GPIO.IN, pull_up_down = GPIO.PUD_UP)  # setup button using pull-up resistor

# Logic that you write
def add_bit():
    while GPIO.input(button_increase) == GPIO.LOW:
          sleep(0.01) 



def minus_bit():
    while GPIO.input(button_decrease) == GPIO.HIGH



def counter():


def main():
   
    while True: 

	if add_bit(): 
"""
          GPIO.output(LED_0, GPIO.HIGH)
          sleep(1)
          GPIO.output(LED_0, GPIO.LOW)
          sleep(1)
"""
          if GPIO.input(button_increase):
              return False
          else:
  	      return True 

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
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)

