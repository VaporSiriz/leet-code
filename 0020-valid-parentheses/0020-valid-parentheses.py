class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for alphabat in s:
            if alphabat in pairs:
                if len(stack) == 0:
                    return False
                pair = stack.pop()
                if pairs[alphabat] != pair:
                    return False
            else:
                stack.append(alphabat)
        return len(stack) == 0
            