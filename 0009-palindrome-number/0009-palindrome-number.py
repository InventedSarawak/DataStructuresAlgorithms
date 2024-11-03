class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        temp : int = x

        digits : int = 0
        while x > 0: 
            digits += 1
            x //= 10

        forward_mask : int = 10 ** (digits - 1)
        
        while forward_mask > 1 : 

            if (temp // forward_mask) % 10 != temp % 10 : return False

            forward_mask //= 100
            temp //= 10

        return True
