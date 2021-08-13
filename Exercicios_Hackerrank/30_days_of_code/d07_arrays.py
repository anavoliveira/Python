import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    tamanho = len(arr)
    
    while(tamanho)>0:
        print(arr[tamanho-1], end=' ')
        tamanho -= 1