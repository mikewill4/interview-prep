# Client-Server model
## Client
* Sometimes on
* Typically the human end user
* Connects to the server and makes some sort of request
* Receives a response
### Typical client program
* Prepare to communicate
	* Create a socket
	* Determine server address and port number
	* Initiate connection to server
* Exchange data with the server
	* Write data to socket
	* Read data from socket
	* Do stuff with data
* Close the socket
## Server
* Always on
* Fixed, well-known address
* Passive open
	* Prepare to accept connection
	* Don't establish connection until heard from client
* Multiple clients
	* Allow backlog of waiting clients
	* Create a new socket for each client 
## Typical server program
* Prepare to communicate
	* Create socket
	* Associate local address and port with socket
* Wait to hear from client (passive open)
	* Indicate how many clients waiting
	* Accept incoming connection from client
* Exchange data with client over new socket
	* Receive data from socket
	* Handle request
	* Send data to socket
	* Close socket
* Repeat for each connection
