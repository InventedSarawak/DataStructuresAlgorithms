class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length: int = len(nums)
        fast: int = 0
        slow: int = 0
        while fast < length:
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1