"""# escribir un archivo
open_file = open('test.txt', 'w')
open_file.write('testprimer renglon\n')
open_file.write('segundo renglon\n')
open_file.write('tercer renglon\n')
open_file.close()

#otra forma de escribir, mejor syntaxis
with open('names.txt', 'w') as open_file:
    open_file.write('cuarto renglon\n')

#leer un archivo y contar los nombres
with open('names.txt', 'r') as open_file:
    all_text = open_file.read()
    all_text = all_text.split("\n")
print(all_text)
Darth = 0
Lea = 0
Luke = 0
for s in all_text:
    if s == "Darth":
        Darth += 1
    elif s == "Lea":
        Lea += 1
    else:
        Luke += 1
print(Darth, Lea, Luke)

# leyendo por renglon
Darth = 0
Lea = 0
Luke = 0
with open('names.txt', 'r') as open_file:
    line = open_file.readline()
#chars = list(line) imprime ["D","a","r","t","h","\n"]
#line = line.strip() #cada obj de la lista es un renglon
    while line:
        line = line.strip()
        if line == "Darth":
            Darth += 1
        elif line == "Lea":
            Lea += 1
        else:
            Luke += 1
        line = open_file.readline()
print(Darth, Lea, Luke)

counter_dict = {}
with open('names.txt') as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()


print("directorio: ", counter_dict) #{"Luke":15, "Darth":31, "Lea":54}
print(counter_dict["Lea"])      #54 ,valor de Lea

for i in counter_dict.items(): #("Luke",15)   ("Darth", 31)   ("Lea", 54)
    print(i)                #  se pueden operar pero como pares juntos

for i in counter_dict:      # luke    Darth   Lea  "no se pueden operar"
    print(i)
#pero si puedo usar sus nombre para operar sus valores
total = 0
for i in counter_dict:
    total += counter_dict[i]
print(total)

total = 0
for x, y in counter_dict.items(): # se pueden operar por separado
    print(x, y)
    if x == "Lea":
        print("esta Lea!!")
    total += int(y)
print(total)

print("solo keys:", counter_dict.keys(), "no se puede acceder")
print("solo values:", counter_dict.values(), "tampoco")
print("los pares:", counter_dict.items(), "sirve para iterar")

# interseccion de numeros en 2 archivos de texto
with open('num1.txt', 'r') as open_file:
    text1 = open_file.read()
    text1 = text1.split()
    print(text1)
with open('num2.txt', 'r') as open_file:
    text2 = open_file.read()
    text2 = text2.split()
    print(text2)
L = []
for i in text1:
    if i in text2:
        L.append(i)
print(L)

#con funcion pasar sting a integer
def arch_a_ints(filename):
	list_to_return = []
	with open(filename) as f:
		line = f.readline()
		while line:
			list_to_return.append(int(line))
			line = f.readline()
	return list_to_return

# otra forma de funcion
def arch_list_int(filename):
    with open(filename) as f:
        f = list(map(x, f.read().split()))
    return f

primes = arch_a_ints('num1.txt')
happies = arch_a_ints('num2.txt')

overlap = [x for x in primes if x in happies]
print(overlap)

# que la compu adivine tu numero con busq binaria
def guess_num():
    tries = 0
    start = 0
    end = 101
    while True:
        guess = int((start+end)/2)
        tries += 1
        print("pc guess:", guess, " tries:", tries)
        if guess == N:
            return tries
        elif guess > N:
                print("too high")
                end = guess
        else:
            start = guess
            print("too low")

N = 54
print("yo got it in", guess_num(), "tries")"""

# idem pero sin busqueda binaria
import random


def guess_number():
    start = 0
    end = 101
    tries = 0
    while True:
        guess = random.randint(start, end)
        print("is", guess, "your number?")
        tries += 1
        answer = input("answer (l=low) (h=high) (y=yes):")
        if answer == "y":
            return tries
        elif answer == "h":
            end = guess
        else:
            start = guess


print("you got it in", guess_number(), "try/es")