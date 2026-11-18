def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")


nombre = input("¿Cómo te llamas? ")
saludar(nombre)
saludar(nombre, "Buenos días")
