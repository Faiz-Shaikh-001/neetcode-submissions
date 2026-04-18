class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        ptr_s, ptr_t = 0, 0

        while ptr_s < len(s) and ptr_t < len(t):
            if s[ptr_s] == t[ptr_t]:
                ptr_t += 1
                ptr_s += 1
            else:
                ptr_t += 1
        
        return True if ptr_s == len(s) else False