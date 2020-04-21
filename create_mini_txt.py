from os import *
from io import *

read = input("write your file: ")
r = ".txt"
y = read + r
write_s = input("write your text: \n")
write_t = input()
write_u = input()
write_p = input()
write_q = input()
write_f = input()
write_v = input()



def save_key():
    new_file = open(y, "w+")
    new_file.write(write_s + '\n')
    new_file.write(write_t + '\n')
    new_file.write(write_u + '\n')
    new_file.write(write_p + '\n')
    new_file.write(write_q + '\n')
    new_file.write(write_f + '\n')
    new_file.write(write_v + '\n')
    print("Can´t write more! \n")
    print("Thanks for use this program. \n")
    new_file.close()

def keyread():
    print("The name you file is " + read + ".txt")


save_key()
keyread()
input("Press a keyword to close")
