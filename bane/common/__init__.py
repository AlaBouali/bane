from .payloads import *
import sys

running_on_python_2=True

if sys.version_info < (3, 0):
        pass
else:
    running_on_python_2=False
