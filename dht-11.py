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
    print('Client Address: ', address[0])
    if cmd == 'GO':
        result = myDHT.read()
        if result.is_valid():
            data = str(result.temperature) + ':' + str(result.humidity)
            data = data.encode('utf-8')
            RPIsocket.sendto(data, address)
        else:
            data = 'Bad Measurement'
            print(data)
            data = data.encode('utf-8')
            RPIsocket.sendto(data, address)
    else:
        data = 'Invalid Request'
        data = data.encode('utf-8')
        RPIsocket.sendto(data, address)
