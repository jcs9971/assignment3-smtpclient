from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    #mailserver = 'localhost'
    #mailport = 1025

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver, port)
    recv = clientSocket.recv(1024)
    # print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    helo = 'HELO Alice\r\n'
    clientSocket.send(helo.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)
    if recv1[:3] != '220':
        print('220 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mailFrom = "MAIL FROM:<jcsully@mail.com> \r\n"
    clientSocket.send(mailFrom.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send RCPT TO command and handle server response.
    rcptTo = 'RCPT TO:<alice@mail.com> \r\n'
    clientSocket.send(rcptTo.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send DATA command and handle server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)
    if recv1[:3] != '354':
        print('354 reply not received from server.')

    # Send message data.
    clientSocket.send(msg.encode())
    # print(recv1)

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send QUIT command and handle server response.
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv1 = clientSocket.recv(1024)
    # print(recv1)
    if recv1[:3] != '221':
        print('221 reply not received from server.')
    clientsocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
