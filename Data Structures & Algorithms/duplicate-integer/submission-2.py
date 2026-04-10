class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        ourSet = set()

        for i in range(len(nums)):
            if nums[i] in ourSet:
                return True
            else:
                ourSet.add(nums[i])

        return False
        