class Nodo:
	arriba = None
	abajo = None
	izquierda = None
	derecha = None

	estado = False # False es sana, True es infectada

	x = 0
	y = 0

	def __init__(self, arriba, abajo, izquierda, derecha, tipo, x, y):
		self.arriba = arriba
		self.abajo = abajo
		self.izquierda = izquierda
		self.derecha = derecha
		estado = tipo
		self.x = x
		self.y = y

	def set_estado(self, estado):
		self.estado = estado
