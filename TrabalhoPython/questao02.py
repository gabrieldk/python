#questao 02:


def cripitografar ():

    numero_a_ser_cripitografado = input("insira o numero a ser cripitografado: ")

    a = int((int(numero_a_ser_cripitografado[0]) + 6)%10)

    b = int((int(numero_a_ser_cripitografado[1]) + 6)%10)

    c = int((int(numero_a_ser_cripitografado[2]) + 6)%10)
    
    d = int((int(numero_a_ser_cripitografado[3]) + 6)%10)

    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)

    print ("número cripitografado: ", c+d+a+b)

def descripitografar():
    numero_a_ser_descripitografado = input("insira o numero a ser descripitografado: ")

    a = int(numero_a_ser_descripitografado[0])

    if a >= 6:
        a -= 6
    else:
        a += 4  

    b = int(numero_a_ser_descripitografado[1]) 

    if b >= 6:
        b -= 6
    else:
        b += 4

    c = int(numero_a_ser_descripitografado[2]) 
    
    if c >= 6:
        c -= 6
    else:
        c += 4

    d = int(numero_a_ser_descripitografado[3]) 

    if d >= 6:
        d -= 6
    else:
        d += 4
    
    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)

    print ("número cripitografado: ", c+d+a+b)

def main ():
    
    cripitografar ()
    descripitografar ()

main()

