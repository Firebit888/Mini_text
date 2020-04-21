from os import *
from io import *

read = input("write your file: ")
r = ".txt"
y = read + r
write_s = input("write your text: \n")

def save_key():

    new_file = open(y, "w+")
    new_file.write(write_s)
    new_file.close()

def keyread():
    print(read)

save_key()
keyread()
