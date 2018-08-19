memo = {}
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            memo[n] = 1
            return memo[n]
        elif n == 2:
            memo[n] = 2
            return memo[n]
        else:
            if n in memo:
                return memo[n]
            else:
                memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
                return memo[n]