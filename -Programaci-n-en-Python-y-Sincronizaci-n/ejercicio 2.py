# Crear una matriz 3x3 con valores numéricos
matriz = [
    [5, 2, 9],
    [3, 7, 1],
    [8, 4, 6]
]


# Función para ordenar una fila específica usando Bubble Sort
def bubble_sort_fila(matriz, fila_index):
    fila = matriz[fila_index]  # Obtener la fila seleccionada
    n = len(fila)

    # Algoritmo Bubble Sort
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:  # Comparar elementos adyacentes
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar valores


# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


# Mostrar la matriz original
print("Matriz Original:")
mostrar_matriz(matriz)

# Definir la fila a ordenar
fila_a_ordenar = 1  # Cambia este valor para ordenar otra fila

# Ordenar la fila seleccionada
bubble_sort_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
mostrar_matriz(matriz)
