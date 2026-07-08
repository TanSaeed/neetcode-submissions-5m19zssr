class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        dp[0] = 1

        for i in range(len(nums)):
            nextDP = defaultdict(int)
            for curs, count in dp.items():
                nextDP[curs + nums[i]] += count
                nextDP[curs - nums[i]] += count
            dp = nextDP
        return nextDP[target]

