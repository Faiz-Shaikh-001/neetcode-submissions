class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        ball_pos = set()
        for i in range(len(boxes)):
            if boxes[i] == '1':
                ball_pos.add(i)
        
        for i in range(len(boxes)):
            for pos in ball_pos:
                if pos != i:
                    res[i] += abs(pos - i)
            
        return res