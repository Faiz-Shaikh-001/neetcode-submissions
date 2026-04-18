class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        compStack = []
        res = []
        for i in range(len(temperatures)-1, -1, -1):
            if len(compStack) == 0:
                res.append(0)
                compStack.append((i, temperatures[i]))
                continue

            while compStack:
                if temperatures[i] >= compStack[-1][1]:
                    compStack.pop()
                else:
                    break
            
            if compStack:
                res.append(compStack[-1][0] - i)
            else:
                res.append(0)
            compStack.append((i, temperatures[i]))
        
        return res[::-1]