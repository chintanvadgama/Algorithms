# coding=utf-8
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
Have you considered these scenarios?
   i.
ii. iii.
iv. v.
Below is a
needle or haystack is empty. If needle is empty, always return 0. If haystack is empty, then there will always be no match (return –1) unless needle is also empty which 0 is returned.
needle’s length is greater than haystack’s length. Should always return –1. needle is located at the end of haystack. For example, “aaaba” and “ba”. Catch
possible off-by-one errors.
needle occur multiple times in haystack. For example, “mississippi” and
“issi”. It should return index 2 as the first match of “issi”.
Imagine two very long strings of equal lengths = n, haystack = “aaa...aa” and needle = “aaa...ab”. You should not do more than n character comparisons, or else your code will get Time Limit Exceeded in OJ.
"""

def needle_haystack()

