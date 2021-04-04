import RPi.GPIO as gp
import time
from ADCDevice import *

red=15
green=13
blue=11

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
    
    global  pRed,pGreen,pBlue
    
    gp.setmode(gp.BOARD)
    gp.setup(red,gp.OUT)
    gp.setup(green, gp.OUT)
    gp.setup(blue,gp.OUT)
    
    pRed = gp.PWM(red,1000)    # configure PMW for RGBLED pins, set PWM Frequence to 1kHz
    pRed.start(0)
    pGreen = gp.PWM(green,1000)
    pGreen.start(0)
    pBlue = gp.PWM(blue,1000)
    pBlue.start(0)


def loop():
    
    while True:
        
        valRed=adc.analogRead(0)   # 0 sta ad indicare a0 di ADCDevice
        valBlue=adc.analogRead(2)
        valGreen=adc.analogRead(1)
        
        pRed.ChangeDutyCycle(valRed*100/255)  # map the read value of potentiometers into PWM value and output it 
        pGreen.ChangeDutyCycle(valGreen*100/255)
        pBlue.ChangeDutyCycle(valBlue*100/255)
        # print read ADC value
        print ('ADC Value value_Red: %d ,\tvlue_Green: %d ,\tvalue_Blue: %d'%(valRed,valGreen,valBlue))
        time.sleep(0.01)
        

def destroy():
    adc.close()
    gp.cleanup()
    
if __name__ == '__main__': # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()