# Sockets
* End point of communication
* Message must traverse underlying network
* Messages can go in and out of sockets
## Ports
* Destination port uniquely identifies a socket to use
* 16-bit quantity
* Common ports:
	* 21 (ftp)
	* 21 (ssh)
	* 25 (email)
	* 80 (http)
	* 443 (https)
* Well known ports are between 0-1023
* Unused ephemeral (temporary) ports are between 20124-65535
## Creating a socket
* int socket(int domain, int type, int protocol)
* Domain: protocol family
* Type: semantics of communication
	* SOCK_STREAM: reliable byte stream
	* SOCK_DGRAM: message-oriented service
* Protocol: specific protocol
	* UNSPEC: unspecified
	* SOCK_STREAM implies TCP for example
## Connecting socket to server
* Translate hostname to IP address
* Identify service's port number using service name and protocol
* Establish connection
## Server preparing a socket
* int bind(int sockfd, struct sockaddr, *my_addr, socklen_t addrlen)
* Bind socket to local address and port number
* Define how many connections can be pending
* int list(int sockfd, int backlog)
* Accept new client connection
* int accept(int sockfd, struct sockaddr *addr, socketlen_t *addrlen)
