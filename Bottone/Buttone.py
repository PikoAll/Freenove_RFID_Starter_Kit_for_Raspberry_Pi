from gpiozero import Button

button=Button(4)

button.wait_for_press()  #il codice resta bloccato qua finquando non viene premuto il bottore
print('mi haipremuto')