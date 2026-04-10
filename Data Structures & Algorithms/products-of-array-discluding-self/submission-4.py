class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix = nums[i] * prefix

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            answer[i] = answer[i] * postfix
            postfix = nums[i] * postfix

        return answer