class Habitacion:
    def __init__(self, numero, tipo, tarifa_por_noche):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_por_noche = tarifa_por_noche
        self.ocupada = False

    def ocupar(self):
        if self.ocupada:
            print(f"⚠️ RECHAZADO: La habitación {self.numero} ya está ocupada.")
        else:
            self.ocupada = True
            print(f"✓ Habitación {self.numero} ocupada con éxito.")

    def liberar(self):
        if not self.ocupada:
            print(f"⚠️ RECHAZADO: La habitación {self.numero} ya está libre.")
        else:
            self.ocupada = False
            print(f"✓ Habitación {self.numero} liberada con éxito.")

    def calcular_costo_estadia(self, noches):
        return self.tarifa_por_noche * noches

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"
        return f"Habitación {self.numero} ({self.tipo}) | Tarifa: {self.tarifa_por_noche:,} Gs./noche | Estado: {estado}"

# Prueba
if __name__ == "__main__":
    hab = Habitacion(101, "Matrimonial", 250000)
    print(hab)
    hab.ocupar()
    print(f"Costo por 3 noches: {hab.calcular_costo_estadia(3):,} Gs.")
    hab.liberar()