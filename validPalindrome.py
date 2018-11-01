"""
4. Valid Palindrome
Code it now: https://oj.leetcode.com/problems/valid-palindrome/ Difficulty: Easy, Frequency: Medium
Question:
Given a string, determine if it is a palindrome, considering only alphanumeric characters
and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Example Questions Candidate Might Ask:
Q: What about an empty string? Is it a valid palindrome?
A: For the purpose of this problem, we define empty string as valid palindrome.
"""


def check_valid_palindrome(string):
    if string:
        if len(string) == 1:
            print 'String %s is a valid palindrome' % string
            return
        else:
            string = [x.lower() for x in string]
            i = 0
            j = 0

            while i <= j:
                while i < j and not string[i].isalnum():
                    i+=1
                while i < j and not string[j].isalnum():
                    j-=1
                if i <= j:
                    if string[i] != string[j]:
                        return False
                    else:
                        i +=1
                        j -=1
                if i > j:
                    return True


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s =s.lower()
        dq = []
        for ch in s:
            if ch and ch.isalnum():
                dq.append(ch)
        left = 0
        right = len(dq)-1
        while left < right and len(dq) > 1:
            first = dq.pop(0)
            last = dq.pop()
            if first != last:
                return False
        return True
        

print Solution().isPalindrome('A man, a plan, a canal: Panama')

# print check_valid_palindrome('race a car')
# print check_valid_palindrome('A man, a plan, a canal: Panama')
# print check_valid_palindrome('A man, a plan, a canal: P')


# arr = [1,3, 10, 20, 35, 51, 55, 67]
# intNumber  = 10
