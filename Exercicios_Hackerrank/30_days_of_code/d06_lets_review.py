

S = []

T = int(input().strip())


for i in range(0,T):
    S.append(input())

for palavras in S:
   
    indice = 0
    par = []
    impar = []

    for letras in palavras:
        if(indice%2 != 0):
            par.append(letras)
        else:
            impar.append(letras)
        indice+=1

    print("{} {}".format(''.join(impar), ''.join(par)))
