
#    Author- Bedabrata Bora
#    Project 1- Simple command line calculator


import re

print("A simple calculator.\n Type 'quit' to exit\n")

previous = 0
run = True


def calculate():
    global previous
    global run

    if previous == 0:
        equation = input("Enter the equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,:{}]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+equation)


while run:
    calculate()







