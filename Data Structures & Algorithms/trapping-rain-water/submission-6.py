class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = 0, 0
        total_water = 0

        while l < r:
            if height[l] < height[r]:
                if max_l <= height[l]:
                    max_l = height[l]
                else:
                    total_water += max_l - height[l]
                l += 1
            else:
                if max_r <= height[r]:
                    max_r = height[r]
                else:
                    total_water += max_r - height[r]
                r -= 1
        return total_water
            

