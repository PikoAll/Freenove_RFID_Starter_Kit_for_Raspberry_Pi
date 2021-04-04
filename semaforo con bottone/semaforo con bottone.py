from gpiozero import LED,Button
from time import sleep

button=Button(17)

ledR=LED(27)
ledG=LED(22)
ledV=LED(5)

def controllo(fl):
    if(fl==True):
        return 2
    return 5

#print(button.wait_for_press())
x=False
while True:
    
  
    if x==True:
        y=2
    else:
        y=5
    ledR.on()
    sleep(y)
    
    
    
    ledR.off()
    ledG.on()
    sleep(y)
    
    ledG.off()
    ledV.on()
    x=False
    while sleep(y):
        print('hola')
        x=button.wait_for_press()
        print('ciao')
    
    ledV.off()

