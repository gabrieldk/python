#calculadora.py
class Calculadora(object):

	def __init__(self, a, b):
		self.a = a
		self.b = b
	def soma(self):
		return self.a + self.b
	def subtrair(self):
		return self.a - self.b
	def multiplicar(self):
		return self.a * self.b
	def dividir(self):
		return self.a/self.b
