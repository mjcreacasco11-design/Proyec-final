
# from modulos.pacientes import Pacientes

# sistema = Pacientes()

# # Registrar pacientes
# sistema.registrar(1, "Carlos", 25, "8888-1111")
# sistema.registrar(2, "María", 30, "8888-2222")

# # Mostrar pacientes
# print("LISTA DE PACIENTES:")
# print(sistema.mostrar())

# # Buscar paciente
# print("\nBUSCAR PACIENTE:")
# print(sistema.buscar(1))

# # Eliminar paciente
# sistema.eliminar(2)

# print("\nLISTA ACTUALIZADA:")
# print(sistema.mostrar())

# def generar_pacientes(self, cantidad):
#     inicio = 1

#     for i in range(inicio, cantidad + 1):
#         paciente = {
#             "id": i,
#             "nombre": f"Paciente {i}",
#             "edad": 25,
#             "telefono": f"8888-{i:04d}"
#         }

#         self.lista.agregar(paciente)

#     return cantidad


from modulos.pacientes import Pacientes
import time

sistema = Pacientes()

# CANTIDAD EDITABLE
cantidad = 1000

inicio = time.perf_counter()

sistema.generar_pacientes(cantidad)

fin = time.perf_counter()

print("PACIENTES GENERADOS:", cantidad)
print("TIEMPO DE REGISTRO:", fin - inicio, "segundos")

# BUSCAR UN PACIENTE INEXISTENTE
inicio = time.perf_counter()

resultado = sistema.buscar(cantidad + 1)

fin = time.perf_counter()

print("RESULTADO:", resultado)
print("TIEMPO DE BUSQUEDA:", fin - inicio, "segundos")
