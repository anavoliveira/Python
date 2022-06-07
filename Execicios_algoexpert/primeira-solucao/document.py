def generateDocument(characters, document):
    for p, letra in enumerate(document):
    
        posicao = characters.find(letra) 
        print(letra, posicao)

        if posicao >= 0 : 
            characters = characters[:posicao] + characters[posicao+1: ]
            print(characters)
        else: 
            return False
    return True

if __name__== '__main__':
    print(generateDocument('abcabc', 'aabbccc'))