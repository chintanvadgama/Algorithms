def backspaceStringCompare(S,T):
    #  S = "ab#c", T = "ad#c"
    skip = 0
    r1 = ''
    r2 = ''
    for i in range(len(S) - 1, -1, -1):
        if S[i] == '#':
            skip += 1
        elif skip:
            skip -= 1
        else:
            r1 += S[i]
    for j in range(len(T) - 1, -1, -1):
        if T[j] == '#':
            skip += 1
        elif skip:
            skip -= 1
        else:
            r2 += T[j]
    return r1 == r2


def bestTimeTobuyNSellStock(prices):
    total = 0
    for i in range(len(prices) - 1):
        if prices[i+1] > prices[i]:
            total += prices[i+1] - prices[i]
    return total

def bestTimeTobuyNSellStockSingleTransaction(prices):
    total = 0
    buy = 0
    maxProfit = 0
    for sell in range(len(prices) - 1):
        if prices[sell] < prices[buy]:
            buy = sell
        else:
            maxProfit = max(maxProfit,prices[sell] - prices[buy])
    return maxProfit


def binary_search(arr,target):
    low = 0
    high = len(arr) - 1
    while low <= high and not found:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


def closest_sum(arr,target):
    # Logic: Sum of two elements - target should be minimum
    # 2 pointers L, R and check minimum sum
    import sys
    diff = sys.maxint
    left = 0
    right = len(arr) - 1
    res_l = res_r = 0
    while left < right:
        difference = abs(arr[left] + arr[right] - target)
        if difference < diff:
            res_l = left
            res_r = right
        elif arr[left] + arr[right] > diff:
            right -= 1
        else:
            left -= 1
    return (res_l,res_r)

def compress_string(data):
    output = ""
    count = 1
    for i in range(len(data) - 1):
        if data[i+1] == data[i]:
            count += 1
        else:
            output = output + data[i] + str(count)
            count = 1
    output = output + data[-1] + str(count)
    return output

def max_consecutive_ones(arr):
    maxNum = 0
    ans = 0
    for i in range(len(arr) - 1):
        if arr[i] == 1:
            maxNum += 1
        else:
            ans = max(maxNum, ans)
            maxNum = 0
    return ans


def containsduplicate(arr):
    lookup = {}
    for ele in arr:
        if ele in lookup:
            lookup[ele] += 1
        else:
            lookup[ele] = 1
    duplicate = False
    for k,v in lookup.items():
        if v > 1:
            return True
max_consecutive_ones([0,1,1,2])


def first_uniq_char(string):
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    idx_arr = []
    for ltr in all_letters:
        if string.count(ltr) == 1:
            index = string.index(ltr)
            idx_arr.append(index)
    if len(idx_arr) > 1:
        return min(idx_arr)
    else:
        return -1

def intersection(arr1,arr2):
    lookup = {}
    common = []
    for a in arr1:
        if a in lookup:
            lookup[a] += 1
        else:
            lookup[a] = 1

    for a in arr2:
        if a in lookup and lookup[a] > 0:
            common.append(a)
            lookup[a] -= 1
    return common

def majorityElement(arr):
    # [2,2,2,1,1] Return 2
    lookup = {}
    freq_numbers = []
    for a in arr:
        if a in arr:
            lookup[a] += 1
        else:
            lookup[a] = 1
    max_count = max(lookup.values())
    for k,v in lookup.items():
        if v == max_count:
            freq_numbers.append(k)
    return freq_numbers

def merge_two_sorted_lists(arr1,arr2):
    # Space O(M+N)
    # Time O(M+N)
    n1 = len(arr1)
    n2 = len(arr2)
    merged_list = [None] * (n1 + n2)
    i = j = k = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            merged_list[k] = arr1[i]
            k += 1
            i += 1
        else:
            merged_list[k] = arr2[j]
            k += 1
            j += 1
    while i < n1:
        merged_list[k] = arr1[i]
        k += 1
        i += 1
    while j < n2:
        merged_list[k] = arr2[j]
        k += 1
        j += 1

    return list(set(merged_list))

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        print output
        print p
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

def rev_words_in_string(string):
    low = 0
    high = len(string) - 1
    j = 0
    # string = string.strip() # remove leading n trailing spaces
    ls = []
    for i in range(len(string) - 1):
        if string[i] == ' ' and i != 0:
            ls.append(string[j:i].strip())
            j = i
    ls.append(string[j:len(string)].strip())
    return ' '.join([i for i in ls[::-1] if i])

def find_target_sum(arr,target):
    # [5,5,1,4,3] 7
    lookup = {}
    for a in arr:
        lookup[a] = arr.index(a)
    pairs = []
    for a in arr:
        complement = target - a
        if complement in lookup:
            pairs.append((complement,a))

    low = 0
    high = len(arr) - 1
    arr = sorted(arr)
    sum_pairs = []
    while arr[low] + arr[high] != target:
        if arr[low] + arr[high] < target:
            low += 1
        elif arr[low] + arr[high] == target:
            sum_pairs.append((arr[low],arr[high]))
            continue
        else:
            high -= 1
    print sum_pairs
    print set(pairs)

def find_max(arr):
    max = arr[0]
    for a in arr:
        if a > max:
            max = a
    return max

def second_larget(arr):
    less = []
    greater = []
    equal = []
    pivot = arr[0]
    for a in arr:
        if a > pivot:
            greater.append(a)
        elif a < pivot:
            less.append(a)
        else:
            equal.append(a)
    print sorted(less) + equal + greater

def removeduplicates(arr):
    arr = sorted(arr)
    j = 0
    for i in range(len(arr) - 1):
        if arr[i] != arr[j]:
            arr[j] = arr[i]
            j += 1
    arr[j] = arr[-1]
    j += 1
    print arr[:j]

def mindistancebetweenarrelements(arr,x,y):
    # to find 1st occurance of x or y
    import sys
    prev = 0
    for a in arr:
        if a == x or a == y:
            prev = arr.index(a)
            break
    i = 0
    minDist = sys.maxint
    # traverse through list and check
    while i < len(arr) - 1:
        if arr[i] == x or arr[i] == y:
            if arr[prev] != arr[i] and i - prev < minDist:
                minDist = i - prev
                prev = i
            else:
                prev = i
        i += 1
    return minDist

# def to_lower(string):
#     string_letters = "ABCDEFGH"
#     ls = list(string)
#     for i in range(len(ls)-1 ):
#         if ord(ls[i]) >= ord('A') and ord(ls[i]) <= ord('Z'):
#             ls[i] = chr(ls[i]-'A'+'a')



def merge_strings(s1,s2):
    min_length = min(len(s1),len(s2))
    output = ''
    for i in range(min_length):
        output += s1[i]
        output += s2[i]
    if min_length == len(s1):
        output += s2[min_length:]
    else:
        output += s1[min_length]
    return output

def extract_maximum(string):
    ls = []
    high = len(string) - 1
    low = 0
    number = ''
    for i in range(low,high):
        if string[i].isdigit():
            number += string[i]
    print number

def first_repeting_ch(string):
    repeting_chr = ''
    for i in range(len(string) - 1):
        if string.count(string[i]) > 1:
            repeting_chr += string[i]
            break

    return repeting_chr

def find_pick_element(nums):
    for i in range(len(nums) - 1):
        if nums[i-1] < nums[i] < nums[i+1]:
            return i
        elif nums[-1] < nums[-2]:
            return

print first_repeting_ch('chintan')


extract_maximum('ass100klh564abc365bg')




print merge_strings('abcd','efghi')
#aebfcgdhi

# removeduplicates([1,1,1,4,5,6])
# print second_larget([1,4,112,129,3,10,4])
#
# print find_max([1,4,112,129,3,10,4])
# find_target_sum([5,5,1,4,3,3,2],7)
# print rev_words_in_string('chintan is good')
#
# Solution().productExceptSelf([1,2,3,4])

