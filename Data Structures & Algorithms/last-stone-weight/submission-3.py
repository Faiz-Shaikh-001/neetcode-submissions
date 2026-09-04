class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStones = []
        for stone in stones:
            heapq.heappush(maxStones, -stone)
        
        while maxStones and len(maxStones) > 1:
            x = -heapq.heappop(maxStones)
            y = -heapq.heappop(maxStones)
            if x == y:
                continue
            elif x > y:
                x = x - y
                heapq.heappush(maxStones, -x)
            else:
                y = y - x
                heapq.heappush(maxStones, -y)
        
        return -maxStones[0] if maxStones else 0