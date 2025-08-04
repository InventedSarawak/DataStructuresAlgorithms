import heapq

class Solution:
    def findKthLargest(self, nums, k):
        output: int = 0
        length = len(nums)
        idx: int = 0
        sequence: list[int] = []
        for num in nums:
            heapq.heappush(sequence, num)
        while idx < length - k + 1:
            output = heapq.heappop(sequence)
            idx += 1
        return output

print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))

    
