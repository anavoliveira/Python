def firstNonRepeatingCharacter(string):
    for posicao, valor in enumerate(string):
       auxiliar = string[:posicao] + string[posicao+1:]
       if (auxiliar.find(valor))<0 :
           return posicao

    return -1


if __name__ == "__main__":
    print(firstNonRepeatingCharacter('aaaaab'))