class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Remove leading and trailing whitespaces
        s = s.strip()
        if not s:
            return ''
        if ' ' not in s:
            return s[::-1]
        stack = []
        for word in s.split():
            stack.append(word[::-1])
        return ' '.join(stack)


print(Solution().reverseWords("Let's take LeetCode contest"))