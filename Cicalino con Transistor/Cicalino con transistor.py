import RPi.GPIO as gp

buzzerPin=11

buttonPin=12

def setup():
    gp.setmode(gp.BOARD)
    gp.setup(buzzerPin,gp.OUT) #cicalino fa solo rumore quin e ouput
    gp.setup(buttonPin,gp.IN, pull_up_down=gp.PUD_UP)  #modalita pull up input
    
    
def loop():
    while True:
        
        if(gp.input(buttonPin)==gp.LOW): #se si preme il pulsante attiva cicalino
            gp.output(buzzerPin,gp.HIGH)
            print('cicalino attivo')
        else:
            gp.output(buzzerPin, gp.LOW)
            print('cicalino spento')



def destroy():
    GPIO.cleanup()                     # Release all GPIO

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

