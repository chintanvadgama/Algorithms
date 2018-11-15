class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        dq = []
        for ch in s:
            if ch and not ch.isalnum():
                dq.append(ch)
        print dq
Solution().isPalindrome('A man, a plan, a canal: Panama')