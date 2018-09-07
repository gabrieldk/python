"""
Faça um programa para loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da area a ser pintada
Considere que a corbertura da tinta é de 1 litro para cada 3 metros quadrados
e q a tinta é vendida em latas de 18 litros, custam R$ 80,00.

Informe ao usuário a quantidade de latas de tinta
a serem compradas e o preço total.
"""
a = int(input(" Qual o tamanho da area q o senhor deseja pintar(em m²)?: "))
l = a//3
if a % 3 > 0:
    l = l + 1
L = l//18
if l % 18 > 0:
    L = L + 1
p = L*80

print ("Você precisará de",L,"latas")
print ("Total a pagar: R$",p,",00")

#  o sinal de porcentagem (%) indica resto 
#  exemplo:
#    8 % 7
#    ler-se: o resto da divisão de 8 por 7
