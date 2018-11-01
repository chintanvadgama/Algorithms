#Given a non-empty array of integers, every element appears twice except for one. Find that single one.#

#Note:#

#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?#

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = {}
        for num in nums:
            if num in lookup:
                lookup[num]+=1
            else:
            	lookup[num]=1
        for k,v in lookup.items():
        	if v ==1:
        		return k

# WithOut Extra Memory
# Bit Operation

# class Solution(object):
#     def singleNumber(self, nums):
#         if len(nums) == 1:
#             return nums[0]
#         if len(set(nums)) == 1 and len(nums) != 1:
#             return []
#         found = None
#         nums = sorted(nums)
#         for i in range(len(nums) - 1):
#             if nums[i] == nums[i+1]:



print Solution().singleNumber([4,1,2,1,2])