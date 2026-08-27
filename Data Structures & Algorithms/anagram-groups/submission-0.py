class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        init_ord = ord('a')
        for e in strs:
            counter = [0] * 26
            for char in e:
                counter[ord(char) - ord('a')] += 1
            res[tuple(counter)].append(e)
        return list(res.values())
        