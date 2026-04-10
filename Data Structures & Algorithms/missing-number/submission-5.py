class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = len(nums)
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            answer += i

        return answer - total 
        