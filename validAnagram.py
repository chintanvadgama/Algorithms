class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        lookupfors = {}
        lookupfort = {}
        for ch in s:
            lookupfors[ch] = lookupfors.setdefault(ch, 0) + 1

        for ch in t:
            lookupfort[ch] = lookupfort.setdefault(ch, 0) + 1
        return lookupfors == lookupfort


test_strings = [
    {"dog": "god"},
    {"dog": "odg"}
]

for test in test_strings:
    for k, v in test.iteritems():
        response = Solution().isAnagram(k, v)
        print("String1: {0} String2: {1} isAnagram: {2}".format(k, v, response))
