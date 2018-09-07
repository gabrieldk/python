# -*- coding: utf-8 -*-
def main():
	
	a = int(input("digite o primeiro numero: \n"))
	b = int(input("digite o segundo numero: \n"))
	soma = a+b
	print("A soma de ",a,"+",b,"eh igual a",soma)

	num = int (input("digite um numero inteiro: "))
	soma = 0

	while num != 0:
		soma = soma + num
		num = int(input("digite um numero inteiro: "))

	print("A soma eh", soma)
	
	metros = float(input("insira um valor em metros "))
	print("o valor em milimetros eh ", metros*1000)
	
	
	segundo1 = int(input("digite um numero em segundos "))
	
	dia = segundo1//(3600*24)
	segundo = segundo1%(3600*24)
	
	hora = segundo//(3600)
	segundo = segundo%(3600)
	
	minuto = segundo//60
	segundo = segundo%60

	print(segundo1, "segundos = ", dia, " dias, ", hora, " horas, ", minuto, " minutos, ", segundo, " segundos")	
	
	n = int(input("n = "))
	fat = 1
	if n == 0:
		fat = 1
		print("n! = ", fat)
	else :
		while n > 0:
			fat = fat*n
			n = n-1
		print("n! = ", fat)
#-------------------------------------------------------
main()