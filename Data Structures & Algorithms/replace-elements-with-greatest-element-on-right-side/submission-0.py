class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [-1] * n
        currMax = arr[-1]
        
        for i in range(n-2, -1, -1):
            res[i] = currMax

            if arr[i] > currMax:
                currMax = arr[i]
        
        return res