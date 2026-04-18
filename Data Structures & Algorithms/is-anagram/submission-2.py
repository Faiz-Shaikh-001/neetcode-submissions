class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        from collections import defaultdict
        
        freq = defaultdict(int)
        for char in s:
            freq[char] = 1 + freq.get(char, 0)
        
        freq = dict(freq)
        for char in t:
            if char not in freq:
                return False
            freq[char] -= 1
            
            
        return all([True if v==0 else False for _, v in freq.items()])

        