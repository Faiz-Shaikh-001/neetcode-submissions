class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        from collections import defaultdict
        
        freq = defaultdict(int)
        for char in s:
            freq[char] = 1 + freq.get(char, 0)
        
        for char in t:
            if char not in freq:
                return False
            freq[char] -= 1
            
            
        return all(v == 0 for v in freq.values())

        