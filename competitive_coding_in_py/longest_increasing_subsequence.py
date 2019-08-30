"""
A subsequence is a sequence that can be derived from another sequence,
by deleting some elements without changing the order of the remaining elements.
"""
import sys

INT_MIN = -sys.maxsize - 1 


def findLongestIncreasingSubsequence(arr):
    length = len(arr)
    auxArr = [1] * (length)
    for i in range(1,length):
        for j in range(i):
            if arr[j] < arr[i] and auxArr[j]+1 > auxArr[i]:
                auxArr[i] = auxArr[j] + 1
    ans = INT_MIN    
    # find max
    for k in auxArr:
        if k > ans:
            ans = k

    return ans

# output should be 5
print(findLongestIncreasingSubsequence([1, 2, 3, -1, -1, 5, 0, 9]))
