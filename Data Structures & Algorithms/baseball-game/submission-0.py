class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            match operation:
                case '+':
                    a = stack[-1]
                    b = stack[-2]
                    stack.append(a+b)
                case 'D':
                    stack.append(stack[-1] * 2)
                case 'C':
                    stack.pop()
                case _:
                    stack.append(int(operation))
        
        return sum(stack)