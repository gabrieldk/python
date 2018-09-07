from Contas import contas
from Poupanca import Poupanca

def main ():
	conta = contas()
	poup = Poupanca(30)

	conta.setTitular('Gabriel')
	conta.setSaldo(100)
	conta.setNumero('1')

	print("Titular %s portador da conta de numero %s tem saldo %d"%(conta.getTitular(), conta.getNumero(), conta.getSaldo()))
	
	conta.Depositar(20)
	print("Titular %s portador da conta de numero %s tem saldo %d"%(conta.getTitular(), conta.getNumero(), conta.getSaldo()))

	conta.Sacar(50)
	print("Titular %s portador da conta de numero %s tem saldo %d"%(conta.getTitular(), conta.getNumero(), conta.getSaldo()))

	print("Saldo da Poupança: %f"%(poup.getSaldoPoup()))
	poup.reajustar()
	print("Saldo da Poupança: %f"%(poup.getSaldoPoup()))
main()