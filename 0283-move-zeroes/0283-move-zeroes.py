class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        slow: int = 0
        fast: int = 0

        while fast != length:
            if nums[fast] == 0:
                fast += 1
                continue
            if slow != fast:
                nums[slow] = nums[fast]
                nums[fast] = 0
            slow += 1
            fast += 1
        
        return nums