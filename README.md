Chat Application with Python Sockets and Threading

This repository contains a basic chat application implemented in Python using sockets and threading. The project consists of two main scripts:

Client Script (client.py):

Asks the user to input their name.
Connects to a server using a specified IP address and port.
Utilizes two threads: one for receiving messages and another for sending messages concurrently.
Handles user disconnection with a ".exit" command.
Server Script (server.py):

Binds to a specified IP address and port, listening for incoming connections.
Accepts client connections, assigns a unique name, and manages a list of connected clients.
Utilizes threading to handle multiple client connections simultaneously.
Handles disconnections and broadcasts messages to all connected clients.
How to Run:

Run the server script (server.py) on a machine.
Run the client script (client.py) on multiple machines or in multiple terminal windows.
Input your name when prompted by the client script.
Start chatting with other connected clients.
Feel free to use and modify this code for your projects. Contributions and improvements are welcome!

Make sure to include any additional information or instructions that users might need, such as dependencies or setup instructions.






