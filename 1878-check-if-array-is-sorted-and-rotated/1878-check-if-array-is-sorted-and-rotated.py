class Solution:
    def check(self, nums: List[int]) -> bool:
        length: int = len(nums)
        isNotSorted: int = 0
        j: int = 0
        for j in range(length):
            i: int = 0
            while i < length - 1:
                if nums[(i + j) % length] > nums[(i + j + 1) % length]:
                    isNotSorted = 1
                    break
                i += 1
            if not isNotSorted:
                return True
            isNotSorted = 0
        return False
