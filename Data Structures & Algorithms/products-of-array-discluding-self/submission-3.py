class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if nums.count(0) > 1:
            return [0] * n

        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for j in range(n-1, -1, -1):
            output[j] *= suffix
            suffix *= nums[j]
        return output