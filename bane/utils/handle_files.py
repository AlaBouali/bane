import os,json

class Files_Interface:

    @staticmethod
    def clear_file(w):
        with open(w, "w") as f:
            pass
        f.close()



    @staticmethod
    def delete_file(w):
        if os.path.exists(w):
            os.remove(w)


    @staticmethod
    def write_file(w, fi, encode="utf-8"):
        with open(fi, "a+", encoding=encode) as f:
            f.write(w + "\n")
        f.close()


    @staticmethod
    def read_file(w,split_lines=True,remove_empty_lines=True):
        with open(w, "r") as f:
            l = f.read()
        f.close()
        l=l.split('\n')
        if remove_empty_lines==True:
            l='\n'.join([x for x in l if x.strip()!=''])
        if split_lines==True:
            return l.split('\n')
        return l

    @staticmethod
    def create_file(w):
        direc, file = os.path.split(w)
        try:
            if not os.path.exists(direc):
                os.makedirs(direc)
        except:
            pass
        with open(w, "w") as f:
            pass
        f.close()


    @staticmethod
    def write_to_json(data,file_name,indent=4,**kwargs):
        with open(file_name, "w") as json_file:
            json.dump(data, json_file,indent=indent,**kwargs)
            json_file.close()
    

    @staticmethod
    def read_from_json(file_name,**kwargs):
        with open(file_name, "r") as json_file:
            data = json.load(json_file,**kwargs)
            json_file.close()
        return data