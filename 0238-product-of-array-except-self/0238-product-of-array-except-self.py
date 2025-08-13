class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_product = [1] * (length)
        out = [1] * (length)
        i = 1
        while i < length:
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
            out[length - 1 - i] = out[length - i] * nums[length - i]
            i += 1
        for i in range(length):
            out[i] *= prefix_product[i]
        return out

