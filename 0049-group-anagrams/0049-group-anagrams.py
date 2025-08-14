class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for idx, string in enumerate(strs):
            sorted_str = ''.join(sorted(string))
            if sorted_str in hash:
                hash[sorted_str].append(strs[idx])
            else:
                hash[sorted_str] = [strs[idx]]
        return list(hash.values())