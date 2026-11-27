
from estructuras.lista_enlazada import ListaEnlazada


class Medicos:
    def _init_(self):
        self.lista = ListaEnlazada()

    def registrar(self, identificacion, nombre, especialidad, telefono):
        # Validar campos vacíos
        if not identificacion or not nombre or not especialidad or not telefono:
            return "Error: Todos los campos son obligatorios."

        # Evitar identificaciones duplicadas
        if self.buscar(identificacion):
            return "Error: El médico ya está registrado."

        medico = {
            "id": identificacion,
            "nombre": nombre,
            "especialidad": especialidad,
            "telefono": telefono
        }

        self.lista.agregar(medico)
        return medico

    def mostrar(self):
        return self.lista.mostrar()

    def buscar(self, identificacion):
        return self.lista.buscar(identificacion)

    def eliminar(self, identificacion):
        return self.lista.eliminar(identificacion)

    def actualizar(self, identificacion, nombre, especialidad, telefono):
        medico = self.buscar(identificacion)

        if not medico:
            return "Error: Médico no encontrado."

        medico["nombre"] = nombre
        medico["especialidad"] = especialidad
        medico["telefono"] = telefono

        return "Médico actualizado correctamente."

    def buscar_especialidad(self, especialidad):
        medicos = self.mostrar()

        return [
            medico for medico in medicos
            if medico["especialidad"].lower() == especialidad.lower()
        ]

    def contar(self):
        return len(self.mostrar())
