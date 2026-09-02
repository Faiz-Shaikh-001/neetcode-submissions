class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity, weights, d):
            count = 1
            currWeight = 0
            for weight in weights:
                if currWeight + weight > capacity:
                    count += 1
                    currWeight = weight
                    continue
                currWeight += weight
            
            return count <= d
        
        l, r = max(weights), sum(weights)
        while l <= r:
            mid = l + (r - l) // 2
            if canShip(mid, weights, days):
                r = mid - 1
            else:
                l = mid + 1
        
        return l