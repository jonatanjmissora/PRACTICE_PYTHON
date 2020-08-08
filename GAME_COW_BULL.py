import string
import random
import sys

chars_dig = string.digits

def check_input(string):
    for c in string:
        if c not in chars_dig:
            if string == "exit":
                sys.exit("fin") 
            else: 
                return False
        elif int(string) in range(1000,10000):
            return True
        else:
            print("por favor, numero entre 1000 y 9999")
            return False

def hay_cow(guess,num):
    cow = 0
    bull = 0
    for g in guess:
        if g in num:
            if guess.index(g) == num.index(g):
                cow += 1
            else:
                bull += 1
    return [cow, bull]

ran = str(random.randint(1000,10000))
print(ran)
intentos = 0
win = False
while not win:
    text = input("ingreso: ")
    result = [] 
    if check_input(text):
        intentos += 1
        result = hay_cow(text,ran)
        if result[0] == 4:
            win = True
            print("ganó en", intentos, "intentos")
        else:
            print("cow: ", result[0], " bull: ", result[1])
    else:
        print("no es numero")