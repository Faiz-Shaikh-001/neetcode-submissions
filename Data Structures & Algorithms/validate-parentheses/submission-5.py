class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        
        for char in s:
            if char not in ')]}':
                stack.append(char)
                continue
            
            if len(stack) < 1:
                return False

            last_char = stack.pop(-1)
            if char == ')' and last_char != '(':
                return False
            elif char == ']' and last_char != '[':
                return False
            elif char == '}' and last_char != '{':
                return False
        if len(stack) != 0:
            return False
        
        return True



            