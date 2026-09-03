class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        currSum = oddCount = evenCount = res = 0
        MOD = 10**9 + 7

        for n in arr:
            currSum += n
            if currSum % 2:
                res = (res + 1 + evenCount) % MOD
                oddCount += 1
            else:
                res = (res + oddCount) % MOD
                evenCount += 1
            
        return res