import sys

INT_MAX = sys.maxsize

"""
 * Given an array of non-zero integers reach the end with minimum number of steps with atmost number of steps from i = a[i]
 * If a[i] equals 0 it can't move.
"""

arr = [1, 2, 3, 4, 5, 6]
length = len(arr)

max = INT_MAX
auxArr = [0,max,max,max,max,max]

def findMinSteps(arr):
    min = 0
    for i in range(1, length):
        for j in range(length):
            if i-j <= arr[j] and (auxArr[j] + 1 < auxArr[i]): 
                auxArr[i] = auxArr[j]+1


findMinSteps(arr)

if (auxArr[length-1] == max):
    print('bruh, no solution for this.')
else:
	print(auxArr[length-1])
