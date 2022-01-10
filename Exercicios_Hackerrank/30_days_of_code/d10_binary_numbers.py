#!/bin/python3

import math
import os
import random
import re
import sys

def converte_para_binario(numero):
    quociente = numero
    numero_binario = ''

    while quociente>0:
        quociente = math.floor(numero/2)
        resto = str(numero%2)

        numero_binario += resto
        numero=quociente

    return numero_binario[::-1]

def encontra_maior_sequencia_de_uns(numero_binario):
    todas_sequencias= ['0', '0']
    sequencia=0
    for i in numero_binario:
        if i=='1': 
            sequencia += 1
        else:
            todas_sequencias.append(sequencia)
            sequencia=0

    todas_sequencias.append(sequencia)

    print(max(todas_sequencias, key=int))


if __name__ == '__main__':
    
    n = int(input().strip())

    numero_binario = converte_para_binario(n)
    encontra_maior_sequencia_de_uns(numero_binario) 


        
    