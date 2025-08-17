class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [num ** 2 for num in nums]
        out = []
        length = len(nums)
        small = 0
        for i in range(length):
            if nums[small] > nums[i]:
                small = i
        right = small
        left = small - 1
        while left >= 0 and right <= length - 1:
            if nums[left] == nums[right]:
                out.append(nums[left])
                out.append(nums[left])
                left -= 1
                right += 1
            elif nums[left] < nums[right]:
                out.append(nums[left])
                left -= 1
            else:
                out.append(nums[right])
                right += 1
        while left >= 0:
            out.append(nums[left])
            left -= 1
        while right <= length - 1:
            out.append(nums[right])
            right += 1
        return out




        
