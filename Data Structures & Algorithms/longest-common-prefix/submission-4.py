class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        res = ""

        if len(strs[0]) <= 0 or len(strs[-1]) <= 0 or strs[0][0] != strs[-1][0]:
            return res
        
        if strs[0] == strs[-1]:
            return strs[0]

        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                break
            res += strs[0][i]

        return res
