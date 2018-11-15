# coding=utf-8
"""
9. Valid Number
Code it now: https://oj.leetcode.com/problems/valid-number/
Question:
Validate if a given string is numeric. Some examples:
"0"  true "0.1"  true "abc"  false
Example Questions Candidate Might Ask:
Difficulty: Easy, Frequency: Low
  Q: How to account for whitespaces in the string?
A: When deciding if a string is numeric, ignore both leading and trailing whitespaces.
Q: Should I ignore spaces in between numbers – such as “1 1”?
A: No, only ignore leading and trailing whitespaces. “1 1” is not numeric.
Q: If the string contains additional characters after a number, is it considered valid?
A: No. If the string contains any non-numeric characters (excluding whitespaces and decimal point), it is not numeric.
Q: Is it valid if a plus or minus sign appear before the number? A: Yes. “+1” and “-1” are both numeric.
Q: Should I consider only numbers in decimal? How about numbers in other bases such as hexadecimal (0xFF)?
A: Only consider decimal numbers. “0xFF” is not numeric.
Q: Should I consider exponent such as “1e10” as numeric?
A: No. But feel free to work on the challenge that takes exponent into consideration. (The Online Judge problem does take exponent into account.)
1. => Valid
.1 => Valid
0.1 => valid
121.12 => valid
123.asdsa => not valid
"""


def check_valid_number(num):
    if isinstance(num,str) and num:
        isNumeric = False
        for i in range(len(num)):
            if num.isdigit():
                isNumeric = True
    else:
        print 'Empty String !'
        return


if __name__ == '__main__':
    check_valid_number('')
    print 'Expected => valid'
    print check_valid_number('123')
    print 'Expected => Not '
    print check_valid_number('3.xxxx')
    print 'Expected => valid'
    print check_valid_number('1.')
    print 'Expected => valid'
    print check_valid_number('.1')
    print 'Expected => valid'
    print check_valid_number('123.1234')
    print 'Expected => valid'
    print check_valid_number('+123.1234')

