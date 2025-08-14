class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str in hash:
                hash[sorted_str].append(string)
            else:
                hash[sorted_str] = [string]
        return list(hash.values())