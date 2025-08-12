class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = [ord(char) - ord('a') for char in s]
        arr2 = [ord(char) - ord('a') for char in t]
        arr1.sort()
        arr2.sort()
        if arr1 == arr2:
            return True
        return False