class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        if len(set(nums)) == 1 and len(nums) != 1:
            return set(nums)
        low = 0
        high = len(nums) - 1
        for i in range(low,high):
            print("nums[%s]=%s,nums[%s]=%s,nums[%s]=%s" %(i,nums[i],i+1,nums[i+1],i+2,nums[i+2]))
            if nums[i+1] < nums[i]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
            elif nums[i+2] > nums[i+1]:
                nums[i+2],nums[i+1] = nums[i+1],nums[i+2]
            else:
                i -= 1
            print nums
        return nums


print Solution().wiggleSort([1, 5, 1, 1, 6, 4])
