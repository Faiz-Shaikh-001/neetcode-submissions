class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        numsSet = set(nums)
        while True:
            if i not in numsSet:
                return i
            i += 1