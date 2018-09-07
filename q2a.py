from random import randint
from math import sqrt
from math import log
def main():

	a = randint(0,50)
	b = randint(0,50)
	c = randint(0,50)

	lista = [a,b,c]

	k = int(input("insira um número inteiro k: "))
	print("logaritimo de k: %f"%(log(k)))
	print("raiz quadrada de k: %f"%(sqrt(k)))

	d = log(k)
	e = sqrt(k)
	
	lista.append(d)
	lista.append(e)
	
	print(lista)

main()