"""
if --> se
a condição só vai ser execultada se a sentença for verdadeiro
else --> se não / caso contrario
"""
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode beber a vontede")
    if idade >= 21:
        print("Você é V.I.P")
else:
    print("Você só pode beber refrigerante")
