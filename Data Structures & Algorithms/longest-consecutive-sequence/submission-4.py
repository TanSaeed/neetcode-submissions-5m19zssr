class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums) 
        res = 0

        for i in n:
            if not i-1 in n:
                val = 0
                while i+val in n:
                    val += 1
                res = max(res,val)

        return res





        