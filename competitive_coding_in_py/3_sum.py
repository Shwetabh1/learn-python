"""
Find all pairs of 3 numbers whose sum is 0
"""
arr1 = [1,1,1,1,1,1,1,1]
arr2 = [1,0,-1,2,-2,3,4,5,6]
arr3 = [999,1000,-1000,0,-1,-998,1]

def find3Sum(array):
    array.sort()
    length = len(array)
    for i in range(length-2):
        lef  = i + 1
        right = length - 1
        x = array[i]
        cunt = 0
        while lef < right:
            if x + array[lef] + array[right] == 0:
                print('Pair:', x, array[lef], array[right])
                break
            elif x + array[lef] + array[right] < 0:  
                lef +=  1
            else: 
                right -= 1

find3Sum(arr1)
find3Sum(arr2)
find3Sum(arr3)