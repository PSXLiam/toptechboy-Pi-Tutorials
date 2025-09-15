#Imports
import socket
from time import sleep

#Variables
bufferSize = 1024
msgFromServer = "Greetings Client, Happy to be your Server"
ServerPort = 2222
ServerIP = '192.168.0.50'
count = 0

#Setup
bytesToSend = msgFromServer.encode('utf-8')
RPIsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIsocket.bind((ServerIP, ServerPort))
print('Server is Up and Listening...')

#Receiving
while True:
    message, address = RPIsocket.recvfrom(bufferSize)
    message = message.decode('utf-8')
    print(message)
    print('Client Address:', address[0])
    if message == 'INC':
        count = count + 1
    if message == 'DEC':
        count = count - 1
    msg = str(count)
    msg = msg.encode('utf-8')

#Responding
    RPIsocket.sendto(msg, address)
