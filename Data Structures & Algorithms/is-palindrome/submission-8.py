class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 0:
            return True

        s = s.lower()
        p1 = 0
        p2 = len(s)-1
        while True:
            if p1 == p2 or p1 > p2 or p1 > len(s) - 1 or p2 < 0:
                break
            elif not s[p1].isalnum():
                p1 += 1
                continue
            elif not s[p2].isalnum():
                p2 -= 1
                continue
            elif s[p1] != s[p2]:
                return False
            else:
                p1 += 1    
                p2 -= 1
        return True

            