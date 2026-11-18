class Producto:
    def __init__(self, nombre, precio, stock):   # constructor
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, pct):
        self.precio *= (1 - pct / 100)           # baja el precio según el %

    def vender(self, cantidad):
        if cantidad > self.stock:                # si no alcanza el stock da error
            raise ValueError("Sin stock")
        self.stock -= cantidad
        return self.precio * cantidad            # devuelve el total de la venta

    def __str__(self):                           # para que print(p) se vea bien
        return f"[{self.nombre}] S/.{self.precio:.2f} - Stock: {self.stock}"

p = Producto("Laptop", 2500, 10)
print(p)
p.aplicar_descuento(15)
total = p.vender(2)
print(f"Total de la venta: S/.{total:.2f}")
print(p)

# p.vender(100)   # quitar el # para probar el ValueError
