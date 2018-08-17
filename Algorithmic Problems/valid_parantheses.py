class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parens = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            try:
                if char in parens:
                    stack.append(char)
                elif parens[stack.pop()] != char:
                    return False
            except:
                return False
        if not stack:
            return True
        else:
            return False