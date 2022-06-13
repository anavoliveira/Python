def findThreeLargestNumbers(array):
    if len(array) == 3:
        return sorted(array)
    else:
        n1=-100000
        n2=-100000
        n3=-100000
        for num in array:
            if num > n1:
                n3=n2
                n2=n1
                n1 = num
            elif num> n2:
                n3=n2
                n2 = num
            elif num > n3:
                n3=num

        return sorted([n1,n2,n3])
            


if __name__ == '__main__':
    assert [10,10,12] == findThreeLargestNumbers([10,12,10])
    assert [10,10,12] == findThreeLargestNumbers([10,12,10,5])
    assert [10,10,12] == findThreeLargestNumbers([10,5,9,10,12])
    assert [-2,-1,7] == findThreeLargestNumbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7])  