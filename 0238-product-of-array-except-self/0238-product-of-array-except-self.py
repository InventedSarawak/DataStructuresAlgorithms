class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length

        # prefix product is calculated
        # prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        prefix_product = 1
        for i in range(length):
            result[i] = prefix_product
            prefix_product *= nums[i]

        # postfix product is calculated
        # out[length - 1 - i] = out[length - i] * nums[length - i]
        postfix_product = 1
        for i in range(length - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        
        return result