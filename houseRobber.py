class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        i = 0
        j = 1
        summation = 0
        sums = []
        memo = {}
        for i in range(0,len(nums) ):
            for j in range(1,len(nums) ):
                print("nums[%s]=%s,nums[%s]=%s" % (i,nums[i],j,nums[j]))
                if j == i+1 or j == i-1:
                    i = 0
                    j = 1
                else:
                    summation = summation + nums[i] + nums[j]
            print summation
            summation = 0

        print sums


print(Solution().rob([2,1,1,2]))