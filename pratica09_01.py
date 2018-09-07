

from Empregados import Empregados

def main ():
	
	empregado01 = Empregados()
	empregado02 = Empregados()
	empregado03 = Empregados()

	print("Primeiro empregado: \n")
	empregado01.setNome()
	empregado01.setSobrenome()
	empregado01.setSalario()
	print("\n------------------------------")

	print("Segundo empregado: \n")
	empregado02.setNome()
	empregado02.setSobrenome()
	empregado02.setSalario()
	print("\n------------------------------")

	print("Terceiro empregado: \n")
	empregado03.setNome()
	empregado03.setSobrenome()
	empregado03.setSalario()

	print("\n------------------------------")

	print("Nome: %s %s"%(empregado01.getNome(), empregado01.getSobrenome()))
	print("Salário Anual: %d"%(12*empregado01.getSalario()))
	print("\n------------------------------------------------------------------------------------------")

	print("Nome: %s %s"%(empregado02.getNome(), empregado02.getSobrenome()))
	print("Salário Anual: %d"%(12*empregado02.getSalario()))
	print("\n------------------------------------------------------------------------------------------")

	print("Nome: %s %s"%(empregado03.getNome(), empregado03.getSobrenome()))
	print("Salário Anual: %d"%(12*empregado03.getSalario()))
	print("\n------------------------------------------------------------------------------------------")

	print ("Aumentar Salário de %s %s \n" %(empregado01.getNome(),empregado01.getSobrenome()))
	empregado01.aumentarSalario()

	print ("Aumentar Salário de %s %s \n" %(empregado02.getNome(),empregado02.getSobrenome()))
	empregado02.aumentarSalario()

	print ("Aumentar Salário de %s %s \n" %(empregado03.getNome(),empregado03.getSobrenome()))
	empregado03.aumentarSalario()

	print("Atualizado")

	print("Nome: %s %s"%(empregado01.getNome(), empregado01.getSobrenome()))
	print("Salário: %d"%(empregado01.getSalario()))
	print("\n------------------------------------------------------------------------------------------")

	print("Nome: %s %s"%(empregado02.getNome(), empregado02.getSobrenome()))
	print("Salário: %d"%(empregado02.getSalario()))
	print("\n------------------------------------------------------------------------------------------")

	print("Nome: %s %s"%(empregado03.getNome(), empregado03.getSobrenome()))
	print("Salário: %d"%(empregado03.getSalario()))
	print("\n------------------------------------------------------------------------------------------")

main()