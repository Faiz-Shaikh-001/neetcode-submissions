class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        n = len(piles)
        max_piles = max(piles)
        if n == h:
            return max_piles
        
        l = 1
        r = max_piles
        res = max_piles

        while l <= r:
            mid = (l + r) // 2
            hours_required = 0
            for pile in piles:
                hours_required += math.ceil(pile / mid)
            if hours_required <= h:
                r = mid - 1
                res = min(mid, res)
            else:
                l = mid + 1
            
        return res

