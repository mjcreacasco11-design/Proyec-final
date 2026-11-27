
from estructuras.lista_enlazada import ListaEnlazada


class Pacientes:
    def __init__(self):
        self.lista = ListaEnlazada()

    def registrar(self, identificacion, nombre, edad, telefono):
        paciente = {
            "id": identificacion,
            "nombre": nombre,
            "edad": edad,
            "telefono": telefono
        }

        self.lista.agregar(paciente)
        return paciente

    def mostrar(self):
        return self.lista.mostrar()

    def buscar(self, identificacion):
        return self.lista.buscar(identificacion)

    def eliminar(self, identificacion):
        return self.lista.eliminar(identificacion)

    def generar_pacientes(self, cantidad):
        pacientes_actuales = self.mostrar()

        if pacientes_actuales:
            ultimo_id = max(p["id"] for p in pacientes_actuales)
        else:
            ultimo_id = 0

        for i in range(1, cantidad + 1):
            identificacion = ultimo_id + i

            self.registrar(
                identificacion,
                f"Paciente {identificacion}",
                25,
                f"8888-{identificacion % 10000:04d}"
            )

        return cantidad
