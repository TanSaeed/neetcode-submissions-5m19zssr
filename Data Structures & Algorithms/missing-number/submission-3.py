class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = len(nums)

        for i in range(len(nums)):
            answer += (i - nums[i])
        return answer

