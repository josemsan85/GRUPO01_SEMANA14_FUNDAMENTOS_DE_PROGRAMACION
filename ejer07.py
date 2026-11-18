# Lista de temperaturas en Celsius
temperaturas = [0, 15, 20, 25, 30, 35]
# Convertir Celsius a Fahrenheit usando map()
fahrenheit = list(map(
    lambda c: (c * 9/5) + 32,
    temperaturas
))
print("Temperaturas en Fahrenheit:")
print(fahrenheit)
# Lista de números
numeros = [10, 5, 8, 3, 12, 7, 4, 9]
# Filtrar solamente los números pares
pares = list(filter(
    lambda n: n % 2 == 0,
    numeros
))
print("\nNúmeros pares:")
print(pares)
# Lista de estudiantes
estudiantes = [
    {"nombre": "Ana", "promedio": 16},
    {"nombre": "Luis", "promedio": 12},
    {"nombre": "Pedro", "promedio": 18},
    {"nombre": "Maria", "promedio": 15}
]
# Ordenar estudiantes por promedio
ordenados = sorted(
    estudiantes,
    key=lambda alumno: alumno["promedio"]
)
print("\nEstudiantes ordenados por promedio:")
print(ordenados)
