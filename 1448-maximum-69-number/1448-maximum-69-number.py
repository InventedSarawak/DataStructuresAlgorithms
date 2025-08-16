import math
class Solution:
    def maximum69Number (self, num: int) -> int:
        num_digits = floor(log10(num)) + 1
        while num_digits > 0:
            exp = 10 ** (num_digits - 1)
            curr_digit = (num // exp) % 10
            if curr_digit == 6:
                return num + 3 * exp
            num_digits -= 1
        return num
        
 