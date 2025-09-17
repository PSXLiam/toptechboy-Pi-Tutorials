#Imports
import socket
import RPi.GPIO as GPIO
import dht11

#Variables
bufferSize = 1024
ServerPort = 2222
ServerIP = '192.168.0.50'

#Setup
GPIO.setmode(GPIO.BCM)
myDHT = dht11.DHT11(pin = 17)
RPIsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIsocket.bind((ServerIP, ServerPort))
print('Server is Up and Listening...')

while True:
    cmd, address = RPIsocket.recvfrom(bufferSize)
    cmd = cmd.decode('utf-8')
    print(cmd)
    if cmd == 'TEMP':
        result = myDHT.read()
        while result.is_valid() == False:
            print('Bad Read... Try Again')
            result = myDHT.read()
        data = cmd + ':' + str(result.temperature)
        data = data.encode('utf-8')
        RPIsocket.sendto(data, address)
    if cmd == 'HUM':
        result = myDHT.read()
        while result.is_valid() == False:
            print('Bad Read... Try Again')
            result = myDHT.read()
        data = cmd + ':' + str(result.humidity)
        data = data.encode('utf-8')
        RPIsocket.sendto(data, address)
    if cmd != 'TEMP' and cmd != 'HUM':
        data = cmd + ':' + 'null'
        data = data.encode('utf-8')
        RPIsocket.sendto(data, address)
