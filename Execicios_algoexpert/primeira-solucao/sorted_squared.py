def sortedSquaredArray(array):
    for i in range(len(array)):
       array[i] = array[i]*array[i]

    array.sort()
    return array

if __name__ == '__main__':
    print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))