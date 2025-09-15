#Imports
import socket

#Variables
bufferSize = 1024
msgFromServer = "Greetings Client, Happy to be your Server"
ServerPort = 2222
ServerIP = '192.168.0.50'

#Setup
bytesToSend = msgFromServer.encode('utf-8')
RPIsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIsocket.bind((ServerIP, ServerPort))
print('Server is Up and Listening...')

#Receiving
message, address = RPIsocket.recvfrom(bufferSize)
message = message.decode('utf-8')
print(message)
print('Client Address:', address[0])

#Responding
RPIsocket.sendto(bytesToSend, address)
