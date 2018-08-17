class Solution:
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        is_currently_char = False
        last_word_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                is_currently_char = True
                last_word_count += 1
            elif s[i] == ' ' and is_currently_char:
                break
        return last_word_count