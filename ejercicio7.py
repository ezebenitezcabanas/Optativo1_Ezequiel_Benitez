class ProductoStock:
    def __init__(self, nombre, stock_inicial, stock_minimo):
        self.nombre = nombre
        self.stock = stock_inicial
        self.stock_minimo = stock_minimo

    def reponer_stock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
            print(f"✓ Repuestos {cantidad} unidades. Stock total: {self.stock}")

    def vender(self, cantidad):
        if cantidad > self.stock:
            print(f"✗ VENTA RECHAZADA: No hay suficiente stock de '{self.nombre}'. Stock actual: {self.stock}")
        else:
            self.stock -= cantidad
            print(f"✓ Venta realizada de {cantidad} unidades. Stock restante: {self.stock}")
            if self.stock < self.stock_minimo:
                print(f"⚠️ ALERTA DE REPOSICIÓN: El stock de '{self.nombre}' ({self.stock}) está por debajo del mínimo ({self.stock_minimo}).")

    def __str__(self):
        return f"Producto: {self.nombre} | Stock actual: {self.stock} | Stock mínimo: {self.stock_minimo}"

# Prueba
if __name__ == "__main__":
    prod = ProductoStock("Leche Entera 1L", 10, 5)
    prod.vender(6) # Alerta por stock bajo
    prod.reponer_stock(10)
    print(prod)