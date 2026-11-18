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
        print(f"Error: operador '{operador}' no válido")
        return None
print(calcular (8, 9, "-"))
#en teoria -1