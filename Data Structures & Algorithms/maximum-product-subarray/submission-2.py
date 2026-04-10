class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = nums[0]
        

        for i in range(len(nums)):
            holder = nums[i]
            answer = max(holder, answer)
            for j in range(i + 1, len(nums)):
                holder *= nums[j]
                answer = max(holder, answer)

        return answer



        