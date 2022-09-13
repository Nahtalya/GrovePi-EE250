"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():

    TCP_IP = '20.171.56.97'
    TCP_Port= 8080
    buffer=1024
    message = "hello"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((TCP_IP, TCP_Port))
        s.send(message)
        data = s.recv(buffer)
    
    print(f"recieved",data)
    # TODO: Create a socket and connect it to the server at the designated IP and port
    
    # TODO: Get user input and send it to the server using your TCP socket
    
    # TODO: Receive a response from the server and close the TCP connection
    
    s.close

if __name__ == '__main__':
    main()
