import RPi.GPIO as gp

import time
import random

pins=[11,12,13]


def setup():
    global red,green,blue
    
    gp.setmode(gp.BOARD)  #indichiamo che tilizziamo la board
    gp.setup(pins,gp.OUT)  #settagio sullamodlita output
    gp.output(pins,gp.HIGH) #accende i pin
    
    red=gp.PWM(pins[0],2000)  #imposta la frequenza a 2kHz
    blue=gp.PWM(pins[1],2000)
    green=gp.PWM(pins[2],2000)
    
    red.start(0)  #inizializza a 0
    blue.start(0)
    green.start(0)
    
    
def setColor(r,g,b):       #setta tonazione di colore
    red.ChangeDutyCycle(r)
    green.ChangeDutyCycle(g)
    blue.ChangeDutyCycle(b)
    
    
def loop():
    
    while True:
        r=random.randint(0,100)
        g=random.randint(0,100)
        b=random.randint(0,100)
        
        setColor(r,g,b)
        print ('r=%d, g=%d, b=%d ' %(r ,g, b))
        time.sleep(1)
        
    
def destroy():
    red.stop()
    green.stop()
    blue.stop()
    gp.cleanup()
    

if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
    