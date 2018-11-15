"""
Question:
Given an array of integers, find two numbers such that they add up to a specific target
number.
The function twoSum should return indices of the two numbers such that they add up to
the target, where index1 must be less than index2. Please note that your returned answers
(both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
"""


def find_target_sum(listOfInt,target):
    # O(n**2)
    if listOfInt and len(listOfInt) == 1:
        print 'Only one element in the list'
        return
    else:
        pairs = []
        for i in listOfInt:
            var = target - i
            if var in listOfInt:
                pairs.append((listOfInt.index(var),listOfInt.index(i)))
        return set(pairs)


def find_target_sum_dict(listOfInt,target):
    # 1. Use dictionary to store the {element:index}
    map = {}
    for ele in listOfInt:
        map[ele] = listOfInt.index(ele)

    # 2. find target-ele in keys of dict
    pairs = []
    for ele in listOfInt:
        complement = target-ele
        if complement in map:
            pairs.append((listOfInt.index(complement),
                          listOfInt.index(ele)))
    return set(pairs)

class Solution(object):
    def twoSum(self,listOfInt,target):
        if len(listOfInt) < 2:
            return 0
        low = 0
        high = len(listOfInt) - 1
        while (listOfInt[low] + listOfInt[high]) != target:
            if listOfInt[low] + listOfInt[high] < target:
                low += 1
            else:
                high -= 1
        return [low+1, high+1]


print(Solution().twoSum([0,0,3,4],0))
print(Solution().twoSum([2, 7, 11, 15],9))
