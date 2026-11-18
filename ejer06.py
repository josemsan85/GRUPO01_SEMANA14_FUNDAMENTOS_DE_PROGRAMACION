class Producto:
    """Producto con nombre, precio y stock."""
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def aplicar_descuento(self, pct):
        self.precio *= (1 - pct / 100)
    def vender(self, cantidad):
        if cantidad > self.stock:
            raise ValueError("Sin stock")
        self.stock -= cantidad
        return self.precio * cantidad
    def __str__(self):
        return f"[{self.nombre}] S/.{self.precio:.2f} (stock: {self.stock})"
p = Producto("Laptop", 2500, 10)
p.aplicar_descuento(15)       # el precio baja a 2125
print(p.vender(2))            # 4250.0, y el stock queda en 8
print(p)                      # [Laptop] S/.2125.00 (stock: 8)

try:
    p.vender(50)              # pide más de lo que hay
except ValueError as e:
    print("ValueError:", e)   # ValueError: Sin stock