class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if not s:
            return 0
        if s in lookup:
            return lookup[s]
        # All characters are same
        if len(set(s)) == 1:
            return lookup[s[0]] * len(s)

        numeric = 0

        for i in range(0,len(s) - 1):
            if lookup[s[i]] < lookup[s[i+1]]:
                numeric -= lookup[s[i]]
            else:
                numeric += lookup[s[i]]
            # print 's[%s] = %s, numeric = %s' % (i,s[i],numeric)
        # numeric += lookup[s[len(s) - 1]]
        return numeric + lookup[s[-1]]


if __name__ == '__main__':
    print Solution().romanToInt('III')