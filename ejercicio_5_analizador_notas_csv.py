import csv

# primero creo el archivo estudiantes.csv con datos de prueba
def crear_csv(archivo):
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["nombre", "nota1", "nota2", "nota3"])  # encabezados
        escritor.writerow(["Ana", 15, 14, 16])
        escritor.writerow(["Bob", 10, 12, 9])
        escritor.writerow(["Carla", 18, 17, 19])
        escritor.writerow(["Diego", 12, 13, 14])
        escritor.writerow(["Elena", 8, 11, 10])

def analizar_notas(archivo):
    alumnos = []   # aquí guardo el nombre y promedio de cada alumno
    with open(archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            suma = float(fila["nota1"]) + float(fila["nota2"]) + float(fila["nota3"])
            promedio = suma / 3
            alumnos.append({"nombre": fila["nombre"], "promedio": promedio})

    for a in alumnos:   # promedio de cada alumno
        print(f"{a['nombre']}: {a['promedio']:.2f}")

    top = max(alumnos, key=lambda a: a["promedio"])   # el de mayor promedio
    print(f"Top alumno: {top['nombre']} ({top['promedio']:.2f})")

    aprobados = 0
    for a in alumnos:
        if a["promedio"] >= 13:   # aprueba con 13 o más
            aprobados += 1
    print(f"Aprobados: {aprobados}")

crear_csv("estudiantes.csv")
analizar_notas("estudiantes.csv")
