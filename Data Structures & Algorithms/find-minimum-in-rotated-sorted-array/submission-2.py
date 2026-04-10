class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        answer = nums[0]


        while l <= r:
            if nums[l] < nums[r]:
                answer = min(nums[l], answer)
                break

            m = (r + l) // 2
            answer = min(nums[m], answer)

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return answer

        