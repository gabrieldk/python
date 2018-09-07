# PROGRAMA: CAIXA DE BANCO

x = 1
y = 5
z = 10
w = 50
k = 100

s = int(input("Quanto o senhor deseja sacar? "))

if 10 <= s <= 600:
    n1 = s // k #quantidade de notas de 100
    n2 = (s % k) // w #quantidade de notas de 50
    n3 = ((s % k) % w ) // z #quantidade de notas de 10
    n4 = (((s % k) % w ) % z) // y #quantidade de notas de 5  
    n5 = ((((s % k) % w ) % z) % y) // x #quantidade de notas de 1
    if n1 > 0:
        print("Serão fornecidas",n1,"nota(s) de R$ 100,00")
    if n2 > 0:
        print("Serão fornecidas",n2,"nota(s) de R$ 50,00")
    if n3 > 0:
        print("Serão fornecidas",n3,"nota(s) de R$ 10,00")
    if n4 > 0:
        print("Serão fornecidas",n4,"nota(s) de R$ 5,00")
    if n5 > 0:
        print("Serão fornecidas",n5,"nota(s) de R$ 1,00")

else:
    print("Você não pode sacar esse valor")


