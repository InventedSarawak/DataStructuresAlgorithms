class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_product = [1] * (length)
        suffix_product = [1] * (length)
        i = 1
        while i < length:
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
            suffix_product[length - 1 - i] = suffix_product[length - i] * nums[length - i]
            i += 1
        out = []
        for i in range(length):
            out.append(prefix_product[i] * suffix_product[i])
        return out

