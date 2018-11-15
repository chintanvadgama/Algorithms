def addNumbers(num1,num2):
    carry = 0
    result = ''
    diff = len(num1) - len(num2)
    if diff > 0:
        num2 = '0'*(len(num1)-len(num2)) + num2
    else:
        num1 = '0'*(len(num2)-len(num1)) + num1

    low = 0
    high = len(num1) - 1
    # print(num1)
    # print(num2)
    for i in range(high,low,-1):
        add = int(num1[i]) + int(num2[i])
        if add >= 10:
            if carry == 1:
                temp = add + carry
                if temp >= 10:
                    result = str(temp)[1] + result
                    carry = 1
                else:
                    result = str(temp) + result
                    carry = 0
            else:
                temp = add
                if temp >= 10:
                    result = str(temp)[1] + result
                    carry = 1
                else:
                    result = str(temp) + result
                    carry = 0
        else:
            if carry == 1:
                temp = add + carry
                if temp >= 10:
                    result = str(temp)[1] + result
                    carry = 1
                else:
                    result = str(temp) + result
                    carry = 0
            else:
                temp = add
                if temp >= 10:
                    result = str(temp)[1] + result
                    carry = 1
                else:
                    result = str(temp) + result
                    carry = 0
    return str(int(num1[0])+int(num2[0])+carry) + result


def addStrings(num1,num2):
    def additionStrings(num1,num2,result,carry):
        carry = 0
        result = ''
        diff = len(num1) - len(num2)
        if diff > 0:
            num2 = '0' * (len(num1) - len(num2)) + num2
        else:
            num1 = '0' * (len(num2) - len(num1)) + num1

        low = 0
        high = len(num1) - 1
        for i in range(high,low,-1):
            add = num1[i] + num2[i] + carry
            if add >= 10:
                additionStrings(num1[i],num2[i],add,1)
            else:
                additionStrings(num1[i],num2[i],add,0)


def addStrings(num1,num2):
    carry = 0
    result = ''
    diff = len(num1) - len(num2)
    if diff > 0:
        num2 = '0'*(len(num1)-len(num2)) + num2
    else:
        num1 = '0'*(len(num2)-len(num1)) + num1

    low = 0
    high = len(num1) - 1
    for i in range(high,low,-1):
        aggregate = int(num1[i]) + int(num2[i]) + carry
        carry, remainder = divmod(aggregate, 10)
        result = str(remainder) + result

    return str(int(num1[0]) + int(num2[0]) + carry) + result



# print addition('123412','5678')
print addStrings('123412','5678')