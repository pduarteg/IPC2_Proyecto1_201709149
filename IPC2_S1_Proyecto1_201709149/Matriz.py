import Nodo

class Matriz:
	raiz = Nodo.Nodo(None, None, None, None, False, 0, 0)
	columnas = 0
	filas = 0

	n = 0 # frecuencia de repetición del patrón inicial
	n_1 = 0 # frecuencia de repetición de un patrón distinto del inicial

	def __init__(self, C, R):
		self.columnas = C
		self.filas = R

	def crear_matriz(self):
		# print("Columnas: " + str(self.columnas) + ", filas: " + str(self.filas))
		t = self.raiz

		for i in range(self.columnas):
			t.derecha = Nodo.Nodo(None, None, None, None, False, i+1, 0)
			t = t.derecha

		t = self.raiz
		for j in range(self.filas):
			t.abajo = Nodo.Nodo(None, None, None, None, False, 0, j+1)
			t = t.abajo

		# Crear columna vacía y enlazar
		t = self.raiz

		n = 0

		for i in range(self.columnas):
			t = t.derecha
			aux = self.raiz.abajo
			superior = t

			for j in range(self.filas):
				nuevo = Nodo.Nodo(None, None, None, None, False, i+1, j+1)

				while aux.derecha != None:
					aux = aux.derecha

				nuevo.arriba = superior
				nuevo.izquierda = aux
				aux.derecha = nuevo
				superior.abajo = nuevo

				aux = aux.abajo
				superior = nuevo

				n+=1
				#print("Nodo no:"  + str(n))

	def imprimir_matriz(self):
		t = self.raiz
		for i in range(self.filas):
			t = t.abajo
			aux = t
			for j in range(self.columnas):
				aux = aux.derecha
				estado_de_celula = ""

				if aux.estado:
					estado_de_celula = "1"
				else:
					estado_de_celula = "0"

				if j == 0:
					print("       	[" + estado_de_celula + "]", end="")
				else:
					print("[" + estado_de_celula + "]", end="")
			print(" ")

	# Método que establece el estado sano o infectado de una celda por sus coordenadas
	def establecer_por_coordenada(self, x , y, estado):
		t = self.raiz
		t = t.abajo
		t = t.derecha
		nodo = None
		encontrado = False

		#print("buscando (" + str(x) + ", " + str(y) + ")")

		for j in range(self.columnas):
			if t.x == x:
				for i in range(self.filas):
					if t.y == y:
						nodo = t
						#print("Encontrado!")
						nodo.set_estado(estado)
						break
					else:
						t = t.abajo
						# print(" MOVIENDO A ABAJO ")
				break
			else:
				t = t.derecha
				# print(" MOVIENDO A DERECHA ")

		if encontrado:
			return nodo
		else:
			return None

	def get_primer_nodo(self):
		return self.raiz.abajo.derecha

	def establecer_periodo_de_recurrencia(self, n):
		self.n = n