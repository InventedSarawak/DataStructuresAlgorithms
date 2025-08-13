import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        heap = []
        for num in freq:
            curr_freq = freq[num]
            if len(heap) < k:
                heapq.heappush(heap, (curr_freq, num))
            else:
                if curr_freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (curr_freq, num))

        out = []
        while heap:
            out.append(heapq.heappop(heap)[1])
        return out


