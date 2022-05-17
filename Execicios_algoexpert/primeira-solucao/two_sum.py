def twoNumberSum(array, targetSum):
    
    arr_target = []
    tam= len(array)
    print(arr_target)
    for i in range(0, tam):
        for j in range (i+1, tam):
            if ((array[i]+array[j]) == targetSum):
                print( f"teste: {array[i]} + {array[j]} = {targetSum}")
                arr_target.append(array[i])
                arr_target.append(array[j])
            
            
	
    return arr_target

if __name__ == '__main__':
    print(twoNumberSum([1,2,3,4,5], 6))