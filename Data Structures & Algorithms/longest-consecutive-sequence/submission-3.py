class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visit = set(nums)
        res = 0

        for i in nums:
            if i-1 not in visit:
                val = 0
                while i+val in visit:
                    val += 1
                res = max(res, val)

        return res






        