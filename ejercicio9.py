class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.atendido = False

    def marcar_atendido(self):
        self.atendido = True

    def __str__(self):
        estado = "Atendido" if self.atendido else "Pendiente"
        return f"Hora: {self.hora} | Paciente: {self.paciente} | Estado: {estado}"

class Agenda:
    def __init__(self, fecha):
        self.fecha = fecha
        self.turnos = []

    def agendar_turno(self, turno):
        self.turnos.append(turno)

    def listar_pendientes(self):
        print(f"\n--- Turnos pendientes para la fecha {self.fecha} ---")
        pendientes = [t for t in self.turnos if not t.atendido]
        if not pendientes:
            print("No hay turnos pendientes.")
        for t in pendientes:
            print(t)

# Prueba
if __name__ == "__main__":
    agenda = Agenda("02/10/2026")
    t1 = Turno("Laura Martínez", "08:00")
    t2 = Turno("Pedro Rojas", "09:00")
    
    agenda.agendar_turno(t1)
    agenda.agendar_turno(t2)
    
    t1.marcar_atendido()
    agenda.listar_pendientes()