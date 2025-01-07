class Solution:
    def secondHighest(self, s: str) -> int:
        return self.find_second_largest_number(self.get_digit_arr(s))

    def get_digit_arr(self, s: str) -> list[int]:
        arr: list[int] = [int(ch) for ch in s if ch.isdigit()]
        return arr


    def find_second_largest_number(self, arr: list[int]) -> int:
        largest = float(-inf)
        second_largest = float(-inf)
        for val in arr:
            if val > largest:
                second_largest = largest
                largest = val
            elif val > second_largest and val != largest:
                second_largest = val
        if second_largest == float(-inf):
            return -1
        return second_largest