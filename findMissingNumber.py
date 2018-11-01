class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sumOfn = n * (n+1) // 2
        array_sum = sum(nums)
        return sumOfn-array_sum
print Solution().missingNumber([3,0,1])
print Solution().missingNumber([9,6,4,2,3,5,7,0,1])
