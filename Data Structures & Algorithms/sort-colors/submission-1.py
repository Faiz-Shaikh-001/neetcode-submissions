class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for num in nums:
            counts[num] += 1
        
        ptr = 0
        for idx, count in enumerate(counts):
            nums[ptr:ptr+count+1] = [idx] * count
            ptr += count
        
