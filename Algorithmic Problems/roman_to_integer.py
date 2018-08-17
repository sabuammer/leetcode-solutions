class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        stack = []
        roman_int = 0
        for char in s:
            if not stack:
                stack.append(char)
            else:
                if roman_dict[char] <= roman_dict[stack[-1]]:
                    roman_int += roman_dict[stack.pop()]
                    stack.append(char)
                else:
                    roman_int += roman_dict[char] - roman_dict[stack.pop()]
        if stack:
            roman_int += roman_dict[stack.pop()]
        return roman_int