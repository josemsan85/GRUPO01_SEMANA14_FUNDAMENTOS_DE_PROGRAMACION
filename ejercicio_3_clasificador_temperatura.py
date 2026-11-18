def clasificar_temperatura(temp):
    if temp < 10:
        return "Frío"
    elif temp < 20:       # aquí ya sabemos que es 10 o más
        return "Fresco"
    elif temp < 30:
        return "Cálido"
    else:                 # 30 o más
        return "Caliente"

print(clasificar_temperatura(5))
print(clasificar_temperatura(15))
print(clasificar_temperatura(25))
print(clasificar_temperatura(30))
