class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        len_s = len(s)
        len_t = len(t) 
        if len_s != len_t:
            return False
        for i in range(len_s):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for i in freq:
            if i != 0:
                return False
        return True