#!/bin/python3

import math
import os
import random
import re
import sys


#Temos duas funçoes, uma que calcula os limite da ampulheta em questao e outra que realiza a soma dos 
#valores da ampulheta

def calcula_ampulheta(limite_esquerdo, limite_direito, limite_superior, limite_inferior, arr ):
    
    avaliador = 0   # serve para especificar quais valores serao somados nao
                    # considerando uma matriz 0 1 2  os valores 3 e 5 nao serao somados
                    #                         3 4 5
                    #                         6 7 8
    soma = 0      # somatorio dos valores da ampulheta
    

    for i in range(limite_superior, limite_inferior+1):
        for j in range(limite_esquerdo, limite_direito+1):
            if avaliador!=3 and avaliador!=5:
                soma +=  arr[i][j]
            avaliador +=1

    return soma

def gera_limites(arr):

    limite_esquerdo=0-3
    limite_direito=2-5
   
    limite_superior=0-3
    limite_inferior=2-5

    soma_total=[]

    for i in range(0,4):
        limite_superior = i
        limite_inferior= i+2
        
        for j in range(0,4):
            limite_esquerdo = j
            limite_direito = j+2

            soma_total.append( calcula_ampulheta(limite_esquerdo, limite_direito,
                                                 limite_superior, limite_inferior, arr))

    return soma_total

if __name__ == '__main__':

    arr = []

    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(max(gera_limites(arr), key=int))

