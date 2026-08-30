class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
                continue
            
            temp = []
            while stack and stack[-1] != '[':
                temp.append(stack.pop())
            
            temp = temp[::-1]

            currStr = ''.join(temp)
            stack.pop()
            mulitiplier = ''
            while stack and stack[-1].isdigit():
                mulitiplier += stack.pop()
            
            multiplier = int(mulitiplier[::-1])
            str_to_append = currStr * multiplier
            stack.append(str_to_append)

        return ''.join(stack) 
