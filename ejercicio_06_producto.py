class Producto:
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
        return f"[{self.nombre}] S/.{self.precio:.2f}"


producto = Producto("Laptop", 2500, 10)
print(producto)

producto.aplicar_descuento(15)
print(producto)

total = producto.vender(2)
print(f"Total de la venta: S/.{total:.2f}")
print("Stock restante:", producto.stock)

try:
    producto.vender(20)
except ValueError as error:
    print("Error:", error)
