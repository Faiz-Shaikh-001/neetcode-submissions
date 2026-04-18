class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_val = float("inf")
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid] and nums[mid] >= nums[r]:
                min_val = min(min_val, nums[mid])
                l = mid + 1
            elif nums[l] >= nums[mid] and nums[mid] <= nums[r]:
                min_val = min(min_val, nums[mid])
                r = mid - 1
            elif nums[l] >= nums[mid] >= nums[r]:
                return min(min_val, nums[r])
            else:
                return min(min_val, nums[l])

        return min_val
     