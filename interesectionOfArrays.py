def intersection(arr1,arr2):
	map_dict = {}
	result =[]
	for a in arr1:
		if a not in map_dict:
			map_dict[a] = 1
		else:
			map_dict[a] += 1

	for a in arr2:
		print map_dict
		if a in map_dict and map_dict[a] > 0:
			result.append(a)
			map_dict[a]-=1
		print 'after',map_dict


	print result


class Solution(object):
	def intersection(self, nums1, nums2):
		"""
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
		if nums1 == nums2:
			return nums1
		lookup = {}
		result = []
		for num in nums1:
			if num in lookup:
				lookup[num] += 1
			else:
				lookup[num] = 1
		print(lookup)
		for num in nums2:
			if num in lookup and lookup[num] > 0:
				result.append(num)
				lookup[num] -= 1
		return list(set(result))

print(Solution().intersection([1,2,2,1],[2,2]))
print(Solution().intersection([4,9,5],[9,4,9,8,4]))