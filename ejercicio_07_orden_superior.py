celsius = [0, 10, 25, 30, 100]
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
print("Fahrenheit:", fahrenheit)

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = list(filter(lambda n: n % 2 == 0, numeros))
print("Pares:", pares)

personas = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Bob", "edad": 22},
    {"nombre": "Carla", "edad": 25},
]
por_edad = sorted(personas, key=lambda persona: persona["edad"])
print("Ordenados por edad:", por_edad)
