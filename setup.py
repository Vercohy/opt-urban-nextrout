#!usr/bin/env python3

import os

print("<< Installing Nextrout >>")

os.chdir("./code/")  # && os.mkdir("Nextrout") && os.chdir("./Nextrout/")
os.system("git clone https://github.com/Danielaleite/Nextrout")
os.chdir("./Nextrout/")
os.system("python setup.py")

print("<<Installation finished>>")
