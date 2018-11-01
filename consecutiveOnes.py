def findMaxConsecutiveOnes(arr):
    if len(arr) == 1 and arr[0] == 1:
        return 1
    maxNum = 0
    ans = 0
    low = 0
    high = len(arr) - 1
    for i in range(low,high):
        if arr[i] != 1:
            maxNum += 1
            ans = max(ans,maxNum)
        else:
            maxNum = 0
    return ans

