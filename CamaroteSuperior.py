from VIP import VIP

class CamaroteSuperior (VIP):
	
	def __init__(self):
		self.localizacao = "Ala leste"
		self.valorCamarote = 500.0
		super(CamaroteSuperior,self).__init__()#para acessar as variaveis da classe pai

	def getLocalizacao(self):
		return self.localizacao
	def getValor(self):
		return self.valorCamarote