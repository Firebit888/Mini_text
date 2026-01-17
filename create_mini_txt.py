from colored import fg

green = fg('green')
magenta = fg('magenta')
red = fg('red')
blue = fg('blue')
white = fg('white')

# Nome do ficheiro
filename = input(green + "Write your file name: ") + ".txt"

print(magenta + "Write your text (type ':exit' to finish)\n")

with open(filename, "w", encoding="utf-8") as file:
    line_number = 1

    while True:
        text = input(white + f"{line_number}º - ")

        if text.lower() == ":exit":
            print(red + "\nCan't write more!")
            break

        file.write(text + "\n")
        line_number += 1

print(green + "Thanks for using this program.")
input(white + "Press ENTER to close")
