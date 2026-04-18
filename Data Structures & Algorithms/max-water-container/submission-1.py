class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        max_area = 0

        while left < right:
            curr_area = min(heights[left], heights[right]) * (right - left)
            
            if max_area < curr_area:
                max_area = curr_area
            
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
                flag = True
        
        return max_area
            