
from modulos.pacientes import Pacientes

sistema = Pacientes()

# Registrar pacientes
sistema.registrar(1, "Carlos", 25, "8888-1111")
sistema.registrar(2, "María", 30, "8888-2222")

# Mostrar pacientes
print("LISTA DE PACIENTES:")
print(sistema.mostrar())

# Buscar paciente
print("\nBUSCAR PACIENTE:")
print(sistema.buscar(1))

# Eliminar paciente
sistema.eliminar(2)

print("\nLISTA ACTUALIZADA:")
print(sistema.mostrar())

def generar_pacientes(self, cantidad):
    inicio = 1

    for i in range(inicio, cantidad + 1):
        paciente = {
            "id": i,
            "nombre": f"Paciente {i}",
            "edad": 25,
            "telefono": f"8888-{i:04d}"
        }

        self.lista.agregar(paciente)

    return cantidad