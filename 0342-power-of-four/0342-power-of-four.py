class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        digits =  math.floor(math.log2(abs(n))) + 1
        if (digits - 1) % 2 != 0:
            return False
        return (1 << (digits - 1) == n)