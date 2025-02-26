# Crear una matriz 3x3 con valores numéricos
matriz = [
    [4, 7, 2],
    [1, 9, 6],
    [8, 3, 5]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor_buscado):
    for fila in range(len(matriz)):  # Recorremos las filas
        for columna in range(len(matriz[fila])):  # Recorremos las columnas
            if matriz[fila][columna] == valor_buscado:
                return fila, columna  # Devuelve la posición si lo encuentra
    return None  # Retorna None si no lo encuentra

# Definir el valor a buscar
valor_buscado = 9

# Buscar el valor en la matriz
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if posicion:
    print(f"Se encontró {valor_buscado} en la fila {posicion[0]} y columna {posicion[1]}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")
