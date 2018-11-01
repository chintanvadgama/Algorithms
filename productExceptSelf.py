class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return []
        if len(set(nums)) == 1 and len(nums) != 1:
            return [1*pow(nums[0],len(nums)-1) for i in nums]

        low = 0
        high = len(nums) - 1
        product = [1]*len(nums)
        print product



Solution().productExceptSelf([1,2,3,4])

