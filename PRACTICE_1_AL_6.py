"""# Escribir nombre y edad, y decir el año cuando tendras 100
name = input("Escriba su nombre: ")
age = int(input("Escriba su edad: "))
age_to_100 = 100 - age
year_date = 2020 + age_to_100
print(name, "tendra 100 años en el", year_date)
print("{} tendra 100 años en el {}".format(name, str(year_date)))

#Escriba numero y ver si es par o impar, si es
#multiplo de 4 cambiar salida
num = int(input("escriba numero: "))
if num % 4 == 0:
    print("es multiplo de 4")
elif num % 2 == 0:
    print("es par")
else: print("es impar")

#decir si el num es multiplo de check
check = int(input("escriba otro: "))
if num % check == 0:
    print(num, "es divisible por", check)
else:
    print(num, "no es divisible por", check)

#crear lista y hacer una nueva con los <=5
lista = [1, 6, 76, 3, 88, 4, 21]
lista2 = []
for n in lista:
    if n <= 5:
        lista2.append(n)
print(lista2)

#crear nueva con todos los menores a num
lista3 = []
num = int(input("numero: "))
for n in lista:
    if n <= num:
        lista3.append(n)
print(lista3)

#aca solo lista, sin crear nueva lista
print([n for n in lista if n<=num])

print("Welcome to the List Less Than Ten program..")
print("\nEnter number as a list\n")
lista1=[int(i) for i in input().split()]
lista2=[j for j in lista1 if j<11]
print(lista2)

#Crear lista de numeros pares del 1 al 10
x = list(range(2, 11, 2))
print(x)
lista = [j for j in range(1,11) if j % 2 == 0]
print(lista)

#dado un numero, encontrar sus divisores
num = int(input("numero: "))
nume = int(num/2)
for i in range(1, nume+1):
    if num % i == 0:
        print(i)
print(num)

#idem pero con listas
lista1 = list(range(1, nume+1))
lista2 = [j for j in lista1 if num % j == 0 ]
lista2.append(num)
print(lista2)

#dadas 2 listas random, hacer una 3era con la interseccion, sin dupli
A = [2, 5, 8, 4, 2, 7, 4, 12]
B = [1, 8, 5, 2, 9, 6, 8]
print("A:", A)
print("B:", B)
C = []
for a in A:
    if a in B and a not in C:
        C.append(a)
print("C(interseccion):", C)

#import random
#a = random.sample(range(100), 5)
#This line of code containing a list of 5 random numbers from 0 to 99.
#a = list(random.sample(range(30), 10 + random.randrange(4)))
#b = list(random.sample(range(40), 10 + random.randrange(6)))
print("otro")
#a C la creo como lista, porque lo de adentro es de conjuntos
#con el set, lo que hago es sacar los duplicados
C = list(set(A).intersection(set(B)))
C.sort()
print("A:", A)
print("B:", B)
print("C(interseccion):", C)"""

# encontrar si una palabra es capicua
S = input("Ingrese palabra:")
bandera = True
medio = int(len(S) / 2)
for x in range(0, medio):
    if S[x] != S[-1 - x]:
        bandera = False
if bandera:
    print("es capicua")
else:
    print("no es capicua")

# otro, invirtiendo la cadena
Sinv = S[::-1]
if S == Sinv:  # o S == S[::-1]
    print("Si")
else:
    print("No")asd