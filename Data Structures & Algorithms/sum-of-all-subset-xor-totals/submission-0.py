class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index, curr_xor):
            if index == len(nums):
                return curr_xor
            
            exclude = backtrack(index + 1, curr_xor)
            include = backtrack(index + 1, curr_xor ^ nums[index])
            return exclude + include
        
        return backtrack(0, 0)