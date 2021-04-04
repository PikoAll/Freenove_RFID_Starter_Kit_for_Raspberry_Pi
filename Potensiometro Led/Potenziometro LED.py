import time

import RPi.GPIO as gp


from ADCDevice import *

ledPin=11

adc = ADCDevice() # Define an ADCDevice class object

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
        
    
    global p
    
    gp.setmode(gp.BOARD)
    gp.setup(ledPin, gp.OUT)
    p=gp.PWM(ledPin,1000)
    p.start(0)
    
        
def loop():
    
    while True:
        
        value=adc.analogRead(0)  #leggi il valore dalcanale 0
        p.ChangeDutyCycle(value*100/255)
        voltage=value/ 255.0*3.3  #calcola il valore di tensione
        
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        time.sleep(0.03)
        


def destroy():
    adc.close()
    gp.cleanup()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()
def destroy():
    adc.close()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()
