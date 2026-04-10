class Solution:
    def rob(self, nums: List[int]) -> int:


        def robber(i):
            rob1, rob2 = 0, 0

            for n in i:
                tmp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = tmp

            return rob2

        return max(nums[0], robber(nums[1:]), robber(nums[:-1]))