class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n and n not in visit:
            visit.add(n)
            n = self.numsq(n)

            if n == 1:
                return True
        return False


    def numsq(self, n):
        output = 0

        while n:
            dig = n % 10
            n = n // 10
            dig = dig * dig
            output += dig

        return output

        