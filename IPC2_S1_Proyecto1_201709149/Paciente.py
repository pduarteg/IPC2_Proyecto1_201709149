import Matriz
import Patrones

class Paciente:
	next = None
	name = ""
	age = 0
	period = 0
	m = 0
	caso_de_enfermedad = ""

	rejilla_inicial = None
	lista_de_patrones = Patrones.Patrones()
	

	def __init__(self, name, age, period, m):
		self.name = name
		self.age = age
		self.period = period
		self.m = m

	def crear_matriz_inicial(self):
		nueva_matriz = Matriz.Matriz(self.m, self.m)
		nueva_matriz.crear_matriz()
		# nueva_matriz.imprimir_matriz()
		self.rejilla_inicial = nueva_matriz

	def imprimir_datos_de_paciente(self):
		print("---------------------------------------------------------------------")
		print("Nombre: " + self.name)
		print("Edad: " + self.age)
		print("Dimensión:" + str(self.m) + " x " + str(self.m))
		print("Periodos: " + str(self.period))
		print("Rejilla: ")
		self.rejilla_inicial.imprimir_matriz()
		print("---------------------------------------------------------------------")

	def diagnosticar(self, m_muestra):
		matriz_diagnostico = Matriz.Matriz(self.m, self.m)
		cell_o = m_muestra
		cell_n = matriz_diagnostico.raiz

		# Creación de copia de la rejilla inicial
		for i in range(self.m):
			cell_o = cell_o.abajo
			cell_n = cell_n.abajo

			for j in range(self.m):
				cell_o = cell_o.derecha
				cell_n = cell_n.derecha
				if cell_o.estado == True:
					cell_n.set_estado(True)

		# Aplicación de los cambios k veces para N_per periodos de repetición del estado
		p = self.period
		N_per = 0
		for k in range(p):
			self.indentificar_futuros_cambios(matriz_diagnostico)
			self.aplicar_cambios_a_celulas(matriz_diagnostico)
			N_per += 1
			if comparar_rejillas(m_muestra, matriz_diagnostico):
				m_muestra.establecer_periodo_de_recurrencia(N_per)
				print("Se ha encontrado una repetición del patrón en N = " + str(N))
				break

	def comparar_rejillas(self, A, B):
		simetry = True
		node_A = A.raiz
		node_B = B.raiz

		for i in range(self.m):
			if simetry:
				A = A.abajo
				B = B.abajo
			else:
				break

			for j in range(self.m):
				A = A.derecha
				B = B.derecha
				if A.estado != B.estado:
					simetry = False
					break
		return simetry

	def indentificar_futuros_cambios(self, matrix):
		cell = matrix.raiz

		for i in range(self.m):
			cell = cell.abajo

			for j in range(self.m):
				cell = cell.derecha
				ady_inf = cell.verificar_vecinos()

				# Caso de célula (sana o contagiada)
				if cell.estado == False: # célula sana
					if ady_inf == 3:
						cell.set_cambiar(True)
				elif cell.estado == True: # célula infectada
					if ady_inf == 1 or ady_inf == 4:
						cell.set_cambiar(True)

	def aplicar_cambios_a_celulas(self, matrix):
		cell = matrix.raiz

		for i in range(self.m):
			cell = cell.abajo
			for j in range(self.m):
				cell = cell.derecha
				if cell.cambiar:
					cell.realizar_cambio()