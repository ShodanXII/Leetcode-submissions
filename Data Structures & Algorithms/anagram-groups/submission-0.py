from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        result = []

        for i in strs:
            test = tuple(sorted(i))
            anagrams[test].append(i)
        for value in anagrams.values():
            result.append(value)
        return result