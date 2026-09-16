class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        keys = {')':'(', ']':'[','}':'{'}
        for c in s:
            if c in keys:
                if not stack:
                    return False
                if keys[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)

        return not stack