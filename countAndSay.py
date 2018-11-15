class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        output = ""
        count = 1
        for i in range(len(n)-1):
            if n[i+1] == n[i]:
                count +=1
            else:
                output = output + str(count) + n[i]
                count = 1
        output = output + str(len(n)-1) + n[len(n)-1]
        print output
        return output

Solution().countAndSay('555512122221')
