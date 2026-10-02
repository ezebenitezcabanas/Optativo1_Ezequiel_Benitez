class LineaTelefono:
    def __init__(self, numero, gb_plan):
        self.numero = numero
        self.gb_plan = gb_plan
        self.gb_consumidos = 0.0

    def registrar_consumo(self, gb):
        if self.gb_consumidos >= self.gb_plan:
            print(f"⚠️ PAQUETE AGOTADO: La línea {self.numero} ya agotó su paquete de {self.gb_plan} GB.")
            return

        self.gb_consumidos += gb
        if self.gb_consumidos >= self.gb_plan:
            print(f"⚠️ PAQUETE AGOTADO: Ha alcanzado el límite de {self.gb_plan} GB de su plan.")

    def gb_disponibles(self):
        restante = self.gb_plan - self.gb_consumidos
        return max(0.0, restante)

    def __str__(self):
        return (f"Línea: {self.numero} | Plan: {self.gb_plan} GB | "
                f"Consumidos: {self.gb_consumidos:.1f} GB | Disponibles: {self.gb_disponibles():.1f} GB")

# Prueba
if __name__ == "__main__":
    linea = LineaTelefono("0981-000000", 10.0)
    linea.registrar_consumo(4.5)
    print(linea)
    linea.registrar_consumo(6.0) # Agota el paquete