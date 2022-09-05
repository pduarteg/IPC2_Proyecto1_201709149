class Nodo:
	arriba = None
	abajo = None
	izquierda = None
	derecha = None

	TipoDato = False

	x = 0
	y = 0

	dato = None

	def __init__(self, arriba, abajo, izquierda, derecha, tipo, x, y):
		self.arriba = arriba
		self.abajo = abajo
		self.izquierda = izquierda
		self.derecha = derecha
		TipoDato = tipo
		self.x = x
		self.y = y

	def voltear_azulejo(self):
		if self.dato == "W":
			self.dato = "B"
		else:
			self.dato = "W"
	
	def dato_inverso(self):
		if self.dato == "W":
			return "B"
		else:
			return "W"