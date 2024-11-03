class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_in_str : str = str(x)
        return x_in_str == x_in_str[::-1]