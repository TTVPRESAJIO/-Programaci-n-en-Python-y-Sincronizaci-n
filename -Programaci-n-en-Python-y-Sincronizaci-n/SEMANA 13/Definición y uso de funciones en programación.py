import random


def calcular_promedios(matriz_temperaturas, num_ciudades, num_semanas, num_dias):
    """
    Calcula los promedios semanales de temperatura por ciudad.

    Args:
        matriz_temperaturas (list): Matriz tridimensional con temperaturas aleatorias.
        num_ciudades (int): Número de ciudades.
        num_semanas (int): Número de semanas.
        num_dias (int): Número de días en una semana.

    Returns:
        list: Lista de listas con los promedios semanales de cada ciudad.
    """
    promedios = []
    for i in range(num_ciudades):
        promedios_ciudades = []
        for j in range(num_semanas):
            temperaturas_semana = matriz_temperaturas[i][j]
            promedio_semana = sum(temperaturas_semana) / num_dias
            promedios_ciudades.append(promedio_semana)
        promedios.append(promedios_ciudades)
    return promedios


# Parámetros del problema
num_ciudades = 3
num_dias = 7
num_semanas = 4

# Generar matriz de temperaturas aleatorias
matriz_temperaturas = [
    [
        [random.randint(10, 35) for _ in range(num_dias)]
        for _ in range(num_semanas)
    ]
    for _ in range(num_ciudades)
]

# Llamamos a la función para calcular los promedios
promedios = calcular_promedios(matriz_temperaturas, num_ciudades, num_semanas, num_dias)

# Lista de nombres de ciudades
nombres_ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]

# Imprimir resultados
for i in range(num_ciudades):
    print(f"\nPromedios de temperatura para {nombres_ciudades[i]}:")
    for j in range(num_semanas):
        print(f"Semana {j + 1}: {promedios[i][j]:.2f}°C")

