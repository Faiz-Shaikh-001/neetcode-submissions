class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = defaultdict()

        n = len(s)
        i = 0
        while i < n:
            if s[i] in hashMap:
                if hashMap[s[i]] != t[i]:
                    return False
                i += 1 
                continue
            
            if t[i] in hashMap.values():
                return False

            hashMap[s[i]] = t[i]
            i += 1
        
        return True