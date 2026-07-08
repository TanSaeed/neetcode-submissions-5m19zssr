class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))

        for n1 in range(len(num1)):
            for n2 in range(len(num2)):
                digit = int(num1[n1]) * int(num2[n2])

                res[n1+n2] += digit

                res[n1+n2+1] += res[n1+n2] // 10
                res[n1+n2] = res[n1+n2] % 10

        beg = 0
        res = res[::-1]

        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])
        return "".join(res)


