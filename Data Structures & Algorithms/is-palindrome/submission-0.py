class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp_str = []
        for char in s:
            if not char.isalnum():
                continue
            temp_str.append(char)
        new_str = ''.join(temp_str)
        return new_str == new_str[::-1]