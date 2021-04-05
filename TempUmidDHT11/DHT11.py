import RPi.GPIO as gp
import time

import Freenove_DHT as DHT

dhtPin=11

def loop():
    
    dht=DHT.DHT(dhtPin)
    
    counts=0
    
    while True:
        
        counts+=1
        
        print('Numero misurazione', counts)
        
        for i in range(0,15):
            
            chk=dht.readDHT11()
            
            if(chk is dht.DHTLIB_OK):
                print('DHT11_OK')
                break
            time.sleep(0.1)
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))
        time.sleep(2)  
 
 
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        gp.cleanup()
        exit()  