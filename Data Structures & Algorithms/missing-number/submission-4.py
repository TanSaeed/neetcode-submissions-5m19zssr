class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = len(nums)
        a,b = 0, 0


        for i in range(len(nums)):
            a += i
            b += nums[i]

        a += len(nums)
        return (a - b)