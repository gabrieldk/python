#!-*- conding: utf8 -*-
#coding: utf-8
def myrange(start, end, step):#essa função vai gerar uma lista com os valores que se encontram no intervalo

    while start <= end:
        yield start
        start += step

def simpson38 (f, a, b, n):
	h = float (b-a)/n

	fxi = lambda i: f(a + i*h)#encontrar o f de cada ponto dentro do intervalo

	somatorioI = sum(map(fxi, myrange(2,n-1,3)))
	somatorioI1 = sum(map(fxi, myrange(3,n-1,3)))
	somatorioJ = sum(map(fxi, myrange(4,n-2,3)))

	somaTotal = 3*(somatorioI + somatorioI1) + 2*somatorioJ

	integral = (3*h/8)*(f(a) + somaTotal + f(b))

	return integral

def main ():
	print(simpson38(lambda x:x**3, 0.0, 10.0, 3))       #2361.11111111
	print(simpson38(lambda x:x**3, 0.0, 10.0, 100000))  #2500.0

	print(simpson38(lambda x:x**4, 0.0, 10.0, 3))       #19907.4074074
	print(simpson38(lambda x:x**4, 0.0, 10.0, 100000))  #20000.0

main()
"""
REFERENCIAS:
Gilat, A.; Subramaniam, V. Métodos Numéricos para Engenheiros e Cientistas:Uma introdução com aplicações usando  o MATLAB.
Porto Alegre: ARTMED EDITORA S.A. 2008

For Loops - Python Wiki. Disponivel em:
<https://wiki.python.org/moin/ForLoop> Acesso em: 14 jun. 2018

Integração Numérica — Regras de Simpson. Disponivel em:
<http://www.sawp.com.br/blog/?p=1638> Acesso em: 14 jun. 2018
"""