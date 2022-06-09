def caesarCipherEncryptor(string, key):
     
    string2 = ''
    for letra in string:
        codigo = ord(letra) + key
          
        while codigo>122:
            codigo = codigo-26

        nova_letra = chr(codigo)
        string2 = string2 + nova_letra
    
    return string2

if __name__ == "__main__":
    print(caesarCipherEncryptor('abc', 52))
