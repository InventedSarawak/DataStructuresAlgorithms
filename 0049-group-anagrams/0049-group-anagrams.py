class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            hash[sorted_str].append(string)
        return list(hash.values())

