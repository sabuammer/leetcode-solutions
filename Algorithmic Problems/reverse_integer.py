class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        stack = []
        negative = False
        if x < 0:
            x *= -1
            negative = True
        str_x = str(x)
        rev_x = ''
        for char in str_x:
            stack.append(char)
        while stack:
            rev_x += stack.pop()
        rev_int = int(rev_x)
        if negative:
            rev_int *= -1
        if rev_int > 2**31 or rev_int < -2**31:
            return 0
        return rev_int
        