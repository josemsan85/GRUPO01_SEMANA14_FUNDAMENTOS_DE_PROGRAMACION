def contar_vocales(texto):
    vocales = "aeiouáéíóú"
    total = 0
    for letra in texto.lower():
        if letra in vocales:
            total += 1
    return total
print(contar_vocales("parangaricutirimucaro"))
#son 10 aaaiuiiuao