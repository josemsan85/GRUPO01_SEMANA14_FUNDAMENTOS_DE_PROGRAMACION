# Celsius a Fahrenheit con map
celsius = [0, 25, 37, 100]
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
print("Fahrenheit:", fahrenheit)

# solo los pares con filter
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, nums))
print("Pares:", pares)

# ordenar los diccionarios por edad con sorted
personas = [{"n": "Ana", "e": 30}, {"n": "Bob", "e": 22}, {"n": "Carla", "e": 27}]
orden = sorted(personas, key=lambda p: p["e"])
print("Ordenados por edad:", orden)
