class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        output = []

        for i, c in enumerate(s):
            last[c] = i

        curM = 0
        lastP = 0
        for i, c in enumerate(s):
            curM += 1
            lastP = max(lastP, last[c])

            if i == lastP:
                output.append(curM)
                curM = 0

        return output


        