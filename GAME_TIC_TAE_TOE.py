# tic tac toe tablero
def dibujar_tablero(n):
    for i in range(n):
        horizontal(n)
        vertical(n+1)
    horizontal(n)

def horizontal(p):
    print(" --- " *p)

def vertical(p):
    print("|    " *p)

num = int(input("nª de tablero? "))
dibujar_tablero(num)

# dadas matrices, responder quien gana
import random
m = []
for x in range(0,3):
    line = [random.randint(0,2) for x in range(3)]
    m.append(line)

for x in range(0,3):
    print(m[x])

#chequeamos si gano ply1
#hay ganador en columans?
def line_check(m):
    for x in range(3):
        if len(set(m[x])) == 1 and m[x][0] != 0:
            return m[x][0]
    return 0

def col_check(m):
    numpy = []
    for x in range(3):
        line = []
        for y in range(3):
            line.append(m[y][x])
        numpy.append(line)
    return line_check(numpy)

def diag_check(m):
    if m[0][0] == m[1][1] and m[0][0] == m[1][1]:
        return m[0][0]
    if m[0][2] == m[1][1] and m[2][0] == m[1][1]:
        return m[0][0]

matrix = [[2, 2, 1], [1, 2, 1], [1, 2, 2]]
for z in range(3):
    print(matrix[z])

print("player", line_check(matrix), "won line")
print("player", col_check(matrix), "won column")
print("player", diag_check(matrix), "won diagonal")

# manejo de entradas de coordenadas
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def free_place(p, r, c):
    if matrix[r - 1][c - 1] == 0:
        if p:
            matrix[r - 1][c - 1] = "X"
        else:
            matrix[r - 1][c - 1] = "O"
        for i in range(3):
            print(matrix[i])
        return True
    else:
        return False

def still_inputs(mat):
    inputs = 0
    ply = True
    while inputs < 9:
        if ply:
            print("Player1 your turn")
        else:
            print("Player2 your turn")
        inp = input("input coord (row,col): ")
        inp = inp.split(",")
        row = int(inp[0].strip())
        col = int(inp[1].strip())
        if free_place(ply, row, col):
            ply = not ply
            inputs += 1
        else:
            print("place taken, again")
    return "game is over"

print(still_inputs(matrix))