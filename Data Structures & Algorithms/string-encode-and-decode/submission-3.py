class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f"{chr(163)}{len(s)}{chr(165)}{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        output = []
        for idx, char in enumerate(s):
            
            if char != chr(163):
                continue
            
            len_s = []
            
            if char == chr(163):
                i = idx + 1
                while s[i] != chr(165):
                    len_s.append(s[i])
                    i += 1
                    
                len_s = int(''.join(len_s))
                
                word = []
                for c in range(i+1, i+len_s+1):
                    word.append(s[c])
                output.append(''.join(word))
        return output