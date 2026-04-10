class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mappy = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mappy:
                return [mappy[diff], i]
            else:
                mappy[n] = i
        return 0