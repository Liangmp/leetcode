class Solution(object):
    def fizzBuzz(self, n):
        fizzbuzzlist = []
        for i in range(1,n+1):
            if i % 15 == 0:
                fizzbuzzlist.append("FizzBuzz")
            elif i % 3 == 0:
                fizzbuzzlist.append("Fizz")
            elif i % 5 == 0:
                fizzbuzzlist.append("Buzz")
            else:
                fizzbuzzlist.append(str(i))
        return fizzbuzzlist
    
        """
        :type n: int
        :rtype: List[str]
        """