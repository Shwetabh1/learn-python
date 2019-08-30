"""
 * Given an array arr[], find a Noble integer in it. 
 * An integer x is said to be Noble in arr[] if the number of integers greater than x are equal to x. 
 * If there are many Noble integers, return any of them. If there is no, then return -1.
 * Implementation using Sorting
 * I have also uploaded another implementation using TreeSet. Do check it out.
"""

def findNobleInteger(arr):
	arr.sort()
	siz = len(arr)
	ans = False

	for i in range(siz):
		if i < siz-1 and arr[i] == arr[i+1]:
			continue
		if arr[i] == siz-i-1:
			ans = True
			break
	if ans or arr[siz-1] == 0:
	   print(arr[i])
	else:
		print("Ain't No Answer")
		
findNobleInteger([-1, -2, -3, 0, 0, 0,1])
findNobleInteger([1,2,3,4,5])