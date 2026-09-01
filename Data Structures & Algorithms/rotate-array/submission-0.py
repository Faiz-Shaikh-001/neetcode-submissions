class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        k = (k % len(nums)) - 1
        n = len(nums) - 1
        reverse(nums, 0, n)
        reverse(nums, 0, k)
        reverse(nums, k+1, n)