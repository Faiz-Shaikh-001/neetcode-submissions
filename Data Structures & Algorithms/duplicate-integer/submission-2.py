# output : boolean value
# input : array of intergers
# logic: if len(set(num)) == len(num) i.e length of original array is equal to length of array after changing it to a set is equal then no duplicates are present. Since set cannot contain duplicates and changes it to a single value

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False

        return True         