class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for val in nums:
            mp[val] = mp.get(val, 0) + 1
        heap = []
        for val, freq in mp.items():
            heapq.heappush(heap, [freq, val])

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        temp = [0] * len(heap)
        index = len(heap) - 1
        while heap:
            temp[index] = heapq.heappop(heap)[1]
            index -= 1
        for val in temp:
            res.append(val)

        return res
