#Use os module to list file in directory

import os

path = "."
files = os.listdir(path)

for file in files:
    print(file)