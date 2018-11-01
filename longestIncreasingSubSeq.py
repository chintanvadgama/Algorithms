def find_longest_increasing_sub(arr):
    if len(arr) == 1 or not arr:
        return arr
    result = []
    i = 0
    j = 1
    for i in range(i,len(arr)):
        for j in range(j,len(arr)):
            print 'arr[%s] = %s , arr[%s] = %s' %(i,arr[i],j,arr[j])
            if arr[j] > arr[i]:
                result.append(arr[i])
                i += 1
                j += 1
            else:

                i = 1
                j = 0
        if arr[i] > arr[i-1]:
            result.append(arr[i])
    return result



if __name__ == '__main__':
    print find_longest_increasing_sub([10,22,9,33,50,60,80])



