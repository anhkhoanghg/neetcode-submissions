class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        n = len(s)
        for i in range(0, n // 2):
            if s[i] == s[n - i - 1]:
                continue
            else:
                return False

        return True
        