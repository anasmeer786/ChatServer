#Anas Zaheer

import threading
import socket
import sys

host = '127.0.0.1'
port = 8888
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
names = []

def broadcast(message):
    for client in clients:
        client.send(message.decode('utf-8').encode('utf-8'))
        
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f'Client: {client} and Client List: {clients}')
            if ".exit" in str(message):
                index = clients.index(client)
                clients.remove(client)
                client.close()
                name = names[index]
                decoded_message = message.decode('utf-8')
                broadcast(f'{name} left the chat room! {decoded_message}'.encode('utf-8'))
                names.remove(name)
                break
            else:
                broadcast(message)
        except:
            
            print(f'Error Occurred! {sys.exc_info()[0]}')
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast(f'{name} left the chat room!'.encode('utf-8'))
            names.remove(name)
            break
        
def main():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'Connected with {str(address)}')
        client.send('name?'.encode('utf-8'))
        name = client.recv(1024)
        names.append(name)
        clients.append(client)
        client_name = name.decode('utf-8')
        output = f'The name of the client is {client_name}'.encode('utf-8')
        
        print(output.decode('utf-8'))
        broadcast(f'{client_name} joined the chat room!'.encode('utf-8'))
        client.send('You are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
if __name__ == "__main__":
    main()
