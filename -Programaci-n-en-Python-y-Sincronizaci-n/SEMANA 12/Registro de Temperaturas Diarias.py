# Importar libreria para generar temperaturas ramdon para el ejercicio:
import random

num_ciudades = 3
num_dias = 7
num_semanas = 4

matriz_temperaturas= [
    [ 
         [random.randint(10,35) for _ in range (num_dias)]
        for _ in range ( num_semanas)
        ]
    for _ in range ( num_ciudades)
]

promedios = []
for i in range(num_ciudades):
    promedios_ciudades = []

    for j in range(num_semanas):
        temperaturas_semana=matriz_temperaturas[i][j]
        promedio_semana=sum(temperaturas_semana)/ num_dias
        promedios_ciudades.append(promedio_semana)
    promedios.append(promedios_ciudades)

nombres_ciudades=["ciudad A","ciudad B","ciudad C"]

for i in range(num_ciudades):
    print(f"\nPromedios de temperatura para {nombres_ciudades[i]}:")
    for j in range(num_semanas):
        print(f"semana{j+1}:{promedios[i][j]:.2f}°C")
