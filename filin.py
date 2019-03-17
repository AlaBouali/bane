def clear_file(w):
 with open(w,'w'):
    pass
def delete_file(w):
 s=0
 if os.path.exists(w):
  os.remove(w)
  s+=1
 return s
def write_file(w,fi):
    with open(fi ,"a+") as f:
        f.write(w+'\n')
        return   
def read_file(w):
    with open(w ,"r") as f:
        return f.readlines()
def create_file(w):
    with open(w ,"a+") as f:
     pass   
