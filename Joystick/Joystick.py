import RPi.GPIO as gp
import time
from ADCDevice import *

Z_pin=12
adc=ADCDevice()

def setup():
    
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)): # Detect the ads7830
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)
        
    gp.setmode(gp.BOARD)
    gp.setup(Z_pin,gp.IN,gp.PUD_UP)  #setta Z_pin come pull up mode
    

def loop():
    
    while True:
        valZ=gp.input(Z_pin)
        valY=adc.analogRead(0)
        valX=adc.analogRead(1)
        
        print ('value_X: %d ,\tvlue_Y: %d ,\tvalue_Z: %d'%(valX,valY,valZ))
        time.sleep(0.01)
        
def destroy():
    adc.close()
    gp.cleanup()
    
if __name__ == '__main__':
    print ('Program is starting ... ') # Program entrance
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()