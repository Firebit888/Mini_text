from os import *
from io import *
from colored import *

green = fg('green')
magenta = fg('magenta')
red = fg('red')
blue = fg('blue')
white = fg('white')


read = input(green + "write your file: ")
r = ".txt"
y = read + r
write_s = input(magenta + "write your text: \n" + white +  "1º - ")
write_t = input(white + "2º - ")
write_u = input(white + "3º - ")
write_p = input(white + "4º - ")
write_q = input(white + "5º - ")
write_f = input(white + "6º - ")
write_v = input(white + "finish - ")



def save_key():
    green = fg('green')
    magenta = fg('magenta')
    red = fg('red')
    blue = fg('blue')
    new_file = open(y, "w+")
    new_file.write(write_s + '\n')
    new_file.write(write_t + '\n')
    new_file.write(write_u + '\n')
    new_file.write(write_p + '\n')
    new_file.write(write_q + '\n')
    new_file.write(write_f + '\n')
    new_file.write(write_v + '\n')
    print(red + "Can´t write more! \n")
    print(green + "Thanks for use this program. \n")
    new_file.close()

def keyread():
    green = fg('green')
    magenta = fg('magenta')
    red = fg('red')
    blue = fg('blue')
    print(blue + "The name you file is " + read + ".txt")


save_key()
keyread()
input(white + "Press a keyword to close")
