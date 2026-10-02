class Producto:
    def __init__(self, nombre, precio_unitario, cantidad_stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad_stock = cantidad_stock

    def calcular_valor_total(self):
        return self.precio_unitario * self.cantidad_stock

    def __str__(self):
        return (f"Producto: {self.nombre} | Precio: {self.precio_unitario:,} Gs. | "
                f"Stock: {self.cantidad_stock} | Valor Total Stock: {self.calcular_valor_total():,} Gs.")

# Prueba
if __name__ == "__main__":
    p1 = Producto("Arroz 1kg", 8500, 20)
    p2 = Producto("Aceite 1L", 14000, 15)

    print(p1)
    print(p2)