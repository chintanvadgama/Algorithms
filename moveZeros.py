# slow and fast pointers
class Solution(object):
    def moveZeroes(self, nums):
        slow = 0
        for fast in range(1,len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        print slow
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
        print nums

    def moveZeros2(self, nums):
        count = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums += [0] * count
        print nums

Solution().moveZeros2([0,1,0,3,12])
Solution().moveZeroes([0,1,0,3,12])