class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n:
            visit.add(n)
            n = self.finder(n)

            if n == 1:
                return True
            if n in visit:
                return False

    def finder(self, n):
        output = 0

        while n:
            dig = n % 10
            n = n // 10
            dig = dig * dig
            output += dig
        return output
