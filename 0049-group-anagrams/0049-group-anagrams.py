class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for idx, string in enumerate(strs):
            sorted_str = ''.join(sorted(string))
            if sorted_str in hash:
                hash[sorted_str].append(idx)
            else:
                hash[sorted_str] = [idx]
        out = []
        for strings in hash:
            anagram_list = []
            for anagram in hash[strings]:
                anagram_list.append(strs[anagram])
            out.append(anagram_list)
        return out