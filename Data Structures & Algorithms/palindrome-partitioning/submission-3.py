class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        pal = []


        def dfs(i):
            if i >= len(s):
                res.append(pal.copy())
                return

            for j in range(i, len(s)):
                con = self.isPal(i, j, s)
                if con:
                    pal.append(s[i:j+1])
                    dfs(j+1)
                    pal.pop()

        dfs(0)
        return res

    def isPal(self, l,r,w):
        while l < r:
            if w[l] != w[r]:
                return False
            l += 1
            r -= 1

        return True
        