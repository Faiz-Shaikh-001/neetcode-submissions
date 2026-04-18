class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def calculateTime(dist, speed):
            return (target - dist) / speed
        
        timeTakenList = [(pos, calculateTime(pos, speed)) for pos, speed in zip(position, speed)]
        stack = sorted(timeTakenList, key=lambda x: x[0])
        
        fleetCount = 1
        currMaxTime = stack[-1][1]
        while stack:
            if stack[-1][1] > currMaxTime:
                currMaxTime = stack[-1][1]
                fleetCount += 1
            stack.pop()
        
        return fleetCount

