import RPi.GPIO as gp
import time

# Definisce il bit di dati che viene trasmesso preferenzialmente nella funzione shiftOut.
LSBFIRST  =  1
MSBFIRST  =  2

# definire i pin per 74HC595
dataPin    =  11       # DS Pin di 74HC595 (Pin14)
latchPin   =  13       # ST_CP Pin di 74HC595 (Pin12)
clockPin  =  15        # CH_CP Pin di 74HC595 (Pin11)


def setup():
    
    gp.setmode(gp.BOARD)
    gp.setup(dataPin, gp.OUT) # set pin to OUTPUT mode
    gp.setup(latchPin, gp.OUT)
    gp.setup(clockPin, gp.OUT)
    
    

# funzione shiftOut, usa la trasmissione seriale di bit.
def shiftOut(dPin,cPin,order,val):
    
    for i in range(0,8):
        gp.output(cPin,gp.LOW)
        
        if(order == LSBFIRST):
            gp.output(dPin,(0x01&(val>>i)==0x01) and gp.HIGH or gp.LOW)
        elif(order == MSBFIRST):
            gp.output(dPin,(0x80&(val<<i)==0x80) and gp.HIGH or gp.LOW)
        gp.output(cPin,gp.HIGH);
        
def loop():
    
    while True:
        
        x=0x01
        for i in range(0,8):
            
            gp.output(latchPin,gp.LOW)
            shiftOut(dataPin,clockPin,LSBFIRST,x)
            gp.output(latchPin,gp.HIGH)
            x<<=1
            time.sleep(0.1)
        
        x=0x80
        for i in range(0,8):
            
            gp.output(latchPin,gp.LOW)
            shiftOut(dataPin,clockPin,LSBFIRST,x)
            gp.output(latchPin,gp.HIGH)
            
            x>>=1
            time.sleep(0.1)

def destroy():   
    gp.cleanup()

if __name__ == '__main__': # Program entrance
    print ('Program is starting...' )
    setup() 
    try:
        loop()  
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()  
            
            
