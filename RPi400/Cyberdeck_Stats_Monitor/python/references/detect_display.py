# coding=utf-8
 
import RPi.GPIO as GPIO
import time
    
# main...
def main():
    try:
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)  # Use board numbering of pins instead of BCM, which changes between Pi1 Model B
        
        #GPIO.setup(17,GPIO.IN)
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        # for x in "12345":
        # print(GPIO.input(17)) # prints five "0"s if the display is plugged in, otherwise prints five "1"s
        if GPIO.input(17) == GPIO.HIGH:
            # display is not plugged in
            print("display not plugged in")
        else:
            # display is plugged in
            print("display is plugged in")
        # time.sleep(1) 
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
