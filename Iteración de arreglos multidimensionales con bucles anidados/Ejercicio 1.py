import numpy as np

# Definir las ciudades, días de la semana y número de semanas
ciudades = ['Quito', 'Guayaquil', 'Cuenca']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Generar una matriz 3D aleatoria para representar las temperaturas (valores entre 10 y 30 grados)
np.random.seed(0)  # Para reproducibilidad
temperaturas = np.random.uniform(10, 30, (len(ciudades), len(dias_semana), semanas))

# Calcular los promedios de temperatura por ciudad y semana
promedios_semanales = np.zeros((len(ciudades), semanas))

for i in range(len(ciudades)):
    for j in range(semanas):
        promedios_semanales[i, j] = np.mean(temperaturas[i, :, j])

# Mostrar los promedios de temperaturas para cada ciudad y semana
resultados = {}
for i, ciudad in enumerate(ciudades):
    resultados[ciudad] = promedios_semanales[i]

# Imprimir los resultados
for ciudad, promedios in resultados.items():
    print(f"{ciudad}:")
    for semana, promedio in enumerate(promedios, start=1):
        print(f"  Semana {semana}: {promedio:.2f}°C")
