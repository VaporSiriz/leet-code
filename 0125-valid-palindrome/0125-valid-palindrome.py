class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check_ord(char: str) -> bool:
            ord_char = ord(char)
            return not ((97 <= ord_char and ord_char <= 122) or \
                (48 <= ord_char and ord_char <= 57))
        s = list(s.lower())
        i = 0
        j = len(s)-1
        while i<=j:
            while i<=j:
                if check_ord(s[i]):
                    i += 1
                else:
                    break
            while i<=j:
                if check_ord(s[j]):
                    j -= 1
                else:
                    break
            
            if i<=j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
        return True