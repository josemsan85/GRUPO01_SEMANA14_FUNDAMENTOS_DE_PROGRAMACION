def calcular(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:
            print("Error: no se puede dividir entre cero")
            return None
        return a / b
    else:
        print("Error: operador no válido")
        return None


print("10 + 5 =", calcular(10, 5, "+"))
print("10 - 5 =", calcular(10, 5, "-"))
print("10 * 5 =", calcular(10, 5, "*"))
print("10 / 5 =", calcular(10, 5, "/"))
print("10 / 0 =", calcular(10, 0, "/"))
print("10 % 5 =", calcular(10, 5, "%"))
