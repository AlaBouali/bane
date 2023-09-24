import os, sys


def update_py2(version=None):
    os.system("pip uninstall bane -y")
    if version:
        os.system("pip install bane==" + str(version))
    else:
        os.system("pip install bane")



def update_py3(version=None):
    os.system("pip3 uninstall bane -y")
    if version:
        os.system("pip3 install bane==" + str(version))
    else:
        os.system("pip3 install bane")
        


def update(version=None):
    if sys.version_info < (3, 0):
        update_py2(version=version)
    else:
        update_py3(version=version)
