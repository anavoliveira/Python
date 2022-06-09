def isPalindrome(string):
    # Write your code here.
    if len(string) == 1:
        return True
    else:
        tamanho = len(string)
        print(tamanho)
        for i in range(0, int(tamanho/2)):
            print(string[i], string[tamanho-1-i])
            if string[i]!= string[tamanho-i-1]:
                return False
    return True

if __name__ == '__main__':
    
    assert True == isPalindrome('a')
    assert False == isPalindrome('ab')
    assert False == isPalindrome('abbc')
    assert True == isPalindrome('abcdcba')
    assert True == isPalindrome('abcdefghhgfedcba')