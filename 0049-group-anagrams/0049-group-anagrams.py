# class Solution:

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hash = {}
#         for string in strs:
#             sorted_str = ''.join(sorted(string))
#             if sorted_str in hash:
#                 hash[sorted_str].append(string)
#             else:
#                 hash[sorted_str] = [string]
#         return list(hash.values())

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for string in strs:
            # Count characters (only 26 lowercase English letters)
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            # Use tuple of counts as key
            hash_map[tuple(count)].append(string)
        return list(hash_map.values())
