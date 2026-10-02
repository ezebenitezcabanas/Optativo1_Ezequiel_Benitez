class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"--- FICHA DE CLIENTE ---\nNombre: {self.nombre}\nCédula: {self.cedula}\nTeléfono: {self.telefono}\n"

# Prueba
if __name__ == "__main__":
    cliente1 = Cliente("María López", "1.234.567", "0981-123456")
    cliente2 = Cliente("Juan Pérez", "987.654", "0971-654321")

    print(cliente1)
    print(cliente2)