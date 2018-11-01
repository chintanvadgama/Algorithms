# In arr find closest sum
# Sum of two elements - target sum should be minimum
import sys
def findClosestSum(arr,target_sum):
	left = 0
	right = len(arr)-1
	diff =  sys.maxint
	res_l = 0
	res_r = 0
	while (left < right):
		print abs(arr[left]+arr[right]-target_sum)
		if abs(arr[left]+arr[right]-target_sum) < diff:
			res_l = left
			res_r = right
			diff = abs(arr[left]+arr[right]-target_sum)
		elif (arr[left] + arr[right]) > diff:
			right-=1
		else:
			left-=1
	return (res_l,res_r)

print findClosestSum([10, 22, 28, 29, 30, 40],54)