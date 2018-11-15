class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        for i in range(1,n+1,1):
            if (i%3==0) and not (i%3==0 and i%5==0) and not (i%5==0):
                i = 'Fizz'
            elif (i%5==0) and not (i%3==0 and i%5==0) and not (i%3==0):
                i = 'Buzz'
            elif (i%3==0 and i%5==0):
                i='FizzBuzz'
            arr.append(i)

        return arr

print Solution().fizzBuzz(1)
                
