class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(oCount, cCount):
            if oCount == cCount == n:
                res.append("".join(stack))
                return


            if oCount < n:
                stack.append("(")
                dfs(oCount + 1, cCount)
                stack.pop()

            if oCount > cCount:
                stack.append(")")
                dfs(oCount, cCount + 1)
                stack.pop()

        
        dfs(0,0)
        return res



        