class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, current_set):
            if index == len(nums):
                res.append(current_set[:])
                return
            
            backtrack(index+1, current_set)

            current_set.append(nums[index])
            backtrack(index+1, current_set)
            current_set.pop()

        backtrack(0, [])
        return res