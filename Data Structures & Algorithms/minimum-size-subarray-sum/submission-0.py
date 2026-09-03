class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minn = float('inf')
        l, currSum = 0, 0
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                minn = min(minn, r - l + 1)
                currSum -= nums[l]
                l += 1
        
        return minn if minn != float('inf') else 0


        
