class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        
        squared_sum = 0
        seen = set([])
        
        while squared_sum != 1:
            while n != 0:
                curr_digit = n % 10
                squared_sum += curr_digit ** 2
                n = n // 10
            if squared_sum not in seen:
                seen.add(squared_sum)
            else:
                return False
            if squared_sum == 1:
                return True
            n = squared_sum
            squared_sum = 0
        