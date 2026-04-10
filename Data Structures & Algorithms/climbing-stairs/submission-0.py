class Solution:
    def climbStairs(self, n: int) -> int:
        v1, v2 = 1, 1

        for i in range(n-1):
            tmp = v1
            v1 = v1 + v2
            v2 = tmp

        return v1




        