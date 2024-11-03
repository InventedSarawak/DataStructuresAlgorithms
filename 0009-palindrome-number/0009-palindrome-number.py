class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_in_str : str = str(x)
        return string_is_palindrome(x_in_str)


def string_is_palindrome(arr : str, left : int = 0) -> bool:
    if left >= (len(arr) - 1) / 2 : return True
    if arr[left] != arr[len(arr) - left - 1] : return False
    return string_is_palindrome(arr, left + 1)