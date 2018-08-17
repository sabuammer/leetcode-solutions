class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not (s or t):
            return True
        
        my_dict = {}
        for i in range(len(s)):
            if s[i] not in my_dict:
                if t[i] in my_dict.values():
                    return False
                my_dict[s[i]] = t[i]
            elif my_dict[s[i]] != t[i]:
                return False
        return True