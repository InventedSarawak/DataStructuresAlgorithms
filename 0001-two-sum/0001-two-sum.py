class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, val in enumerate(nums):
            if val in hash:
                return [idx, hash[nums[idx]]]
            hash[target - nums[idx]] =  idx
