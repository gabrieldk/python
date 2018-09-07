#modelar numero complexo

class NumComplexo(object):

    def __init__ (self, real, imaginaria = 0):
        self.numcomp = complex(real, imaginaria)
    
    def ImprimirNum(self):
        print ("%d + %di"%(self.numcomp.real, self.numcomp.imag))
    
    def Equal(self):
        print ("digite o numero que vai ser comparado\n")

        real2 = int(input("parte real: "))
        imag2  = int(input("parte imaginaria: "))
        
        self.numcomp2 = complex(real2, imag2)

        if self.numcomp == self.numcomp2:
            return print("True")
        
        else:
            return print ("False")
    
    def Soma(self):
        print("insira o numero a ser somado: \n")

        real3 = int(input("parte real: "))
        imag3  = int(input("parte imaginaria: "))

        self.numcomp3 = complex(real3, imag3)
        self.soma = complex(self.numcomp + self.numcomp3)

        print ("(%d + %di) + (%d + %di) = "%(self.numcomp.real, self.numcomp.imag, real3, imag3))
        print ("%d + %di"%(self.soma.real, self.soma.imag))

    def Subtrai (self):
        print("insira o numero a ser subtraido: \n")

        real4 = int(input("parte real: "))
        imag4  = int(input("parte imaginaria: "))

        self.numcomp4 = complex(real4, imag4)
        if self.numcomp == self.numcomp4:
            return print("0")
        
        else:
            self.subit = complex(self.numcomp - self.numcomp4)

        print ("(%d + %di) - (%d + %di) = "%(self.numcomp.real, self.numcomp.imag, real4, imag4))
        print ("%d + %di"%(self.subit.real, self.subit.imag))

    def Multiplica (self):
        print("insira o numero a ser multiplicado: \n")

        real5 = int(input("parte real: "))
        imag5  = int(input("parte imaginaria: "))

        self.numcomp5 = complex(real5, imag5)
        
        self.realmultnumcomp = ((self.numcomp.real * self.numcomp5.real) - (self.numcomp.imag * self.numcomp5.imag))
        self.imagmultnumcomp = ((self.numcomp.real * self.numcomp.imag) + (self.numcomp.imag * self.numcomp5.real))

        print ("(%d + %di) * (%d + %di) = "%(self.numcomp.real, self.numcomp.imag, self.numcomp5.real, self.numcomp5.imag))
        print ("%d + %di"%(self.realmultnumcomp, self.imagmultnumcomp))

    def Divide (self):
        print("insira o numero a ser dividido: \n")

        real6 = int(input("parte real: "))
        imag6  = int(input("parte imaginaria: "))

        self.numcomp6 = complex(real6, imag6)

        self.realdivnumcomp = ((self.numcomp.real * self.numcomp6.real) - (self.numcomp.imag * self.numcomp6.imag)/((self.numcomp6.imag * self.numcomp6.imag) + (self.numcomp6.real * self.numcomp6.real)))
        self.imagdivnumcomp = ((self.numcomp.real * self.numcomp.imag) + (self.numcomp.imag * self.numcomp6.real)/((self.numcomp6.imag * self.numcomp6.imag) + (self.numcomp6.real * self.numcomp6.real)))

        print ("(%d + %di) / (%d + %di) = "%(self.numcomp.real, self.numcomp.imag, self.numcomp6.real, self.numcomp6.imag))
        print ("%d + %di"%(self.realdivnumcomp, self.imagdivnumcomp))

    def Ecomplexo(self):
        if self.numcomp.imag == 0:
            print ("não é complexo, pois a parte imaginaria é zero")
        else:
            print ("é complexo, pois a parte imaginaria não é zero")
    def Nulo(self):
        if self.numcomp.imag == 0 and self.numcomp.real == 0:
            print("numero nulo, não é complexo pois a parte imaginária é zero.")
        else:
            print("numero não nulo.")
