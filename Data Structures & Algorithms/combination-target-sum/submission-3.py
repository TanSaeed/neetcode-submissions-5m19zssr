class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(i, carry, total):
            if total == target:
                res.append(carry.copy())
                return

            if i >= len(nums) or total > target:
                return

            carry.append(nums[i])
            dfs(i, carry, total + nums[i])

            carry.pop()
            dfs(i + 1, carry, total)


        dfs(0, [], 0)

        return res


        