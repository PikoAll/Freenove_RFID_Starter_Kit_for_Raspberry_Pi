from gpiozero import LED, Button

led=LED(20)

button=Button(4)

while True:
    
    button.wait_for_press()
    led.on()
    
    button.wait_for_press()
    led.off()
    