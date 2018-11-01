# coding=utf-8
#Question
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
def reverse_integer(num):
    if num < -2**31 or num > (2**31-1):
        return 0
    if len(str(num)) == 1:
        return num
    else:
        if num < 0:
            # Negative Numbers
            rev = str(num)[1:][::-1]
            return int('-'+rev)
        else:
            # Positive Numbers
            return int(str(num)[::-1])


if __name__ == '__main__':
    print reverse_integer(123)
    print reverse_integer(9)
    print reverse_integer(0)
    print reverse_integer(-123123124)
    print reverse_integer(120)
    print reverse_integer(1534236469)


