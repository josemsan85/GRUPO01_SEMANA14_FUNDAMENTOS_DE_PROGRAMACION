def clasificar_temperatura(temp):
    if temp < 10:
        return "Frío"
    elif temp < 20:
        return "Fresco"
    elif temp < 30:
        return "Cálido"
    else:
        return "Caliente"


print("5°C:", clasificar_temperatura(5))
print("15°C:", clasificar_temperatura(15))
print("25°C:", clasificar_temperatura(25))
print("30°C:", clasificar_temperatura(30))
