import csv

alumnos = []
aprobados = 0

with open("estudiantes.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        # los datos del CSV llegan como texto, por eso se usa float()
        nota1 = float(fila["nota1"])
        nota2 = float(fila["nota2"])
        nota3 = float(fila["nota3"])
        promedio = (nota1 + nota2 + nota3) / 3

        alumnos.append({"nombre": fila["nombre"], "promedio": promedio})
        print(f"{fila['nombre']}: {promedio:.2f}")

        if promedio >= 13:
            aprobados += 1

top = max(alumnos, key=lambda alumno: alumno["promedio"])
print(f"Top alumno: {top['nombre']} ({top['promedio']:.2f})")
print(f"Aprobaron: {aprobados}")
