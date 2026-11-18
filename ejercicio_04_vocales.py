def contar_vocales(texto):
    vocales = "aeiouáéíóú"
    contador = 0
    for letra in texto.lower():
        if letra in vocales:
            contador += 1
    return contador


print("Hola Mundo:", contar_vocales("Hola Mundo"))
print("Murciélago ÁRBOL:", contar_vocales("Murciélago ÁRBOL"))
