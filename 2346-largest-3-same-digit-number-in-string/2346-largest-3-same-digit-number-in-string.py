class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max = -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:
                curr = int(num[i])
                if curr > max:
                    max = curr
        if max == -1:
            return '' 
        return ''.join([str(max)] * 3)
