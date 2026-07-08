class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []


        def backtrack(oCount, cCount):
            if oCount == cCount == n:
                res.append("".join(stack))
                return

            if oCount < n:
                stack.append("(")
                backtrack(oCount + 1, cCount)
                stack.pop()

            if oCount > cCount:
                stack.append(")")
                backtrack(oCount, cCount + 1)
                stack.pop()

        
        backtrack(0,0)
        return res
            



        