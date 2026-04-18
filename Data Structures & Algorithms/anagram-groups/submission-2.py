class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        output = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            output[sorted_word].append(word)
        
        return list(output.values())

