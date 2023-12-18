#Anas Zaheer

import threading 
import socket

name = input('Enter Your Name: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'name?':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            client_name = str(name)
            print(f'{client_name} has left the room!')
            client.close()
            break

        
def send():
    while True:
        message = f'{name}: {input("")}'
        
        if ".exit" in str(message):
            client.send(message.encode('utf-8'))
            break
        else:
            client.send(message.encode('utf-8'))

    client.close()
    
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
