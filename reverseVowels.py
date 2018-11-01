class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        low = 0
        high = len(s) - 1
        s = list(s)
        while low < high:
            if s[low] in vowels and s[high] in vowels:
                s[low],s[high] = s[high],s[low]
                low += 1
                high -= 1
            elif s[low] not in vowels:
                low += 1
            elif s[high] not in vowels:
                high -= 1
        return ''.join(s)


#chantin
print(Solution().reverseVowels("chintan"))