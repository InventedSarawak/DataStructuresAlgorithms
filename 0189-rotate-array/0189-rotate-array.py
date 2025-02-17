class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length: int = len(nums)
        duplicate_list: list[int] = nums[:]
        nums[:] = []
        k %= length
        for num in duplicate_list[-k:]:
            nums.append(num)
        for num in duplicate_list[:-k]:
            nums.append(num)