class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        output = []

        for i, c in enumerate(s):
            last[c] = i

        size = 0
        end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(last[c], end)

            if i == end:
                output.append(size)
                size = 0

        return output
            


        