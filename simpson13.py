#!-*- conding: utf8 -*-
#coding: utf-8
def simpson(f, xi, xe, n):
    """
    Numerical integration using the Simpson 1/3 Rule.
 
    integral = simpson13(f, xi, xe, n=10000)
 
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
    h = float(xe - xi) / n
    s = lambda i: i % 2 == 0
    fxi = lambda i: f(xi + i * h)
    g = lambda i: s(i) * (2.0 * fxi(i)) + (not s(i)) * (4.0 * fxi(i))
    sumatory = sum(map(g, xrange(1, n)))
    integral = (fxi(0) + sumatory + fxi(n)) * (h / 3.0)
    return integral
# Demonstrate that the method is exact for polynomials up to 3rd order

print(simpson(lambda x:x**3, 0.0, 10.0, 2))       # 2500.0
print(simpson(lambda x:x**3, 0.0, 10.0, 100000))  # 2500.0

print(simpson(lambda x:x**4, 0.0, 10.0, 2))       # 20833.3333333
print(simpson(lambda x:x**4, 0.0, 10.0, 100000))  # 20000.0