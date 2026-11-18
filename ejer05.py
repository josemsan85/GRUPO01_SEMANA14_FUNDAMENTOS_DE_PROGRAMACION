import os
import csv
# Obtener la ruta de la carpeta del programa
ruta = os.path.dirname(os.path.abspath(__file__))
# Crear las rutas de los archivos
csv_path = os.path.join(ruta, "estudiantes.csv")
txt_path = os.path.join(ruta, "reporte_notas.txt")
# Crear el archivo CSV con datos de ejemplo
with open(csv_path, "w", newline="", encoding="utf-8") as archivo:
    campos = ["nombre", "nota1", "nota2", "nota3"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows([
        {"nombre": "Ana", "nota1": 15, "nota2": 18, "nota3": 16},
        {"nombre": "Luis", "nota1": 10, "nota2": 12, "nota3": 14},
        {"nombre": "Pedro", "nota1": 18, "nota2": 17, "nota3": 19}
    ])
# Leer el archivo CSV
estudiantes = []
with open(csv_path, "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for alumno in lector:
        promedio = (
            float(alumno["nota1"]) +
            float(alumno["nota2"]) +
            float(alumno["nota3"])
        ) / 3
        estudiantes.append({
            "nombre": alumno["nombre"],
            "promedio": promedio
        })
# Generar el reporte TXT
with open(txt_path, "w", encoding="utf-8") as archivo:
    for alumno in estudiantes:
        archivo.write(
            f"{alumno['nombre']}: {alumno['promedio']:.2f}\n"
        )
    top = max(estudiantes, key=lambda alumno: alumno["promedio"])
    aprobados = sum(
        1 for alumno in estudiantes
        if alumno["promedio"] >= 13
    )
    archivo.write(f"\nTop alumno: {top['nombre']}\n")
    archivo.write(f"Promedio: {top['promedio']:.2f}\n")
    archivo.write(f"Alumnos aprobados: {aprobados}\n")
print("Archivos creados correctamente.")