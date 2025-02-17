class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length: int = len(nums)
        k %= length
        nums[:] = nums[-k:] + nums[: -k]