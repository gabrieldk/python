"""
trabalho quetao 01:
"""
from ModelarNumComplexo import NumComplexo

def main ():

    a = int(input("parte real: "))
    b = int(input("parte imaginaria: "))

    complexo = NumComplexo (a, b)

    complexo.ImprimirNum()
    complexo.Equal()
    complexo.Soma()
    complexo.Subtrai()
    complexo.Multiplica()
    complexo.Divide()
    complexo.Ecomplexo()
    complexo.Nulo()

main()