def burbuja_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Definición de la matriz 3x3
matriz = [
    [3, 1, 2],
    [6, 4, 5],
    [9, 7, 8]
]

# Seleccionar la fila a ordenar (por ejemplo, la segunda fila, índice 1)
fila_a_ordenar = 1

# Mostrar matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Ordenar la fila seleccionada
burbuja_sort(matriz[fila_a_ordenar])

# Mostrar matriz con la fila ordenada
print("\nMatriz después de ordenar la fila seleccionada:")
imprimir_matriz(matriz)

