class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, producto, cantidad):
        self.items.append(Item(producto, cantidad))

    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.items)

    def mostrar_detalle(self):
        print("=== DETALLE DEL CARRITO DE COMPRAS ===")
        for item in self.items:
            print(f"- {item.producto.nombre} x{item.cantidad} = {item.calcular_subtotal():,} Gs.")
        print(f"TOTAL GENERAL: {self.calcular_total():,} Gs.")

# Prueba
if __name__ == "__main__":
    p1 = Producto("Teclado Mecánico", 250000)
    p2 = Producto("Mouse Gamer", 120000)

    carrito = Carrito()
    carrito.agregar_item(p1, 1)
    carrito.agregar_item(p2, 2)
    carrito.mostrar_detalle()