# Escritura de Archivo de Texto
# Creamos un archivo llamado "my_notes.txt" y escribimos tres líneas de notas personales.

with open("my_notes.txt", "w") as file:  # Abrimos el archivo en modo de escritura ("w")
    file.write("Primera nota: Aprendiendo sobre manipulación de archivos en Python.\n")  # Escribimos una línea
    file.write("Segunda nota: La lectura y escritura de archivos es fundamental en programación.\n")  # Escribimos otra línea
    file.write("Tercera nota: Es importante cerrar los archivos después de usarlos.\n")  # Otra línea más

# Lectura de Archivo de Texto
# Abrimos el archivo "my_notes.txt" en modo lectura ("r").
file = open("my_notes.txt", "r")

# Leemos cada línea y la mostramos
for line in file:
    print(line.strip())

# Cerramos el archivo manualmente
file.close()
