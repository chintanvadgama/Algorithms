class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        low = 0
        high = len(nums) - 1
        print nums[0]
        for j in range(low,high + 1):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


# print(Solution().removeElement([3,2,2,3],3))
print(Solution().removeElement([3,2,2,3],3))

