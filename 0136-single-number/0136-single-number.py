class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single: list[int] = []
        for num in nums:
            if num in single: single.remove(num)
            else: single.append(num)
        return single[0]
