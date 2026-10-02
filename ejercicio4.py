class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: '{self.titulo}' por {self.autor} | Estado: {estado}"

# Prueba
if __name__ == "__main__":
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", True)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", False)

    print(libro1)
    print(libro2)