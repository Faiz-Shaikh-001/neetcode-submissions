class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # calculate hashValue for s1
        s1_count = [0] * 26
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        
        k = len(s1)
        start, end = 0, k
        window_count = [0] * 26
        for c in s2[start:end]:
            window_count[ord(c) - ord('a')] += 1 
        
        if window_count == s1_count:
            return True

        for i in range(end, len(s2)):
            window_count[ord(s2[i-k]) - ord('a')] -= 1
            window_count[ord(s2[i]) - ord('a')] += 1
            if window_count == s1_count:
                return True

        return False
            
            