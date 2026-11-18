def calcular(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:                          # no se puede dividir entre 0
            print("Error: división por cero")
            return None
        else:
            return a / b
    else:                                   # si el operador no es ninguno de los 4
        print("Error: operador no válido")
        return None

print(calcular(10, 5, "+"))
print(calcular(10, 5, "-"))
print(calcular(10, 5, "*"))
print(calcular(10, 5, "/"))
print(calcular(10, 0, "/"))   # prueba de división por cero
print(calcular(10, 5, "%"))   # prueba de operador inválido
