# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         stack = []
#         balanced = True
#         idx =0
#         while idx < len(s) and balanced:
#         	if s[idx] in '[(<{':
#         		stack.append(s[idx])
#         	else:
#         		if len(stack) == 0:
#         			balanced = False
#         		else:
#         			symbol = stack.pop()
#         			if symbol in '])>}':
#         	idx = idx+1
#        	if balanced and len(stack) ==0:
#        		return True
#        	else: 
#        		return False

def matches(s1,s2):
	openers = '[(<{'
	closers =  '])>}'
	open_idx =0
	close_idx=0

class Solution2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {
        			'[':']',
        			'{':'}',
        			'(':')',
        			'<':'>'
        			}

        ch_counts = {}
        balanced = True
        for ch in s:
        	if ch in ch_counts:
        		ch_counts[ch] +=1
        	else:
        		ch_counts[ch] = 1
        print ch_counts
        for ch,count in ch_counts.items():
        	if ch in lookup:
        		opening_bracket_cnt = count
        		closing_bracket = lookup[ch]
        		if closing_bracket not in ch_counts:
        			return False
        		else:
        			closing_bracket_cnt = ch_counts[closing_bracket]
        			if opening_bracket_cnt != closing_bracket_cnt:
        				balanced = False
        return balanced

class Solution(object):
    def isValid(self, s):
        # print len(s)
        # if len(s) % 2 == 1: return False
        dic = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for char in s:
            if char in dic:   
                stack.append(char)
            else:
                if not stack or dic[stack.pop()] != char:
                    return False
        print stack
        return not stack

# print Solution().isValid('[chintan]')
print Solution().isValid('[c]')
