import Paciente

class Lista_pacientes:

	first = None
	cant = 0

	def agregar(self, paciente):
		if self.first == None:
			self.first = paciente
			self.cant += 1
		else:
			temp = self.first

			for i in range(self.cant - 1):
				temp = temp.next

			temp.next = paciente
			self.cant += 1

	def mostrar_pacientes(self):
		temp = self.first

		print("-----------------------------------------")
		while temp != None:
			temp.printself()
			temp = temp.next
			print("-----------------------------------------")

	def buscar_por_nombre(self, name):
		r_paciente = None
		temp = self.first

		while temp != None:
			if temp.name == name:
				r_paciente = temp
				break
			else:
				temp = temp.next

		return r_paciente

	def buscar_por_posicion(self, pos):
		actual = self.first
		for i in range(pos-1):
			actual = actual.next
		return actual

	def diagnosticar_pacientes(self):
		t = self.first

		while t != None:
			t.diagnosticar()
			t = t.next