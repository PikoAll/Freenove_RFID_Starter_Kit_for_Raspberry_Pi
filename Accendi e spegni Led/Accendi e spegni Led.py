from gpiozero import LED
from time import sleep

#gamba corda e collegata a  GND gamba lunga e collegata a resistenza e la restistenz a GP25
led=LED(25) #perche e collegata a GP 25 ho messo il numero 25

#led.on()  #per accendere
#led.off()  #per spegnere

while True:
    
    led.on()
    sleep(1)
    led.off()
    sleep(1)



