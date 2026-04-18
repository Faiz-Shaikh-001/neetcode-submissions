class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums and nums.count(0) > 1:
            return [0] * len(nums)

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for idx in range(1, n):
            prefix[idx] = nums[idx-1] * prefix[idx-1]
        
        for idx in range(n-2, -1, -1):
            suffix[idx] = nums[idx+1] * suffix[idx+1]
        return [prefix[idx] * suffix[idx] for idx in range(n)]