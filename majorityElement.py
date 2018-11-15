class Solution(object):
    def majorityElement(self, nums):
        major = nums[0]
        count = 1
        for i in range(len(nums) - 1):
            if count == 0:
                count += 1
                major = nums[i]
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major


print(Solution().majorityElement([2,2,1,1,1,2,2]))