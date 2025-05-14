class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length: int = len(nums)

        nums.sort()
        if nums[0] != 0:
            return 0
        if nums[length - 1] != length:
            return length
            
        i = 1
        while i <= length - 1:
            if (nums[i - 1] + 1 != nums[i]):
                return nums[i - 1] + 1
            i += 1