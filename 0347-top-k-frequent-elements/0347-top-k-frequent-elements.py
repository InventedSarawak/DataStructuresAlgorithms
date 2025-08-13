import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        out = []
        length = len(nums)
        for i in range(length):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        for num in freq:
            heapq.heappush(heap, (-freq[num], num))
        len_heap = len(heap)

        while len_heap - len(heap) < k:
            neg_freq, num = heapq.heappop(heap)
            out.append(num)
        return out