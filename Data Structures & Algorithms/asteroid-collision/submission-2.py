class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
                continue
            
            if asteroids[i] > 0:
                stack.append(asteroids[i])
                continue
            
            if stack[-1] < 0:
                stack.append(asteroids[i])
                continue
            else:
                add = False
                while stack and stack[-1] > 0:
                    if stack[-1] > abs(asteroids[i]):
                        add = False
                        break
                    elif stack[-1] == abs(asteroids[i]):
                        stack.pop()
                        add = False
                        break
                    else:
                        add = True
                        stack.pop()
                
                if add:
                    stack.append(asteroids[i])

        return stack
