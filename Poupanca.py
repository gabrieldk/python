from Contas import contas

class Poupanca (contas):
	"""docstring for Poupanca """
	def __init__(self, Saldo):
		self.SaldoPoup = float(Saldo)
		super(Poupanca , self).__init__()
	
	def reajustar (self):
		self.SaldoPoup += self.SaldoPoup*0.01
	def getSaldoPoup(self):
		return self.SaldoPoup

