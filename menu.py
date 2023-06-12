matriz = []

def mostrar_diagonal_principal():
    print("Diagonal principal:")
    for i in range(len(matriz)):
        for j in range(i):
            print("        ", end="")
        print("{:8.2f}".format(matriz[i][i]))

def mostrar_diagonal_secundaria():
    print("Diagonal secundaria:")
    for i in range(len(matriz)):
        for j in range(len(matriz) - i - 1):
            print("        ", end="")
        print("{:8.2f}".format(matriz[i][len(matriz) - i - 1]))


def llenar_mostrar_matriz():
    global matriz

    filas = int(input("Ingrese el número de filas (entre 4 y 22): "))
    while filas < 4 or filas > 22:
        print("El número de filas debe ser mayor o igual a 4 y menor o igual a 22.")
        filas = int(input("Ingrese el número de filas (entre 4 y 22): "))

    columnas = int(input("Ingrese el número de columnas (entre 4 y 22): "))
    while columnas < 4 or columnas > 22:
        print("El número de columnas debe ser mayor o igual a 4 y menor o igual a 22.")
        columnas = int(input("Ingrese el número de columnas (entre 4 y 22): "))

    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            valor = int(input("Fila {}, Columna {}: ".format(i+1, j+1)))
            while valor < 100 or valor > 300:
                print("El valor debe estar entre 100 y 300.")
                valor = int(input("Fila {}, Columna {}: ".format(i+1, j+1)))
            matriz[i].append(valor)

    print()
    for fila in matriz:
        for elemento in fila:
            print("{:8.2f}".format(elemento), end="")
        print()

# Llamar a la función para llenar y mostrar la matriz
llenar_mostrar_matriz()

def mostrar_filas_columnas_externas():
    print("Filas y columnas externas:")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == 0 or i == len(matriz) - 1 or j == 0 or j == len(matriz[0]) - 1:
                print("{:8.2f}".format(matriz[i][j]), end="")
            else:
                print("        ", end="")
        print()

def mostrar_filas_columnas_cruz():
    print("Filas y columnas de una cruz:")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == len(matriz) // 2 or j == len(matriz[0]) // 2:
                print("{:8.2f}".format(matriz[i][j]), end="")
            else:
                print("        ", end="")
        print()

# Menú principal
while True:
    print("------ Menú Principal ------")
    print("1. Mostrar diagonal principal")
    print("2. Mostrar diagonal secundaria")
    print("3. Mostrar filas y columnas externas")
    print("4. Mostrar filas y columnas de una cruz")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_diagonal_principal()
    elif opcion == "2":
        mostrar_diagonal_secundaria()
    elif opcion == "3":
        mostrar_filas_columnas_externas()
    elif opcion == "4":
        mostrar_filas_columnas_cruz()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")