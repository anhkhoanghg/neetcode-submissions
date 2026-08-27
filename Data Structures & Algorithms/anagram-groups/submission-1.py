class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            sortedW = ''.join(sorted(word))
            group[sortedW].append(word)
        return list(group.values())
