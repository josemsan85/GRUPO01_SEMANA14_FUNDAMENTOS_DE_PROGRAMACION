import matematicas_utils as mu


def reporte_geometrico(radios):
    print("Radio     Área        Perímetro")
    print("-" * 31)
    for radio in radios:
        area = mu.area_circulo(radio)
        perimetro = 2 * mu.PI * radio
        # :<10 alinea a la izquierda en 10 espacios, :.2f deja 2 decimales
        print(f"{radio:<10}{area:<12.2f}{perimetro:.2f}")


reporte_geometrico([1, 2, 5, 10])
