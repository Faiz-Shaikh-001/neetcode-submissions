class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                
                if self.kmp(words[j], words[i]):
                    res.append(words[i])
                    break
        
        return res

    def lps(self, pat: str) -> List[int]:
        i, j = 0, 1
        n = len(pat)
        lpsArray = [0] * n

        while j < n:
            if pat[i] == pat[j]:
                i += 1
                lpsArray[j] = i
                j += 1
            else:
                i = 0
                j += 1
        
        return lpsArray
    
    def kmp(self, txt: str, pat: str) -> bool:
        lpsArray = self.lps(pat)

        i = j = 0
        
        while i < len(txt):
            if txt[i] != pat[j]:
                if j != 0:
                    j = lpsArray[j-1]
                else:
                    i += 1
            else:
                j += 1
                i += 1

            # Match Found
            if j == len(pat):
                return True
    
        return False

        