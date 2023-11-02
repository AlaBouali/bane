import socket,os,sys,pwinput

if sys.version_info < (3, 0):
    user_input=raw_input
else:
    user_input=input


class Botnet_Master:

    @staticmethod
    def send_data(data,sock,timeout=2,real_timeout=3):
        sock.send('{}\n'.format(data).encode())
        return Botnet_Master.read_data(sock,timeout=2,real_timeout=3)

    
    def login(self,host,port,username,password,timeout=3,read_timeout=2):
        self.sock=socket.socket()
        self.sock.settimeout(timeout)
        self.sock.connect((host,port))
        Botnet_Master.read_data(self.sock,timeout=read_timeout,real_timeout=timeout)
        self.sock.send('{}\n'.format(username).encode())
        Botnet_Master.read_data(self.sock,timeout=read_timeout,real_timeout=timeout)
        self.sock.send('{}\n'.format(password).encode())
        self.data=Botnet_Master.read_data(self.sock,timeout=read_timeout,real_timeout=timeout)
        if 'failed' in self.data:
            raise Exception('Login failed')

    def execute(self,cmd,timeout=2,real_timeout=3):
        return Botnet_Master.send_data(cmd,self.sock,timeout=2,real_timeout=3)
    
    def close(self):
        self.sock.close()
        self.sock=None

    @staticmethod
    def read_data(sock,timeout=2,real_timeout=3):
        data=''
        sock.settimeout(timeout)
        while True:
            try:
                d=sock.recv(1024).decode()
                if d=='':
                    break
                data+=d
            except Exception as ex:
                break
        sock.settimeout(real_timeout)
        return data

    @staticmethod
    def interact(host,port,read_timeout=3,timeout=3):
        s=socket.socket()
        s.settimeout(timeout)
        s.connect((host,port))
        data=Botnet_Master.read_data(s,timeout=read_timeout,real_timeout=timeout)
        username=user_input(data)
        s.send('{}\n'.format(username).encode())
        data=Botnet_Master.read_data(s,timeout=read_timeout,real_timeout=timeout)
        password=pwinput.pwinput(prompt=data, mask='*')
        s.send('{}\n'.format(password).encode())
        while True:
            data=Botnet_Master.read_data(s,timeout=read_timeout,real_timeout=timeout)
            cmd=user_input(data)
            s.send('{}\n'.format(cmd).encode())