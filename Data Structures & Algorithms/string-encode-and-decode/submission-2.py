class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = []
        for s in strs:
            final_str.append(f"{len(s)}#")
            final_str.append(s)
        return ''.join(final_str)
            
        
    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        length = ''
        while index < len(s):
            if s[index].isdigit():
                length += s[index]
                index += 1
            if s[index] == '#':
                length = int(length) + index + 1
                temp_str = s[index+1: length]
                index = length
                length = ''
                res.append(temp_str)
        
        return res
