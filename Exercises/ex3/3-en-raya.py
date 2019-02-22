A1=" "
A2=" "
A3=" "
B1=" "
B2=" "
B3=" "
C1=" "
C2=" "
C3=" "

en_juego = True

while en_juego:
    print(" A B C")
    print("1"+A1+"|"+A2+"|"+A3)
    print(" "+"-"*5)
    print("2"+B1+"|"+B2+"|"+B3)
    print(" "+"-"*5)
    print("3"+C1+"|"+C2+"|"+C3)

    fila = input("Número de fila (1,2,3): ")
    columna = input("Letra de columna (A,B,C): ")

    if (fila == "1"):
        if (columna == "A"):
            A1 = "X"
        if (columna == "B"):
            B1 = "X"
        if (columna == "C"):
            C1 = "X"
    elif (fila == "2"):
        if (columna == "A"):
            A2 = "X"
        if (columna == "B"):
            B2 = "X"
        if (columna == "C"):
            C2 = "X"
    elif (fila == "3"):
        if (columna == "A"):
            A3 = "X"
        if (columna == "B"):
            B3 = "X"
        if (columna == "C"):
            C3 = "X"
