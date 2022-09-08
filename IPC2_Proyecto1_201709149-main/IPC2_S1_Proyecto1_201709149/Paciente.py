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
		# nueva_matriz.imprimir_matriz()
		self.rejilla_inicial = nueva_matriz

	def imprimir_datos_de_paciente(self):
		print("---------------------------------------------------------------------")
		print("Nombre: " + self.name)
		print("Edad: " + self.age)
		print("Dimensión:" + str(self.m) + " x " + str(self.m))
		print("Periodos: " + str(self.period))
		print("Rejilla: ")
		rejilla = self.rejilla_inicial
		if rejilla != None:
			rejilla.imprimir_matriz()
		else:
			print("Sin rejilla cargada")
		print("---------------------------------------------------------------------")

	# Si inicial es verdadero, se verifica el patron inicial y agregan nuevos patrones encontrados
	# a la lista de patrones. Si inicial es falso, no se agregan nuevos patrones.
	def diagnosticar(self, m_muestra, inicial):
		print("	Se ha iniciado un diagnóstico...")
		# Creación de copia de la rejilla inicial		
		matriz_diagnostico = self.crear_copia_de_patron(m_muestra)

		# Aplicación de los cambios k veces para N_per periodos de repetición del estado
		p = self.period
		N_per = 0 # Número de periodo actual
		N_rep = 0 # Número de periodos de repetición (frecuencia)

		for k in range(p):
			self.indentificar_futuros_cambios(matriz_diagnostico)
			self.aplicar_cambios_a_celulas(matriz_diagnostico)
			N_per += 1
			print("	Estado de la rejilla tras " + str(N_per) + " periodo(s):")
			print("")
			matriz_diagnostico.imprimir_matriz()
			print("")
			print("")

			if self.comparar_rejillas(m_muestra, matriz_diagnostico):
				m_muestra.establecer_periodo_de_recurrencia(N_per)
				print("")
				print("Se ha encontrado una repetición del patrón en N = " + str(N_per))
				N_rep = N_per
				if N_rep == 1:
					#print("Se ha identificado un caso mortal.")
					break
			elif inicial == False:
				self.lista_de_patrones.agregar(self.crear_copia_de_patron(matriz_diagnostico))

		return N_rep

	def crear_copia_de_patron(self, muestra):
		patron_copiado = Matriz.Matriz(self.m, self.m)

		cell_o = muestra.raiz
		cell_n = patron_copiado.raiz

		for i in range(self.m):
			cell_o = cell_o.abajo
			cell_n = cell_n.abajo

			aux_o = cell_o
			aux_n = cell_n
			
			for j in range(self.m):				
				aux_o = aux_o.derecha
				aux_n = aux_n.derecha
				if aux_o.estado == True:
					aux_n.set_estado(True)

		return patron_copiado

	def comparar_rejillas(self, A, B):
		simetry = True
		node_A = A.raiz
		node_B = B.raiz

		for i in range(self.m):
			if simetry:
				node_A = node_A.abajo
				node_B = node_B.abajo

				node_A_aux = node_A
				node_B_aux = node_B
			else:
				break


			for j in range(self.m):
				node_A_aux = node_A_aux.derecha
				node_B_aux = node_B_aux.derecha
				if node_A_aux.estado != node_B_aux.estado:
					simetry = False
					break
		return simetry

	def indentificar_futuros_cambios(self, matrix):
		cell = matrix.raiz

		for i in range(self.m):
			cell = cell.abajo
			cell_aux = cell
			for j in range(self.m):
				cell_aux = cell_aux.derecha
				ady_inf = cell_aux.verificar_vecinos()
				#print("Celda (" + str(i+1) + ", " + str(j+1) + ") tiene " + str(ady_inf) + " vecinos")

				# Caso de célula (sana o contagiada)
				if cell_aux.estado == False: # célula sana
					if ady_inf == 3:
						cell_aux.set_cambiar(True)
				elif cell_aux.estado == True: # célula infectada
					if ady_inf == 1 or ady_inf == 4:
						cell_aux.set_cambiar(True)

	def aplicar_cambios_a_celulas(self, matrix):
		cell = matrix.raiz

		for i in range(self.m):
			cell = cell.abajo
			cell_aux = cell
			for j in range(self.m):
				cell_aux = cell_aux.derecha
				if cell_aux.cambiar:
					cell_aux.realizar_cambio()

	def diagnosticar_lista_de_patrones(self):
		first = self.lista_de_patrones.first
		
		# Almacena un periodo N_1 en caso de encontrarse repeticiones.
		# Establece siempre el menor N_1 posible.
		
		menor_n1 = None
		menor_aux = 0

		while first != None:
			menor_aux = self.diagnosticar(first, False)

			if menor_aux == 1:
				menor_n1 = 1
				break
			elif menor_n1 == None and menor_aux != 0:
				menor_n1 = menor_aux
			elif menor_n1 != None:
				if menor_aux > 0 and menor_aux < menor_n1:
					menor_n1 = menor_aux

		return menor_n1