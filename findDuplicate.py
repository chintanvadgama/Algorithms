class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = {}
        duplicates = []
        for num in nums:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1
        for k,v in lookup.items():
            if v > 1:
                return k

    def findDuplicateAlgo(self,nums):
        if len(nums) == 1:
            return None
        if len(set(nums)) == 1 and len(nums) != 1:
            return nums[0]

        duplicate = None
        # duplicate = None



print(Solution().findDuplicateAlgo([1,3,4,2,6,2]))