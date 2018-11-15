# Use slow and fast pointers
class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0
        for fast in range(1, len(nums) - 1):
            if nums[fast] != nums[slow]:
                nums[fast] = nums[slow]
                slow += 1
        nums[slow] = nums[len(nums) - 1]
        print nums[:slow]


Solution().removeDuplicates([1, 1, 2])
