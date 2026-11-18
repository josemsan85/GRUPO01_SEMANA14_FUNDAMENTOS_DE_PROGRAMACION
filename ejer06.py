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