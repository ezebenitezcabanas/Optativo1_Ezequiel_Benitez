class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}

    def registrar_nota(self, materia, nota):
        self.notas[materia] = nota

    def calcular_promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas.values()) / len(self.notas)

    def esta_aprobado(self, nota_minima=60):
        return self.calcular_promedio() >= nota_minima

    def __str__(self):
        res = f"=== BOLETÍN DE NOTAS: {self.nombre} ===\n"
        for materia, nota in self.notas.items():
            res += f"- {materia}: {nota}\n"
        promedio = self.calcular_promedio()
        condicion = "APROBADO" if self.esta_aprobado() else "REPROBADO"
        res += f"Promedio: {promedio:.2f} | Condición: {condicion}"
        return res

# Prueba
if __name__ == "__main__":
    estudiante = Estudiante("Rodrigo Silva")
    estudiante.registrar_nota("Python I", 85)
    estudiante.registrar_nota("Base de Datos", 70)
    estudiante.registrar_nota("Algoritmos", 90)

    print(estudiante)