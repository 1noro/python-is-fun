T=[[" "," "," "],[" "," "," "],[" "," "," "]]
en_juego = True
human_turn = True

def insert(tablero, filaint, columnastr, simbolo):
    filaint -= 1
    if (columnastr == "A") or (columnastr == "a"):
        tablero[filaint][0] = simbolo
    elif (columnastr == "B") or (columnastr == "b"):
        tablero[filaint][1] = simbolo
    elif (columnastr == "C") or (columnastr == "c"):
        tablero[filaint][2] = simbolo
    return tablero

def IA1(t):
    f, c = 1, "A"
    if t[0][0] == " ":
        f, c = 2, "B"
    return f, c

while en_juego:
    print("\n A B C")
    print("1"+T[0][0]+"|"+T[0][1]+"|"+T[0][2])
    print(" "+"-"*5)
    print("2"+T[1][0]+"|"+T[1][1]+"|"+T[1][2])
    print(" "+"-"*5)
    print("3"+T[2][0]+"|"+T[2][1]+"|"+T[2][2])

    if human_turn:
        print("Tu turno...")
        fila = int(input("Número de fila (1,2,3): "))
        columna = input("Letra de columna (A,B,C): ")
        simbolo = "X"
        human_turn = False
    else:
        print("Turno de la máquina...")
        fila, columna = IA1(T)
        simbolo = "O"
        human_turn = True

    T = insert(T, fila, columna, simbolo)

    print("\n"*100)
