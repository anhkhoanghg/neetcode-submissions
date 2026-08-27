class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0] * 26
        init_ord = ord('a')
        for i in range(len(s)):
            counter[ord(s[i]) - init_ord] += 1
            counter[ord(t[i]) - init_ord] -= 1

        for val in counter:
            if val != 0:
                return False

        return True

