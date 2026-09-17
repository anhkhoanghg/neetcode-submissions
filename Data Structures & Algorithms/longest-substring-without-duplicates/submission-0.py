class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        travel = set()
        left = 0

        for right in range(len(s)):
            while s[right] in travel:
                travel.remove(s[left])
                left += 1

            travel.add(s[right])
            res = max(res, right - left + 1)

        return res
