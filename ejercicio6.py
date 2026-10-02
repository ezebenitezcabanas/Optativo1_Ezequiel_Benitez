class CuentaCorriente:
    def __init__(self, cliente, saldo_inicial=0):
        self.cliente = cliente
        self.saldo = saldo_inicial

    def acreditar_saldo(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"✓ Acreditados: {monto:,} Gs. Nuevo saldo: {self.saldo:,} Gs.")
        else:
            print("El monto a acreditar debe ser mayor a 0.")

    def registrar_consumo(self, monto):
        if monto <= 0:
            print("El consumo debe ser mayor a 0.")
        elif monto > self.saldo:
            print(f"✗ CONSUMO RECHAZADO: Fondo insuficiente. Intento de compra: {monto:,} Gs. Saldo disponible: {self.saldo:,} Gs.")
        else:
            self.saldo -= monto
            print(f"✓ Consumo registrado: {monto:,} Gs. Saldo restante: {self.saldo:,} Gs.")

    def __str__(self):
        return f"Cuenta de {self.cliente} | Saldo actual: {self.saldo:,} Gs."

# Prueba
if __name__ == "__main__":
    cuenta = CuentaCorriente("Ana Gómez")
    cuenta.acreditar_saldo(100000)
    cuenta.registrar_consumo(40000)
    cuenta.registrar_consumo(80000) # Se rechaza
    print(cuenta)