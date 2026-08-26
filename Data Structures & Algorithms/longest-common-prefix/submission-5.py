class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        i = 0
        while i < len(strs[0]):
            if strs[0][i] != strs[-1][i]:
                break
            i += 1
        
        return strs[0][:i]