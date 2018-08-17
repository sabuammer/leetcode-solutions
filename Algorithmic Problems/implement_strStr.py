class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        elif len(haystack) < len(needle):
            return -1
        elif len(haystack) == len(needle):
            return 0 if haystack == needle else -1 
        else:
            i = j = k = returned_index = 0
            first_index = True
            for i in range(len(haystack)):
                k = i
                while j < len(needle) and k < len(haystack):
                    if haystack[k] == needle[j]:
                        if first_index:
                            returned_index = k
                            first_index = False
                        j += 1
                        k += 1
                    else:
                        first_index = True
                        j = 0
                        break
                if j == len(needle):
                    return returned_index
        return -1