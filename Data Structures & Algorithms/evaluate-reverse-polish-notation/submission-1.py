class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: y - x,
            '*': lambda x, y: x * y,
            '/': lambda x, y: y / x,
        }
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
                continue
            
            x = stack.pop(-1)
            y = stack.pop(-1)
            res = int(operators[token](x, y))
            stack.append(res)
        
        return stack.pop()
            


