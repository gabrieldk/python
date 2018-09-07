# COMPARAÇÕES MULTIPLAS
"""
OBS: quando tiver fazendo duas comparações ao mesmo tempo ( ex: a = 3
  1 < a < 2) se umas das condições for falsa ele vai devolver falso
CONCLUSÃO: o false tem a preferencia

OBS: (1 < 3) < 2 --> resultado: True
 -> a primeira sentença (1 < 3) é verdadeira(True)
 True recebe valor = 1 então fica:
  True < 2 --> True

CONCLUSÃO: quando coloca parenteses as comparações são separadas (em duas distintas)
   quando não coloca parenteses são comparações encadeadas

"""

idade = int(input("digite sua idade: "))

if 18 <= idade < 70:
    print("Você pode receber o Benefício")
else:
    print("Você não pode receber o benefício")
    


