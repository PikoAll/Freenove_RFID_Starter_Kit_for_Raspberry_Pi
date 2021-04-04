import RPi.GPIO as GPIO
import time

ledPins=[11,12,13,15,16,18,22,3,5,24]

def setup():
    time.sleep(5)
    print('1')
    GPIO.setmode(GPIO.BOARD)      #usa la numerazione gpio fisica
    time.sleep(5)
    print('2')
    GPIO.setup(ledPins,GPIO.OUT)  #imposta tutti i led in modalta output
    time.sleep(5)
    print('3')
    GPIO.output(ledPins,GPIO.HIGH) #spegne tutti i led
    time.sleep(5)
    print('4')
    
def loop():
    
    while True:
        
        for pin in ledPins:     #fa muovere i led acceso da sinistra a destra
            GPIO.output(pin,  GPIO.LOW)   #accende pin
            time.sleep(0.1)
            GPIO.output(pin,GPIO.HIGH)  #spegne pin
        
        for pin in ledPins[::-1]:  #fa muovere i led da sinistra a destra
            
            GPIO.output(pin,  GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(pin,GPIO.HIGH)
            

def destropy():
    GPIO.cleanup()    #rilascia tutti i gpio
    
    
if __name__=='__main__':
    
    print('start')
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:  #premere control c per terminare il programma
        destropy()
            
    
