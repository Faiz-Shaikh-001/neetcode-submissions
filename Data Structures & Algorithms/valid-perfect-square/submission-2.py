class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 1:
            return True
            
        l, r = 1, (num // 2)

        while l < r:
            mid = (l + r) // 2
            mid_squared = mid * mid
            if mid_squared == num:
                return True
            elif mid_squared < num:
                l = mid + 1
            else:
                r = mid
        
        return False
