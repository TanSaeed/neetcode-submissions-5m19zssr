class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) / 2

        for i in range(len(nums) -1, -1, -1):
            dpCopy = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                dpCopy.add(t)
                dpCopy.add(t + nums[i])
            dp = dpCopy
        return False


