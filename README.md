# Python Chat Application with Sockets and Threading

This project was done by me and another team member Suayeb Ahmed for COMP3825

This repository contains a simple chat application implemented in Python, leveraging sockets and threading to enable real-time communication. The project is divided into two main scripts:

## Client Script (`client.py`):

- Requests the user to input their name.
- Establishes a connection with the server using a specified IP address and port.
- Utilizes two threads—one for receiving messages and another for sending messages concurrently.
- Provides a clean exit mechanism with the ".exit" command.

## Server Script (`server.py`):

- Binds to a specified IP address and port, waiting for incoming connections.
- Accepts client connections, assigns a unique name, and maintains a list of connected clients.
- Employs threading to handle multiple client connections simultaneously.
- Manages disconnections gracefully and broadcasts messages to all connected clients.

## How to Run:

1. Execute the server script (`server.py`) on your machine.
2. Run the client script (`client.py`) on multiple machines or in separate terminal windows.
3. Input your name when prompted by the client script.
4. Start engaging in conversations with other connected clients.

Feel free to use and modify this code for your own projects. Contributions and improvements are always welcome!

## Dependencies:

- Python 3.x

## Getting Started:

1. Clone the repository.
2. Navigate to the project directory.
3. Run the server script:
4. Run the client script on different machines or terminals:


Run the server script (server.py) on a machine.
Run the client script (client.py) on multiple machines or in multiple terminal windows.
Input your name when prompted by the client script.
Start chatting with other connected clients.
Feel free to use and modify this code for your projects. Contributions and improvements are welcome!


Make sure to include any additional information or instructions that users might need, such as dependencies or setup instructions.






