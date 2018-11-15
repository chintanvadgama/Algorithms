# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0 
        for i in range(len(nums)):
        	if nums[i] != 0:
        		nums[j] = nums[i]
        		j+=1
       	print 'j',j
       	print nums
        while j < len(nums):
        	nums[j] = 0
        	j += 1
        # print nums

Solution().moveZeroes( [0,1,0,3,12])
Solution().moveZeroes( [0,1])
