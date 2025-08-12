class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_1 = {}
        freq_2 = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in freq_1:
                freq_1[s[i]] += 1
            else:
                freq_1[s[i]] = 1
            
            if t[i] in freq_2:
                freq_2[t[i]] += 1
            else:
                freq_2[t[i]] = 1
        
        if freq_1 == freq_2:
            return True
        return False