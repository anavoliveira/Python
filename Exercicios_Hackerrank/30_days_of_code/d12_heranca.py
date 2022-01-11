class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, notas):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.notas = notas

    def calculate(self):
        soma = 0
        quant_notas = 0

        for nota in self.notas:
            soma+= nota
            quant_notas+=1

       
        return gera_notas(soma/quant_notas)


def gera_notas( media):
    
    if media>=90 and media<=100:
        return 'O'
    elif media>=80:
        return 'E'
    elif media>=70:
        return 'A'
    elif media>=55:
        return 'P'
    elif media>=40:
        return 'D'
    elif media<40:
        return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]

numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )

s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())