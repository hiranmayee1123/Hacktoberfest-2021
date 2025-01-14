#This technique shows how a nested for loop in some problems can be converted to a single for loop to reduce the time complexity.
#Let’s start with a problem for illustration where we can apply this technique – 

#Given an array of integers of size ‘n’.
#Our aim is to calculate the maximum sum of ‘k’ 
#consecutive elements in the array.

#Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4 
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.

import sys

INT_MIN = -sys.maxsize - 1



def maxSum(arr, n, k):
  max_sum = INT_MIN
	for i in range(n - k + 1):
		current_sum = 0
		for j in range(k):
			current_sum = current_sum + arr[i + j]
      max_sum = max(current_sum, max_sum)

	return max_sum

arr = [1, 4, 2, 10, 2,
	3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
