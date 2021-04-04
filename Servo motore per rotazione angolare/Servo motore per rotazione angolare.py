import RPi.GPIO as gp

import time

OFFSE_DUTY=0.5 #impulso da dare a servo

SERVO_MIN_DUTY= 2.5+OFFSE_DUTY
SERVO_MAX_DUTY=12.5+OFFSE_DUTY

servoPin=12

def map(value,fromLow,fromHight, toLow, toHigh):
    
    return (toHigh-toLow)*(value-fromLow)/(fromHight-fromLow)+toLow


def setup():
    
    global p
    
    gp.setmode(gp.BOARD)
    gp.setup(servoPin, gp.OUT)
    gp.output(servoPin,gp.LOW)
    
    p=gp.PWM(servoPin, 50)
    p.start(0)
    
def servoWrite(angle):
    
    if (angle<0):
        angle=0
    elif angle>180:
        angle=180
    p.ChangeDutyCycle(map(angle,0,180,SERVO_MIN_DUTY,SERVO_MAX_DUTY))  #mappa l'angolo


def loop():
    
    while True:
        for dc in range(0,181,1):  #rotazione da 0 a 180
            servoWrite(dc)
            time.sleep(0.001)
        time.sleep(0.5)
        
        for dc in range(180,-1,-1):  #rotazione da 180 a 0
            servoWrite(dc)
            time.sleep(0.001)
        time.sleep(0.5)




def destroy():
    p.stop()
    gp.cleanup()

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

