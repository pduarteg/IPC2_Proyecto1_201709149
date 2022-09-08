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
		
		while temp != None:
			temp.imprimir_datos_de_paciente()
			temp = temp.next			

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

	def diagnosticar_todos_los_pacientes(self):
		t = self.first

		while t != None:
			n_case = t.diagnosticar(t.rejilla_inicial, True, True)

			if n_case == 0:
				n1_case = t.diagnosticar_lista_de_patrones()
				t.caso_de_enfermedad = "leve"

				if n1_case == None:
					n1_case = 0
					
				if n1_case == 1:
					t.caso_de_enfermedad = "mortal"
				elif n1_case > 1:
					t.caso_de_enfermedad = "grave"        
			elif n_case == 1:
				t.caso_de_enfermedad = "mortal"
			elif n_case > 1:
				t.caso_de_enfermedad = "mortal"

			t = t.next