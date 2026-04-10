class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappy = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in mappy:
                if stack and stack[-1] == mappy[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        