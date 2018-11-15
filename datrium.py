
test_list_to_dict = [1,2,3,4,5]

def convert_list_to_dict(arr):
    output = {}
    for idx, ele in enumerate(arr):
        output[idx] = ele
    return output

print(convert_list_to_dict(test_list_to_dict))


class Sort(object):
    def __init__(self,arr):
        self.arr = arr

    def partition(self,first,last):
        pivot = self.arr[first]
        left = first + 1
        right = last
        done = False
        while not done:
            while left <= right and self.arr[left] <= pivot:
                left += 1
            while self.arr[right] >= pivot and right >= left:
                right -= 1
            if right < left:
                done = True
            else:
                self.arr[left],self.arr[right] = self.arr[right],self.arr[left]
        self.arr[first],self.arr[right] = self.arr[right],self.arr[left]
        return right

    def helper(self,first,last):
        if first < last:
            split = self.partition(first,last)
            self.helper(first,split - 1)
            self.helper(split + 1, last)

    def quicksort(self):
        self.helper(0,len(self.arr) - 1)


def prime_numbers(number):
    """
    [2,3,5,7,11,13]
    :param number:
    :return: List of prime numbers
    """
    if number == 2:
        return [2]
    elif number < 2:
        return []
    s = range(3,number + 1,2)
    # [3,5,7,9]
    mroot = number ** 0.5 #3.xxxx
    half = (number+1)/2 - 1 #4.5
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2 #j =3
            s[j] =0 #[3,5,7,0]
            while j < half:
                s[j] = 0
                j += m # j= 3
        i += 1
        m = 2*i + 3
    return [2] + [i for i in s if i]


def find_closest_match(arr, target):
    """
    [0, 34, 15, -7, 2, 16, 8]
    [-7, 0, 2, 8, 15, 16, 34]

    :param input:
    :return:
    """
    min_diff = -1 
