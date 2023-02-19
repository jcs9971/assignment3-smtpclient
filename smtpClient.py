from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\nTo Infinity and Beyond"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = 'localhost'
    mailport = 1025

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, mailport))
    recv = clientSocket.recv(1024).decode()

    #print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    helo = 'HELO Alice\r\n'
    clientSocket.send(helo.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '220':
        print('220 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mailFrom = "MAIL FROM: <jcsully@mail.com>\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    if recv2[:3] != '250':
        print('250 reply not received from server.')

    # Send RCPT TO command and handle server response.
    rcptTo = '<alice@mail.com>\r\n'
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    if recv3[:3] != '250':
        print('250 reply not received from server.')


    # Send DATA command and handle server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    if recv4[:3] != '250':
        print('250 reply not received from server.')

    # Send message data.
    #input = raw_input("Enter your message: \r\n")
    #clientSocket.send(input.encode())
    clientSocket.send(msg.encode())
    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv5)
    if recv5[:3] != '250':
        print('250 reply not received from server.')

    # Send QUIT command and handle server response.
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv6)
    if recv6[:3] != '250':
        print('250 reply not received from server.')
    clientsocket.Close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
