import Matriz

class Paciente:
	next = None
	name = ""
	age = 0
	period = 0
	m = 0

	matriz_inicial = None
	matriz_final = None

	def __init__(self, name, age, period, m):
		self.name = name
		self.age = age
		self.period = period
		self.m = m

	def crear_matriz_inicial(self):
		nueva_matriz = Matriz.Matriz(self.m, self.m)
		nueva_matriz.crear_matriz()
		nueva_matriz.llenar_matriz(self.patI)
		# nueva_matriz.imprimir_matriz()
		self.matriz_inicial = nueva_matriz

	def imprimir_datos_de_paciente(self):
		print("---------------------------------------------------------------------")
		print("Nombre: " + self.name)
		print("Edad: " + self.age)
		print("Dimensión:" + str(self.m) + " x " + str(self.m))
		print("Periodos: " + str(self.period))
		print("---------------------------------------------------------------------")

	def crear_matriz_final(self, silencioso):
		print("método para manejo de rejillas")