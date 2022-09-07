class Nodo:
	arriba = None
	abajo = None
	izquierda = None
	derecha = None

	estado = False # Estado infectado: False es sana, True es infectada
	cambiar = False # Indica si el estado debe cambiar para el siguiente periodo

	x = 0
	y = 0

	def __init__(self, arriba, abajo, izquierda, derecha, tipo, x, y):
		self.arriba = arriba
		self.abajo = abajo
		self.izquierda = izquierda
		self.derecha = derecha
		self.x = x
		self.y = y

	def set_estado(self, estado):
		self.estado = estado

	def set_cambiar(self, cambiar):
		self.cambiar = cambiar

	def realizar_cambio(self):
		self.cambiar = False
		if self.estado:
			self.estado = False
		else:
			self.estado = True

	def verificar_vecinos(self, cell):
		ady_inf = 0

		if cell.derecha != None:
			if cell.derecha.estado == True:
				ady_inf += 1
		if cell.arriba != None:
			if cell.arriba.estado == True:
				ady_inf += 1
		if cell.izquierda != None:
			if cell.izquierda.estado == True:
				ady_inf += 1
		if cell.abajo != None:
			if cell.abajo.estado == True:
				ady_inf += 1

		return ady_inf