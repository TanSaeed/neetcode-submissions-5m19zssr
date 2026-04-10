class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        answer = 0


        for n in numSet:
            if n-1 not in numSet:
                currentL = 0
                while n+currentL in numSet:
                    currentL += 1
                answer = max(answer,currentL)
        return answer