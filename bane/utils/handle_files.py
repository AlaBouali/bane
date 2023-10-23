import os

def clear_file(w):
    with open(w, "w") as f:
        pass
    f.close()



def delete_file(w):
    if os.path.exists(w):
        os.remove(w)


def write_file(w, fi, encode="utf-8"):
    with open(fi, "a+", encoding=encode) as f:
        f.write(w + "\n")
    f.close()


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

