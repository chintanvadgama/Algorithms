# Python quick sort
import datetime
def quickSort(arr):
	less = []
	equal = []
	greater = []
	if len(arr) > 1:
		pivot = arr[0]
		for ele in arr:
			if ele < pivot:
				less.append(ele)
			if ele > pivot:
				greater.append(ele)
			if ele == pivot:
				equal.append(ele)
		return sorted(less) + equal + sorted(greater)
	else:
		return arr

arr = [12,1231,12321,1433,1230,7593,1281121,37]
start = datetime.datetime.now()
print quickSort(arr)
print 'quick sort time taken ', datetime.datetime.now() - start
start = datetime.datetime.now()
print sorted(arr)
print 'quick sort time taken ', datetime.datetime.now() - start
