import matematicas_utils as mu   # el archivo matematicas_utils.py debe estar en la misma carpeta

def reporte_geometrico(radios):
    print(f"{'Radio':>8} | {'Área':>12} | {'Perímetro':>12}")   # encabezado de la tabla
    print("-" * 38)
    for r in radios:
        area = mu.area_circulo(r)
        perimetro = 2 * mu.PI * r      # perímetro = 2 × π × r
        print(f"{r:>8} | {area:>12.2f} | {perimetro:>12.2f}")

reporte_geometrico([1, 2, 5, 10])
