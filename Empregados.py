

class Empregados (object):
	
	def __init__(self):
		pass

	def setNome(self):
		self.nome = input("Nome do empregado: ")
	def getNome(self):
		return self.nome

	def setSobrenome(self):
		self.sobrenome = input("Sobrenome: ")
	def getSobrenome(self):
		return self.sobrenome

	def setSalario(self):
		self.salario = float(input("Salário mensal do empregado: "))
		
		if self.salario < 0:
			self.salario = 100

	def getSalario(self):
		return self.salario

	def aumentarSalario(self):
		self.aumento = float(input("taxa de aumento: "))
		self.aumento /= 100 

		self.salario += self.salario*self.aumento  