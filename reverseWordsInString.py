"""
6. Reverse Words in a String
Code it now: https://oj.leetcode.com/problems/reverse-words-in-a-string/ Difficulty: Medium, Frequency: High Question:
Given an input string s, reverse the string word by word.
For example, given s = "the sky is blue", return "blue is sky the".
Example Questions Candidate Might Ask:
Q: What constitutes a word?
A: A sequence of non-space characters constitutes a word.
Q: Does tab or newline character count as space characters?
A: Assume the input does not contain any tabs or newline characters.
Q: Could the input string contain leading or trailing spaces?
A: Yes. However, your reversed string should not contain leading or trailing spaces.
Q: How about multiple spaces between two words?
A: Reduce them to a single space in the reversed string.
"""


def reverse_words_in_string(source):
    if source and len(source) == 1:
        return source
    elif source:
        reverse_string = source.split(' ')
        reverse_string.reverse()
        return ' '.join(reverse_string)
        # for i in range(len(source)):
        #     if source[i] == ' ':
        #         j = i
        #         print 'j (%s) i (%s)' %(j,i)
        #     elif i==0 or source[i-1] == ' ':
        #         if len(reverse_string) != 0:
        #             reverse_string.append(' ')
        #         reverse_string.append(source[i:j])
        # print reverse_string

# time complexity : O(n)
# Remove
def test(input):
    if input == ' ':
        print 'going'
        return input.strip()

def rev_words_in_string(source,debug=False):
    if source and len(source) == 1:
        return source
    elif source:
        i=0
        string_list = []
        for j in range(len(source)):
            if source[j] == ' ' and j != 0:
                string_list.append(source[i:j])
                if debug:
                    print 'i --> %s, j --> %s' %(i,j)
                i = j
                if debug:
                    print 'After (i=j) i --> %s, j --> %s' %(i,j)
            elif source[j] != ' ' and j == len(source)-1:
                string_list.append(source[i:j+1])
        string_list = [x.strip(' ') for x in string_list]
        string_list.reverse()
        return ' '.join(string_list)


class Solution(object):
    # Reverse words in string
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if ' ' not in s:
            return s[::-1]
        stack = []
        j = 0
        for i in range(len(s) - 1):
            if s[i] == ' ' and (i != 0):
                stack.append(s[j:i].strip())
                j = i
            elif s[i] != ' ' and i == len(s) - 1:
                stack.append(s[j:i+1].strip())
        stack.append(s[j:len(s)].strip())
        print stack
        return ' '.join([i for i in stack[::-1] if i])





print(Solution().reverseWords('chitnan is good'))

print(Solution().reverseWords('       '))



#print reverse_words_in_string('the sky is blue')
# print test(input=' ')
# print rev_words_in_string('the sky is blue')
# print rev_words_in_string(' the sky is blue ')
# print rev_words_in_string('the sky is blue ')
# print rev_words_in_string(' the sky is blue')
# print rev_words_in_string('  the sky is blue')
# print rev_words_in_string('  a1213  ')