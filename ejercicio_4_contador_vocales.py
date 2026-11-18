def contar_vocales(texto):
    vocales = "aeiouáéíóú"    # vocales con tilde incluidas
    texto = texto.lower()     # todo en minúscula para no importar mayúsculas
    cantidad = 0
    for letra in texto:
        if letra in vocales:  # si la letra es vocal, suma 1
            cantidad += 1
    return cantidad

print(contar_vocales("Hola Mundo"))
print(contar_vocales("Programación"))
print(contar_vocales("ÁRBOL y Murciélago"))
