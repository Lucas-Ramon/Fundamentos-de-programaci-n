import numpy as np

# Definir las ciudades, días de la semana y número de semanas
ciudades = ['Quito', 'Guayaquil', 'Cuenca']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Generar una matriz 3D aleatoria para representar las temperaturas (valores entre 10 y 30 grados)
np.random.seed(0)  # Para reproducibilidad
temperaturas = np.random.uniform(10, 30, (len(ciudades), len(dias_semana), semanas))


# Función para calcular la temperatura promedio de cada ciudad durante el periodo de tiempo
def calcular_promedio_temperaturas(temperaturas, ciudades, semanas):
    """
    Esta función calcula el promedio de temperaturas de varias ciudades durante un período de semanas.

    Parámetros:
    temperaturas (numpy array): Una matriz 3D que contiene las temperaturas para diferentes ciudades, días y semanas.
    ciudades (list): Una lista con los nombres de las ciudades.
    semanas (int): El número de semanas para las que se tienen datos.

    Retorna:
    dict: Un diccionario con los nombres de las ciudades como claves y los promedios de temperatura como valores.
    """
    promedios_semanales = np.zeros((len(ciudades), semanas))

    # Bucle anidado para calcular los promedios por ciudad y por semana
    for i in range(len(ciudades)):
        for j in range(semanas):
            promedios_semanales[i, j] = np.mean(temperaturas[i, :, j])

    # Crear un diccionario con los promedios para cada ciudad
    promedios_totales = {}
    for i, ciudad in enumerate(ciudades):
        promedios_totales[ciudad] = np.mean(promedios_semanales[i])  # Promedio total por ciudad

    return promedios_totales


# Calcular y mostrar los promedios de temperaturas por ciudad
promedios_ciudades = calcular_promedio_temperaturas(temperaturas, ciudades, semanas)

# Imprimir los resultados
for ciudad, promedio in promedios_ciudades.items():
    print(f"El promedio de temperatura en {ciudad} es: {promedio:.2f}°C")

