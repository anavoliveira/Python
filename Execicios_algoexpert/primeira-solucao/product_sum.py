def productSum(array):
    soma_total=0 
    deep = 1
    for valor in array:
        if type(valor) == list:
            print(f'{valor}  é uma lista')
            
            soma = lista_aninhada(valor, deep=2)
            soma_total = soma_total + soma
        else:
            print(f'{valor} não é uma lista')
            soma_total += valor
        

    return soma_total


def lista_aninhada (lista, deep):  
    soma_total = 0

    for num in lista:
        if type(num) == list:
            print(f'{num} é uma lista')
           
            soma = lista_aninhada(num, deep+1)
            soma_total = soma_total + soma
        else:
            print(f'{num} não é uma lista')
            soma_total +=num
    return soma_total * deep

if __name__ == '__main__':
    print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
    # print(productSum([5, 2, [7, [-1, 2]]]))