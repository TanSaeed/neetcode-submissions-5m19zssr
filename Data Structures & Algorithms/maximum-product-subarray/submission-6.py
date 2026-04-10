class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        answer = nums[0]

        for n in nums:
            tmp = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * tmp, n * curMin, n)

            answer = max(curMax, answer)

        return answer

        