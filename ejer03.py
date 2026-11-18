def clasificar_temperatura(temp):
    if temp < 10:
        return "Frío"
    elif temp < 20:
        return "Fresco"
    elif temp < 30:
        return "Cálido"
    else:
        return "Caliente"
print(clasificar_temperatura(5))