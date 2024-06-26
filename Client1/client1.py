import socket
from threading import Thread
from tkinter import *


#nickname = input("Please choose your nickname : ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 8000

client.connect((ip_address,port))
print("Welcome Welcome \n\n\n")

class GUI():
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")

        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)

        self.pls = Label(self.login,
                         text="Please Login to continue",
                         justify="center",
                         font="Helvetica 14 bold")
        self.pls.place(relheight=0.15,
                       relx=0.35,
                       rely=0.07)
        self.labelName = Label(self.login,
                               text="Name : ",
                               font="Helvetica 12")
        self.labelName.place(relheight=0.2,
                             relx=0.1,
                             rely=0.13)
        self.entryName = Entry(self.login,
                               font="Helvetica 14")
        self.entryName.place(relheight=0.12,
                             relx=0.35,
                             rely=0.2)
        self.entryName.focus()

        self.go = Button(self.login,text="Continue",
                         font="Helvetica 14 bold",
                         command=lambda:self.goAhead(self.entryName.get()))
        self.go.place(relx=0.4,
                      rely=0.55)
        
        self.Window.mainloop()

    def goAhead(self,name):
        self.login.destroy()
        self.name = name
        rcv = Thread(target=self.recive)
        rcv.start()

    def recive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == "NICKNAME":
                    client.send(self.name.encode('utf-8'))
                else:
                    print(message)
            except:
                print("An error occur !\n!\n!")
                break

g = GUI()

# def write():
#     while True:
#         message = '{} : {}'.format(nickname,input(''))
#         client.send(message.encode('utf-8'))

# recive_thread = Thread(target = recive)
# recive_thread.start()
# write_thread = Thread(target = write)
# write_thread.start()