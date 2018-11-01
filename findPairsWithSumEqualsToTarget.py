def find_pairs(arr,target):
    if len(arr) < 2:
        return "Error"
    lookup = {}
    result = []
    for a in arr:
        diff = target - a
        if diff > 0 and diff in lookup:
            result.append((diff,a))
        else:
            lookup[diff] = a
    # print lookup
    return result


def find_pairs_bs(arr,target):
    arr = sorted(arr)
    pairs = []
    low = 0
    high = len(arr) - 1
    for i in range(low,high):
        diff = target - arr[i]
        j = binary_search(arr[i+1:],diff,0,len(arr[i+1:])-1)
        # print("index=%s"%j)
        import sys
        if j != sys.maxint:
            pairs.append((arr[i],arr[i+1:][j]))
    return pairs


def binary_search(arr,target,left,right):
    if len(arr) == 1 and arr[0] == target:
        return 0
    found = False
    import sys
    idx = sys.maxint
    while left <= right and not found:
        mid = (left+right) // 2
        if arr[mid] == target:
            found = True
            idx = mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return idx

# print binary_search([1,2,3,4],6,1,3)
# print(find_pairs([2,5,2,5,1,12,12,6],7))
print(find_pairs_bs([2,5,5,1,12,12,6],3))

