def runLengthEncoding(string):
    encoding = ''
    count = 1
    caracter_anterior = string[0]
    caracter = ''

    for posicao, caracter in enumerate(string[1:]):
        if caracter_anterior == caracter:
            count+=1
        else: 
            if count>=9:
                while count>9:
                    encoding = encoding + f'9{caracter_anterior}'
                    count = count-9
               
            encoding = encoding + f'{count}{caracter_anterior}'
            caracter_anterior = caracter
            count=1

    if count>=9:        
        while count>9:
            encoding = encoding + f'9{caracter_anterior}'
            count = count-9

    encoding = encoding + f'{count}{caracter_anterior}'
    return encoding


if __name__ == '__main__':
    print(runLengthEncoding('************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA'))
    