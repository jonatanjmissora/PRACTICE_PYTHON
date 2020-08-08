"""# lista nueva con impares, compacto
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if x % 2 != 0]
print(b)

# generar una lista aleatoria
import random
numlist = []
list_length = random.randint(5,15)
while len(numlist) < list_length:
    numlist.append(random.randint(1,75))
print(numlist)

# piedra papel o tijera
import random
print("roca, papel o tijera, o fin:")
while True:
    options = ["roca", "papel", "tijera"]
    p1 = random.choice(options)
    p2 = random.choice(options)
    #p1 = input("player1: ")
    #p2 = input("player2: ")
    if p1 == "fin" or p2 == "fin":
        print("terminado")
        break
    else:
        if p1 == p2:
            print("empate")
        elif p1 == "roca":
            if p2 == "papel":
                print("gana player2")
            else: print("gana player1")
        elif p1 == "papel":
            if p2 == "tijera":
                print("gana player2")
            else: print("gana player1")
        elif p1 == "tijera":
            if p2 == "roca":
                print("gana player2")
            else: print("gana player1")

#otro
def rockPaperSci(p1, opt1, p2, opt2):
    if options.index(opt1) - options.index(opt2) == 1:
        print('\n' + p1 + ' wins')

    elif options.index(opt1) - options.index(opt2) == -1:
        print('\n' + p2 + ' wins')

    elif options.index(opt1) - options.index(opt2) == -2:
        print('\n' + p1 + ' wins')

    elif options.index(opt1) - options.index(opt2) == 2:
        print('\n' + p2 + ' wins')
    else:
        print('\nTie')

options = ['scissors', 'rock', 'paper']
player1Name = input('player 1 name: ')
player2Name = input('player 2 name: ')

while True:

while True:
    player1Option = input('\n'+ player1Name + ' choose from rock, paper or scissors: ')
    if player1Option not in options:
        print(player1Option + ' is an invalid option. Try again')
        continue
    else:
        break

while True:
    player2Option = input('\n' + player2Name + ' choose from rock, paper or scissors: ')
    if player2Option not in options:
        print(player2Option + ' is an invalid option. Try again')
        continue
    else:
        break

rockPaperSci(player1Name, player1Option, player2Name, player2Option)

# adivinar un numero al azar
import random
ran = random.randint(1, 9)
print(ran)
intentos = 0
n = 0
while n != ran:
    n = input("ingrese numero o salga con exit: ")
    intentos += 1
    if n == "exit":
        print("fin")
        break
    else:
        n = int(n)
        if n == ran:
            print ("acertastes en {} intentos!!".format(intentos))
        elif n < ran:
            print("tiene que ser mayor")
        else:
            print("tiene que ser menor")

# forma de crear lista comprimida
x = [1, 2, 3]
y = [5, 10, 15]
customlist = [a*b for a in x for b in y if a*b%2 != 0]
# customlist = [5, 15, 15, 45]

# crea lista con la interseccion de 2 listas
import random
#a = random.sample(range(1,30), 12) #sin repeticiones
#b = random.sample(range(1,30), 14)
a = [random.randint(1,30) for x in range(12)] #con
b = [random.randint(1,30) for x in range(14)]
print(a)
print(b)
c = [i for i in set(a) if i in b]
print(c)
# otro
d = list(set(i for i in a if i in b))
#otro sin usar set
e_rep = [i for i in a if i in b]
f = []
for x in e_rep:
  if x not in f:
    f.append(x)

def give_me(some_var = "Numero :"):
    return input(some_var)
# se puede invocar con solo give_me() y es default
# o se le puede mandar variable give_me("Letra: ")

# averiguar si es numero primo, con funcion
# usando lista comprimida
num = int(input('Insert a number: '))
n = int(math.sqrt(num))
a = [x for x in range(2, n + 1) if num % x == 0]
print(a)
def is_prime(var):
    if var > 1:
	    if len(a) == 0:
	    	print("primo")
	    else:
	    	print("NO primo")
    else:
    	print("NO primo")
is_prime(num)

#super comprimida
# The algorithm builds a list of factors including the number 2 and all odd numbers
# up to the square root of "a", and then checks if any of those numbers divides "a"
import math

if sum([ True if a % factor == 0 else False for factor in ( [2] + list(range(3,int(math.sqrt(a)),2) )) ]):
  print("Number is composite")
else:
  print("Number is prime")

# mio, completo, con fun()
import sys, math

digits = list(range(0,10))
strs = [str(d) for d in digits]

def enter_num():
    n = input("numero del 2 al 100: ")
    for c in n:
        if c not in strs:
            sys.exit("no es un numero")
        else:
            return int(n)

def es_primo(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        sqr_x = math.sqrt(x)
        for i in (2, sqr_x + 1):
            if x % i == 0:
                return False
        return True

def print_resultado(num):
    if es_primo(num):
        b = ""
    else:
        b = "no"
    print(num, b, "es primo")

print_resultado(enter_num())

# repetir pregunta hasta que ponga exit o sea el numero
import random
ran = random.randint(1, 11)
print(ran)
num = 0
inp = "0"
while inp != "exit" and int(inp) != ran:
    inp = input("ingrese numero del 1 al 10 o exit: ")
    if inp == "exit":
        print("fin")
        break
    elif int(inp) == ran:
        print("es ese")

# dar el 1er y ultimo obj de una lista de num
import random
a = [random.randint(1,15) for x in range(6)]
print(a)

def pri_ult(b):
    return [x for x in a[0::len(a)-1]]

print(pri_ult(a))

# Fibonacci de un cierto numero, fun()
n = int(input("numero: "))
def fibo(x):
    if x == 0:
        return 0
    elif x in (1, 2):
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(n))

# fibonacci armando una lista
a = int(input('Please input number: '))
if a == 1:
    b = [1]
elif a != 1:
    b = [1,1]
for i in b:
    if len(b) < a:
        i = b[-1] + b[-2]
        b.append(i)
print(b)

# otra
n = int(input('Please input number: '))
f = []
for i in range(n):
    if i == 0 or i == 1 :
        f.append(1)
    else:
        f.append(f[-2] + f[-1])
print(f)

# formas de crear una lista
# [start:stop:salto] si el start no se completa
# empieza desde default=0, sino se pone stop,
# termina en default=len()-1
# si el salto es negativo, va hacia atras
a = list(range(10))
b = [a[0], a[len(a)-1]]
c = [i for i in a[0::len(a)-1]]
print(a)
print(b)
print(c)
# busca la posicion de "4"  dentro de a[2:7]
ind = a.index(4,2,7)
print(ind)
# inserta 11 en la posicion 3, desplaza la lista
a.insert(3, 11)
print(a)
# remueve los obj desde el 2do hasta el 4to
for i in range(2, 5):
    a.remove(i)
print(a)
for i in a:
    print(a.index(i), ",", i)

a = list(range(10))
# print(*a) imprime la lista, pero sin "[]" ni ","

# juntar los elementos de una multidireccional
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_matrix = []
for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)
print(flatten_matrix)
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# con lista comprimida
flatten_matrix = [val for sublist in matrix for val in sublist]

# lista comprimida [lo que va a entrar a lst, ciclo for, ciclo for, condicional
# que tiene que cumplir para que entre a lst]
# en lst estara la multi x 2, de los numero impares del rango 1 al 10
# lst  =  [x * 2  for x in range (1, 11)   if  x % 2 == 1]
# [2, 6, 10, 14, 18]

# lista de numeros primos hasta el 49
no_primos = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primos = [x for x in range(2, 50) if x not in no_primos]
print(primos)

# listas conteniendo [const, x in (1,10), const*x]
# tabla de multiplicar
const = 4
table = [[const, x, const * x] for x in range(1, 11)]
print("tabla de multiplicar del ", const)
for i in table:
    print(i)
# dadas 2 listas, averiguar cuales de la 2da lista son multiplos
# de los objetos de la 1era. crear una nueva lista multi, donde
# cada sublista sea el par [numero de a, multiplo de b]
a = [2, 3, 4, 5, 6, 7]
b = [12, 14, 10]
c = [[x, y] for x in a for y in b if y % x == 0]
for i in c:
    print(i)"""
# filtering negative numbers uso de lambda
#lst = list(range(1, 10))
lst = filter((lambda x: x < 0), range(-5, 5))
print(list(lst))
