# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# Example 1:
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:
#
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

# solution -> 1. Iterate through list if the list[i+1] - list[i] != 1 increment counter

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output = []
        if not nums:
            return []
        var = nums[0]
        isConsecutive = True
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] != 1:
                isConsecutive = False
                if var == nums[i]:
                    ran = "%s" %(nums[i])
                else:
                    ran = "%s->%s" % (var,nums[i])
                var = nums[i+1]
                output.append(ran)
            else:
                isConsecutive = True
                continue
        if isConsecutive and var != nums[len(nums)-1]:
            output.append('%s->%s' %(var,nums[len(nums)-1]))
        elif var == nums[len(nums)-1]:
            output.append('%s' % var)
        return output
        # if var == nums[len(nums) - 1]:



Solution().summaryRanges([0,1,2,4,5,7])
Solution().summaryRanges([0,2,3,4,6,8,9,10])
print Solution().summaryRanges([-1])

print Solution().summaryRanges([])