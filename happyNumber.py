class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.squareSum(n)

    def squareSum(self,number):
        sum = 0
        for n in str(number):
            sum += pow(int(n),2)
        if sum == 1:
            return True
        else:
            self.squareSum(sum)


print(Solution().squareSum(19))





