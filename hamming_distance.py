# coding=utf-8
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = format(x,'b')
        bin_y = format(y,'b')

        # Zero padding
        len_diff = len(bin_x) - len(bin_y)
        print(len_diff)
        if len(bin_x) > len(bin_y):
            bin_y = '0' * (len(bin_x) - len(bin_y)) + bin_y
        else:
            bin_x = '0' * (len(bin_y) - len(bin_x)) + bin_x

        hamming_distance = 0
        low = 0
        high = len(bin_x)
        for i in range(low,high):
            if bin_x[i] != bin_y[i]:
                hamming_distance += 1
        return hamming_distance


print(Solution().hammingDistance(1,4))

