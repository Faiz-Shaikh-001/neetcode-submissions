# input: nums: arr, target: int
# output: sum_index_array
# logic: [3, 4, 5, 6], 7 => two pointers, one at leftmost end and one at rightmost end
#                           first iteration: 3+6=9 > 7 decrease the right pointer by one
#                           second iteration: 3+5=8 > 7 decrease the right pointer by one
#                           third iteration: 3+4=7 == 7 return the indexes that is 0, 1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i <= len(nums) - 2:
            for j in range(i+1, len(nums)):
                total = nums[i] + nums[j]

                if total == target:
                    return [i, j]
                elif total != target:
                    j += 1
            i += 1
            

                
