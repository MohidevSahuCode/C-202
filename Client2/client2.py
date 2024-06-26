import socket
from threading import Thread

nickname = input("Please choose your nickname : ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 8000

client.connect((ip_address,port))
print("Welcome Welcome \n\n\n")

def recive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == "NICKNAME":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occur !\n!\n!")
            break
def write():
    while True:
        message = '{} : {}'.format(nickname,input(''))
        client.send(message.encode('utf-8'))

recive_thread = Thread(target = recive)
recive_thread.start()
write_thread = Thread(target = write)
write_thread.start()