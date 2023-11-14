from .utils import *
from ..cryptographers._base64 import BASE64

class JWT_Manager:

    @staticmethod
    def analyze_token(token):
        parts=token.split('.')
        algorith=json.loads(BASE64.decode(parts[0]))["alg"]
        seg=parts[2]
        try:
            data=json.loads(BASE64.decode(parts[1].encode()))
        except Exception as ex :
            try:
                data=json.loads(BASE64.decode(parts[1]+'=='))
            except:
                data=parts[1]
        return {'algorithm':algorith,'data':data,'signature':seg}


    @staticmethod
    def encode(data,secret_key,algorithm="HS256"):
        return jwt.encode(data,secret_key,algorithm=algorithm)


    @staticmethod
    def decode(data,secret_key):
        algorithm=JWT_Manager.analyze_token(data)['algorithm']
        return jwt.decode(data, secret_key, algorithms=algorithm)


    @staticmethod
    def guess_secret_key(word_list,token):
        word_list=Userful_Utilities.load_word_list(word_list)
        started_at=time.time()
        d=JWT_Manager.analyze_token(token)
        algo=d['algorithm']
        data=d['data']
        for x in word_list:
            if JWT_Manager.encode(data,x,algorithm=algo)==token:
                {'input':token,'start_date':started_at,'end_date':time.time(),'secret_key':x}