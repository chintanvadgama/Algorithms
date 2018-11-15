def finddNumber(array, intNumber):
    if array:
        if len(array) == 1:
            pass
        else:
            array = sorted(array)
            lower = 0
            upper = len(array)
            matched = False
            while lower < upper:
                x = lower + (upper - lower) // 2
                val = array[x]
                if intNumber == val:
                    matched = True
                    break
                elif intNumber > val:
                    if lower == x:
                        break
                    lower = x
                    if val == intNumber:
                        matched = True
                        break
                elif intNumber < val:
                    upper = x
                    if val == intNumber:
                        matched = True
                        break
            return matched

def binarySearch(arr,target):
    arr = sorted(arr)
    lower = 0
    upper = len(arr) -1
    while (lower <= upper):
        mid = lower + (upper-lower) //2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            lower = mid+1
        else:
            upper =mid-1
    return False



print binarySearch([1, 3, 10, 20, 35, 51, 55, 67], 69)
# print finddNumber([1, 3, 10, 20, 35, 51, 55, 67], 69)


