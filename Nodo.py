class Nodo:
	arriba = None
	abajo = None
	izquierda = None
	derecha = None

	estado = False # Estado infectado: False es sana, True es infectada
	cambiar = False # Indica si el estado debe cambiar para el siguiente periodo

	x = 0
	y = 0

	def __init__(self, arriba, abajo, izquierda, derecha, x, y):
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

	def verificar_vecinos(self):
		ady_inf = 0

		if self.derecha != None:
			if self.derecha.estado == True:
				ady_inf += 1

			if self.derecha.arriba != None:
				if self.derecha.arriba.estado == True:
					ady_inf += 1

		if self.arriba != None:
			if self.arriba.estado == True:
				ady_inf += 1

			if self.arriba.izquierda != None:
				if self.arriba.izquierda.estado == True:
					ady_inf += 1

		if self.izquierda != None:
			if self.izquierda.estado == True:
				ady_inf += 1

			if self.izquierda.abajo != None:
				if self.izquierda.abajo.estado == True:
					ady_inf += 1

		if self.abajo != None:
			if self.abajo.estado == True:
				ady_inf += 1

			if self.abajo.derecha != None:
				if self.abajo.derecha.estado == True:
					ady_inf += 1

		return ady_inf