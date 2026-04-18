class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p1, p2 = 0, 0

        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
            
        return 0 if p2 == len(t) else len(t[p2:])