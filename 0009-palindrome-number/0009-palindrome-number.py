class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): return False
        temp : int = x
        reverse : int = 0
        while reverse < x : 
            reverse = reverse * 10 + temp % 10
            temp //= 10
        if reverse == x: return True
        return False
