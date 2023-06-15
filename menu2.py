matriz = []

def llenar_mostrar_matriz():
    global matriz

    filas = 30
    columnas = 10

    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            valor = int(input("Ingrese precipitación del día {} y de la ciudad {}: ".format(i+1, j+1)))
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
