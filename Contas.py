class contas (object):
	def __init__(self):
		pass
	
	def setTitular(self, nome):
		self.Titular = str(nome)
	def getTitular(self):
		return self.Titular

	def setNumero(self, numero):
		self.Numero = str(numero)
	def getNumero(self):
		return self.Numero

	def setSaldo(self, saldo):
		self.Saldo = int(saldo)
	def getSaldo(self):
		return self.Saldo

	def Depositar(self, valor):
		self.Saldo += valor
	def Sacar(self, valor):
		self.Saldo -= valor

