import heapq

class Solution:
    def findKthLargest(self, nums, k):
        output: int = 0
        length = len(nums)
        idx: int = 0
        sequence: list[int] = nums
        heapq.heapify(sequence)
        while idx < length - k + 1:
            output = heapq.heappop(sequence)
            idx += 1
        return output


    
