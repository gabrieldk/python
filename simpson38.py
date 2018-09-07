#!-*- conding: utf8 -*-
#coding: utf-8

def simpson38(f, xi, xe, n):
    """
    Numerical integration using the Simpson 3/8 Rule.
 
    integral = simpson38(f, xi, xe, n=10000)
 
    INPUT:
      * f: function to be integrated
      * xi: beginning of integration interval
      * xe: end of integration interval
      * n: number of interval divisions
 
    return: \int_{xi}^{xe} f(x)
 
    Author: Pedro Garcia [sawp@sawp.com.br]
    see: http://www.sawp.com.br
 
    License: Creative Commons
             http://creativecommons.org/licenses/by-nc-nd/2.5/br/
 
    Jul 2012
    """
    h = float(xe - xi) / n #tamanho do intervalo
    
    s = lambda i: i % 3 == 0 #testa se o numero e divisivel por 3 ou n, retorna erdadeiro ou falso
    
    fxi = lambda i: f(xi + i * h) #vai calcular os f's 
    
    g = lambda i: s(i) * (2.0 * fxi(i)) + (not s(i)) * (3.0 * fxi(i))
    
    """
    nessa g:
    	se i for divisível por 3 então ele vai fazer 2*fxi
    	caso contrário ela vai fazer 3*fxi
    """
    
    sumatory = sum(map(g, xrange(1, n)))#map aplica a função g em cada elemento gerado pela xrange
    
    integral = (fxi(0) + sumatory + fxi(n)) * (3.0 * h / 8.0)#formula geral da regra de simpson3/8
    
    return integral

def main():

	print(simpson38(lambda x:x**5, 0.0, 10.0, 2))       
	print(simpson38(lambda x:x**5, 0.0, 10.0, 100000))  

	print(simpson38(lambda x:x**8, 0.0, 10.0, 2))       
	print(simpson38(lambda x:x**8, 0.0, 10.0, 100000))  

main()


"""

REFERENCIAS:
e o livro
https://wiki.python.org/moin/ForLoop
http://www.sawp.com.br/blog/?p=1638

"""