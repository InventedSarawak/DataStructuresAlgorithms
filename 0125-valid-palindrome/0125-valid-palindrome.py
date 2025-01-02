class Solution:
    def format_string(self, s:str):
        s = s.lower()
        new_str = ''
        for i in s:
            if i.isalnum():
                new_str += i
        return new_str

    
    def isPalindrome(self, s: str) -> bool:
        s = self.format_string(s)
        length = len(s)
        for i in range(length // 2):
            if s[i] != s[length - i - 1]:
                return False
        return True
        