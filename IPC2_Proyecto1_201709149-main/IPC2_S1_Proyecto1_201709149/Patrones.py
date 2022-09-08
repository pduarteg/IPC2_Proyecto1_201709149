class Patrones:
	first = None
	cant = 0

	def agregar(self, patron):
		if self.first == None:
			self.first = patron
			self.cant += 1
		else:
			temp = self.first

			for i in range(self.cant - 1):
				temp = temp.next

			temp.next = patron
			self.cant += 1