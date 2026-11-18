def saludar(nombre, saludo="Hola"):   # saludo tiene valor por defecto
    print(f"{saludo}, {nombre}!")

saludar("Ana")                  # usa el saludo por defecto
saludar("Luis", "Buenos días")  # cambia el saludo
