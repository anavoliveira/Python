class Difference():
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.diferencas = []
        numero_elementos = len(self.__elements)

        for i in range(0, numero_elementos):
            for j in range(i+1, numero_elementos):
                diferenca = self.__elements[i]-self.__elements[j]
               
                self.diferencas.append(abs(diferenca))
               
        self.maximumDifference =  max(self.diferencas, key=int)
        
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)