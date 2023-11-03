from .utils import *



class Botnet_Reporting_Server:

    def get_server(self):
        return self.server

    def __init__(self,host='0.0.0.0',port=11111,debug=True):
        self.host=host
        self.port=port
        self.debug=debug
        self.server=flask.Flask(__name__)
    
    def run(self):
        self.server.run(host=self.host,port=self.port,debug=self.debug)
    
    def set_route(self,*args,**kwargs):
        self.server.add_url_rule(*args,**kwargs)