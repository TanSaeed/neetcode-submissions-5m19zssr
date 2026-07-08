class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappy = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "qprs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        res = []

        sub = []
        def dfs(i, sub):
            if i >= len(digits):
                res.append(sub)
                return

            for c in mappy[digits[i]]:
                dfs(i+1, sub + c )

        if digits:
            dfs(0, "")
        return res



        