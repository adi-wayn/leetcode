class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        open_close = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        if s[0] in open_close.values():
            return False

        stack = []

        for i in range(len(s)):
            if stack and s[i] == open_close.get(stack[-1], ''):
                stack.pop()
            else:
                stack.append(s[i])
        
        return not stack
