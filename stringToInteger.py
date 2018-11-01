class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return
        ls = list(str.strip()) # Removing leading and trailing whitespaces
        if str[0] == '-':
            sign = -1
        else:
            sign = 1
        if ls[0] in ['-','+']:
            del ls[0]
        ret = i = 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + int(ls[i])
            i += 1
        return max(-2**31,min(sign*ret,2**31))


print Solution().myAtoi('-123')


