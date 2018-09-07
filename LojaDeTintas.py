# -*- coding: utf-8 -*-
a = int(input("informe a area a ser pintada: "))
l = a // 6
if a % 6 > 0:
    l = l + 1
L = l//18
if l % 18 > 0:
    L = L + 1
Pl = L*80
g = l//4
if l % 4 > 0:
    g = g + 1
Pg = g*25
print ("\nSe você quiser comprar em latas, vai precisar de",L,"lata(s)")
print ("o Preço da(s) lata(s) vai(ão) sair de: R$",Pl,",00")

print ("\nSe você quiser comprar em galões, vai precisar de",g,"galão(ões)")
print ("o Preço do(s) galão(ões) vai(ão) sair de: R$",Pg,",00")

L2 = l // 18
g2 = ( l % 18 ) // 4
if  (l % 18 ) % 4 > 0:
    g2 = g2 + 1
Pg2 = g2*25
Pm = (l // 18)*80 + Pg2

print ("\nSe quiser misturar latas e galões")
print ("vai precisar de",L2,"lata(s) e",g2,"galão(ões)")
print ("o preço sairá de R$",Pm,",00")
