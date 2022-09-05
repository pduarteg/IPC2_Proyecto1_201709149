import Nodo

class Matriz:
	raiz = Nodo.Nodo(None, None, None, None, False, 0, 0)
	columnas = 0
	filas = 0

	def __init__(self, C, R):
		self.columnas = C
		self.filas = R

	def crear_matriz(self):
		#print("Columnas: " + str(self.columnas) + ", filas: " + str(self.filas))
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
				nuevo = Nodo.Nodo(None, None, None, None, True, i+1, j+1)

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

	def llenar_matriz(self, cadena):
		cadena = cadena.rstrip()
		cadena = cadena.lstrip()

		t = self.raiz
		aux = t
		x = 1
		y = 1
		n = 0

		for z in cadena:			

			# Disminuye la columna
			while n < y:
				aux = aux.abajo
				n += 1

			nodo = aux

			for i in range(x):
				nodo = nodo.derecha

			nodo.dato = z
			#print("dato agregado en: (" + str(x) + ", " + str(y) + ")")
			
			# Aumenta la columna solo si se está al final de la fila
			if x == self.columnas:
				y += 1
				x = 1
			else:
				x += 1

	def imprimir_matriz(self):
		t = self.raiz
		for i in range(self.filas):
			t = t.abajo
			aux = t
			for j in range(self.columnas):
				aux = aux.derecha
				if aux.dato != None and j == 0:
					print("       [" + aux.dato + "]", end="")
				elif aux.dato != None:
					print("[" + aux.dato + "]", end="")
			print(" ")

	def buscar_por_coordenada(self, x , y):
		t = self.raiz
		t = t.abajo
		t = t.derecha
		nodo = None
		encontrado = False

		print("buscando (" + str(x) + ", " + str(y) + ")")

		for j in range(self.columnas):
			if t.x == x:
				for i in range(self.filas):
					if t.y == y:
						nodo = t
						print("Encontrado!")
						print("con dato: " + str(nodo.dato))
						break
					else:
						t = t.abajo
						print(" MOVIENDO A ABAJO ")
				break
			else:
				t = t.derecha
				print(" MOVIENDO A DERECHA ")

		if encontrado:
			return nodo
		else:
			return None

	def get_primer_nodo(self):
		return self.raiz.abajo.derecha