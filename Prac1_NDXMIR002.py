Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
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
    global led = 0
    global bit = 0
    global current_number = ""

# Logic that you write
def main():
    print("write your logic here")
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
   
    while True: 
          GPIO.output(8, GPIO.HIGH)
          sleep(1)
          GPIO.output(8, GPIO.LOW)
          sleep(1)
   


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

