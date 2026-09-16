class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        
        numSet = set()
        for i in nums:
            numSet.add(i)

        for val in nums:
            if val in numSet and (val - 1) not in numSet:
                cur = val
                streak = 0
                while cur in numSet:
                    cur += 1
                    streak += 1
                
                res = max(res, streak)
        return res
