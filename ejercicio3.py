class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self, incluir_aguinaldo=True):
        meses = 13 if incluir_aguinaldo else 12
        return self.salario_mensual * meses

    def __str__(self):
        return (f"Empleado: {self.nombre} | Cargo: {self.cargo} | "
                f"Salario Mensual: {self.salario_mensual:,} Gs. | "
                f"Salario Anual (con aguinaldo): {self.calcular_salario_anual():,} Gs.")

# Prueba
if __name__ == "__main__":
    emp1 = Empleado("Carlos Benítez", "Analista de sistemas", 4500000)
    print(emp1)