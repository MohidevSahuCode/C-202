#setup connection of client and server & socket = ip+ports
import socket
#Help for multitasking / Thread = flow of execution
from threading import Thread

#AF_INET = ip v4 address , SOCK_STREAM = TCB protocol
server=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

ip_address = '127.0.0.1'
#protocol according to our serves
port = 8000

server.bind((ip_address,port))
server.listen()

list_of_clients = []
nicknames = []
print("Server has started ...... :>")

def clientthread(conn , nickname):
    conn.send("Welcome to this chatroom".encode('utf-8'))
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                print(message)
                boardcast(message,conn)
            else:
                remove(conn)
                remove_nickname(nickname)
        except:
            continue

def boardcast(message,connecion):
    for clients in list_of_clients:
        if clients!=connecion:
            try:
                clients.sent(message.encode('utf-8'))
            except:
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
    
def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)

while True:
    conn,addr = server.accept()
    conn.send("NICKNAME".encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    list_of_clients.append(conn)
    nicknames.append(nickname)
    message = "{} Joiend \n\n".format(nickname)
    print(message)
    boardcast(message,conn)
    new_thread = Thread(target = clientthread,args=(conn,addr))
    new_thread.start()