# Creación del diccionario 'informacion_personal'
informacion_personal = {
    "nombre": "Antonio Lucas",
    "edad": 35,
    "ciudad": "Ibarra",
    "profesion": "Arquitecto"
}

# Acceder y modificar el valor de la clave 'ciudad'
informacion_personal["ciudad"] = "Ibarra"

# Agregar una nueva clave-valor para la 'profesion'
informacion_personal["profesion"] = "Ingeniero Civil"

# Verificar si la clave 'telefono' existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998765432"

# Eliminar la clave 'edad' del diccionario
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)
