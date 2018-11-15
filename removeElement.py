# slow and fast pointer
class Solution(object):
    def removeElement(self, nums, val):
        slow = 0
        for fast in range(1,len(nums) - 1):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        nums[slow] = nums[len(nums) - 1]
        print nums[:slow]


Solution().removeElement([3,2,2,3],3)