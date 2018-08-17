class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x2 = x
        is_palin = True
        num_digits = len(str(x))
        for i in range(num_digits):
            if x // 10**(num_digits-1) != x2 % 10:
                is_palin = False
                break
            x = x % (10**(num_digits-1))
            x2 = x2 // 10
            num_digits -= 1
        return is_palin