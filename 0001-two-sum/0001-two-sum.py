class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, val in enumerate(nums):
            if target - val in hash:
                return [hash[target - val], idx]
            hash[val] = idx
        