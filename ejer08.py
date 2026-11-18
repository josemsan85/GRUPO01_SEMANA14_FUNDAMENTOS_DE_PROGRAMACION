import matematics_utils as mu
def reporte_geometrico(radios):
    print("REPORTE GEOMETRICO")
    print("--------------------------------")
    print("Radio\tArea\t\tPerimetro")
    print("--------------------------------")
    for r in radios:
        area = mu.area_circulo(r)
        perimetro = 2 * mu.PI * r
        print(f"{r}\t{area:.2f}\t\t{perimetro:.2f}")
radios = [2, 3, 4, 5]
reporte_geometrico(radios)
