import threading
import socket
from connection import recv_by_size
from connection import send_by_size 
class server:
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((ip,port))
        self.s.listen(6)
        print("server started")




    def recieve(self,serv_cleint):  
        

        length_bytes = serv_cleint.recv(4)
        message_length = int.from_bytes(length_bytes, byteorder='big')
        recieved=0
        msg=b'' 
        while recieved < message_length:
            msg+=serv_cleint.recv(1024)
            recieved+=1024

    def foo(self):
        return "boo hoo nigga "
    
    def foo2(self): 
        print( self.foo())
    def parse_reply(self,msg):    
        return input("enter you reply ")  
        #this function will receive will protocol command was sent and parse a reply acordinglly


    def handle_client(self,serv_cleint):

        while True:
          
            msg=recv_by_size(serv_cleint,"bytes")   
            #print("recvied msg")
            print(msg)
           
            reply=self.parse_reply(msg)
            print(reply)
            #after implementing this function 
            send_by_size(serv_cleint,reply)
            if b"quit" in msg:
                print ("this clie niggernt has finished his business")  
                serv_cleint.close()
                break  
            else :
                continue
            


    def accept_cleints(self):
        threads=[]
        tid=0   
        while True:
            try:
                self.serv_cleint,self.addr=self.s.accept()  
                thread=threading.Thread(target=self.handle_client,args=[self.serv_cleint]) 
                thread.start()
                threads.append(thread)
                print("new client")
                tid += 1       
            except socket.error as err:
                print('socket error', err)
                break
                exit_all = True
                for t in threads:
                    t.join()


#server=server('0.0.0.0', 1234)    
#server.accept_cleints()
# create user server with a dictionary of every online user , the socket it has .
# in the send function the message will give u a username then server will enter it dictionary and send to the socket in the value 
# server will then send to that socket the forwared message aditionally it will ad it to the logs db.