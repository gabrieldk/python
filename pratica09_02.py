from Ingresso import Ingresso
from VIP import VIP
from CamaroteSuperior import CamaroteSuperior

def main():

	ingresso = Ingresso()
	ingressoVIP = VIP()
	local = CamaroteSuperior()

	ingresso.imprimeValor()
	ingressoVIP.imprimeValorVIP()
	print("\n")

	print("Valor do ingresso para o camarote: %s"%(local.getValor()))
	print ("Localização do camarote: %s" %(local.getLocalizacao()))

main()