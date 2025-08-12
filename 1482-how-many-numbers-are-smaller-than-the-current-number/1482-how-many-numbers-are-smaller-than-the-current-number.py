class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        temp = nums[:]
        temp.sort()
        hash = {temp[0] : 0}
        for idx, element in enumerate(temp):
            if element not in hash:
                hash[element] = idx
        return [hash[nums[idx]] for idx in range(length)]
