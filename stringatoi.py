# Author: Chintan Vadgama
# To convert the string to integer value
import sys
"""
1. Check for signs in first place
2. If string starts with whitespaces then after whitespace the first letter should be sign +/-
3. if whitespaces inside string then return error
4. i
"""
max_val = 2**31 - 1
min_val = - 2**31 -1

def convert_string_to_number(string):
    sign = 1
    for ltr in string:
        if ltr and ltr == '+':
            sign = 1
        elif ltr and ltr == '-':
            sign = -1

    num = 0
    for ltr in string:
        if ltr and ltr.isdigit():
            num = num * 10 + int(ltr)
    return num * sign


print convert_string_to_number('+1234') #s
print convert_string_to_number('-1234') #s
print convert_string_to_number('1234') #success
print convert_string_to_number('1 234') #error
print convert_string_to_number('1+234') #error
print convert_string_to_number('xsasd112') #error


