class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num_1: int = 0
        num_1: int = 0
        for num in nums:
            if num == 0: 
                if num_1 > max_num_1:
                    max_num_1 = num_1
                num_1 = 0
                continue
            if num == 1: 
                num_1 += 1
                continue
        return max_num_1 if max_num_1 > num_1 else num_1