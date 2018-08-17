class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        
        for char in t:
            if char in s_dict:
                s_dict[char] -= 1
            else:
                return False
            
        vals_list = list(s_dict.values())
        for val in vals_list:
            if val != 0:
                return False
        return True