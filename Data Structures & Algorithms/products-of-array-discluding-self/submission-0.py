class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums and nums.count(0) > 1:
            return [0] * len(nums)
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for idx in range(n):
            if idx == 0:
                continue
            if idx == 1:
                prefix[idx] = nums[idx-1]
                continue
            prefix[idx] = nums[idx-1] * prefix[idx-1]
        
        for idx in range(n-1, -1, -1):
            if idx == n-1:
                continue
            if idx == n-2:
                suffix[idx] = nums[idx+1]
                continue
            suffix[idx] = nums[idx+1] * suffix[idx+1]
        return [prefix[idx] * suffix[idx] for idx in range(n)]