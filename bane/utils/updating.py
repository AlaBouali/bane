import os, sys


class Update_Module_Interface:

    @staticmethod
    def update_py2(version=None):
        os.system("pip uninstall bane -y")
        if version:
            os.system("pip install bane==" + str(version))
        else:
            os.system("pip install bane")



    @staticmethod
    def update_py3(version=None):
        os.system("pip3 uninstall bane -y")
        if version:
            os.system("pip3 install bane==" + str(version))
        else:
            os.system("pip3 install bane")
            


    @staticmethod
    def update(version=None):
        if sys.version_info < (3, 0):
            Update_Module_Interface.update_py2(version=version)
        else:
            Update_Module_Interface.update_py3(version=version)
