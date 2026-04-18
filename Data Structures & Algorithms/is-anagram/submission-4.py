class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        from collections import defaultdict

        count_s = defaultdict()       

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        for char in t:
            if char not in count_s.keys():
                return False
            count_s[char] = count_s.get(char, 0) - 1

        return all([val == 0 for val in count_s.values()])

        