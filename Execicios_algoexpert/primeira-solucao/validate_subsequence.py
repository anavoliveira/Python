def isValidSubsequence(array, sequence):
    position = 0
    quantos_encontrei =0 
    for i in range(0, len(sequence)): 
        for j in range(position, len(array)):
            if sequence[i] == array[j]:
                position=j+1
                quantos_encontrei+=1
                # print(f'elemento{i} {sequence[i]} = elemento{j}{array[j]} na posicao {position} quantos encontrei {quantos_encontrei}')
                break
                
    if quantos_encontrei == len(sequence):   
        return True
    else:
        return False
        


if __name__ == '__main__':
    print(isValidSubsequence([1, 1, 6, 1], [1, 1, 1, 6]))