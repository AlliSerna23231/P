import random

# Crear una matriz vacía
matriz = []

# Generar los valores aleatorios y llenar la matriz
for i in range(5):
    fila = []
    for j in range(5):
        valor = random.uniform(0.0, 100.0)
        valor = f"{valor:.2f}"
        fila.append(valor)
    matriz.append(fila)

# Mostrar la matriz
for fila in matriz:
    print(fila)


def encontrar_mayores(matriz):
    # Crear una lista vacía para almacenar los mayores de cada columna
    mayores = []

    # Recorrer cada columna de la matriz
    for columna in range(len(matriz[0])):
        # Obtener todos los valores de la columna actual
        valores_columna = [fila[columna] for fila in matriz]
        # Encontrar el mayor valor en la columna actual
        mayor = max(valores_columna)
        # Agregar el mayor valor a la lista de mayores
        mayores.append(mayor)

    # Mostrar los mayores de cada columna
    for i, mayor in enumerate(mayores):
        print(f"La mayor precipitación de la ciudad {i + 1} es: {mayor}")

    # Devolver la lista de mayores de cada columna
    return mayores


encontrar_mayores(matriz)


# Crear una lista vacía para almacenar los promedios de cada columna
promedios = []

# Recorrer cada columna de la matriz
for columna in range(len(matriz[0])):
    # Obtener todos los valores de la columna actual
    valores_columna = [float(fila[columna]) for fila in matriz]
    # Calcular el promedio de la columna actual
    promedio = sum(valores_columna) / len(valores_columna)
    promedio_entero = int(promedio)
    # Agregar el promedio a la lista de promedios
    promedios.append(promedio_entero)

promdeprom = sum(promedios) / len(promedios)
print(f"El promedio de los promedios de precipitaciones es: {promdeprom}")


def encontrar_mayores(matriz, promdeprom):
    filas, columnas = [], []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if float(matriz[i][j]) > promdeprom:
                filas.append(i)
                columnas.append(j)

    # Mostrar las filas y columnas encontradas
    for fila, columna in zip(filas, columnas):
        print(f"Las precipitaciones mayores que el pomedio general ({promdeprom}) fueron encontrados en los días {fila + 1}, de la ciudad {columna + 1}")
    return filas, columnas


encontrar_mayores(matriz, promdeprom)


def encontrar_menor(matriz):

    for i, fila in enumerate(matriz):
        menor = 0
        menor = min(fila)
        columna_menor = fila.index(menor)
        print(f"La menor precipitacion del día {i+1} es: {menor} de la ciudad {columna_menor+1}")

encontrar_menor(matriz)