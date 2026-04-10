class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        ourSet = set()

        for n in nums:
            if n in ourSet:
                return True
            else:
                ourSet.add(n)
        return False