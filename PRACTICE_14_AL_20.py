"""# crear una nueva lista sin repet
# con loop y con sort
a = [1, 1, 2, 3, 3, 4, 5, 5]
print(a)
def crear_sin_rep(b):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b
def set_lista(b):
    return list(set(b))
print(crear_sin_rep(a))
print(set_lista(a))

# otra con lista comprimida
b = []
[b.append(i) for i in a if i not in b]
print(b)

#otra
c = []
c.extend(i for i in a if i not in c)
print(c)

#invertir el orden de las palabras de una frase
string = input("frase: ")
new = string.split()
new = new[::-1]
new = " ".join(new)
print(new)

# escribir un generador de codigo de varios niveles
import string
import random
def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for c in range(size))

print(pw_gen(int(input('How many characters in your password?'))))

#otro
import random
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

p =  "".join(random.sample(s,passlen ))
print(p)

# mio
import random
import string
a = string.ascii_letters[:26]
A = string.ascii_letters[26:]
n = string.digits
s = string.punctuation

def pw_gen(lv):
    if lv == 1:
        new = "".join(random.sample(a,8))
    elif lv == 2:
        new = "".join(random.sample(a,4)+random.sample(A,4))
    elif lv == 3:
        new = "".join(random.sample(a,4)+random.sample(A,2)+random.sample(n,2))
    else:
        new = "".join(random.sample(a,2)+random.sample(A,2)+random.sample(n,2)+random.sample(s,2))
    return mezcla(new)

def mezcla(lista):
    l = []
    for x in range(0,8):
        i = random.randint(0,7-x)
        l.append(lista.pop(i))
    return l

lev = int(input("level: "))
print(pw_gen(lev))

# ordenar una lista con loop basico
import random
a = random.sample(range(1,11), 5)
print("a: ",a)
#c = sorted(a)
#print(c)
b = []
for x in range(0,len(a)):
    mini = a[0]
    ind = 0
    for j in range(1,len(a)):
        if a[j] <= mini:
            ind = j
            mini = a[j]
    b.append(mini)
    del a[ind]
print("b: ", b)

# dada una lista ordenada, usar busqueda binaria para buscar un n
import random
L = sorted(random.sample(range(1,21), 10)) #sin repe
#b = sorted([random.randint(1,21) for x in range(10)]) #con repe
print("L: ",L)

def esta(a,num):
    start = 0
    end = len(a)-1

    while True:
        mid = int((end+start)/2)
        if mid == start or mid == end:
            if a[mid] == num or a[end] == num:
                return True
            else:
                return False
        if a[mid] == num:
            return True
        elif a[mid] > num:
            end = mid
        else:
            start = mid
for x in range(0,11):
    print("n:", x, esta(L,x))"""

# usando lista comprimida y bucle de una funcion
a = [1, 3, 5, 7]
num = 0

def binary_search(n, L=[]):
    mid = int(len(L) / 2)
    if len(L) == 1:
        if L[0] == n:
            return True
        else:
            return False
    if n == L[mid]:
        return True
    elif n < L[mid]:
        return binary_search(n, L[:mid])
    elif n > L[mid]:
        return binary_search(n, L[mid:])


for x in range(0, 9):
    print("n:", x, binary_search(x, a))



