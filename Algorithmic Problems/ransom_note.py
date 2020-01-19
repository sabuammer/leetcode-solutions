class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = {}
        for char in magazine:
            if char not in mag_count:
                mag_count[char] = 1
            else:
                mag_count[char] += 1

        for char in ransomNote:
            if char in mag_count and mag_count[char] > 0:
                mag_count[char] -= 1
            else:
                return False

        return True
