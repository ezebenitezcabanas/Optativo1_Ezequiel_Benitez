class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos

    def __str__(self):
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"'{self.titulo}' - {self.artista} ({minutos}:{segundos:02d})"

class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def duracion_total(self):
        total_seg = sum(c.duracion_segundos for c in self.canciones)
        minutos = total_seg // 60
        segundos = total_seg % 60
        return f"{minutos} min {segundos} seg"

    def __str__(self):
        res = f"=== Lista de Reproducción: {self.nombre} ===\n"
        for i, c in enumerate(self.canciones, 1):
            res += f"{i}. {c}\n"
        res += f"Duración Total: {self.duracion_total()}"
        return res

# Prueba
if __name__ == "__main__":
    lista = ListaReproduccion("Favoritas 80s")
    lista.agregar_cancion(Cancion("Bohemian Rhapsody", "Queen", 354))
    lista.agregar_cancion(Cancion("Billie Jean", "Michael Jackson", 294))
    print(lista)