class Solution:
    def maxArea(self, heights: List[int]) -> int:

        answer = 0

        l, r = 0, len(heights)-1

        while l < r:
            curC = min(heights[l], heights[r]) * (r - l)
            answer = max(curC, answer)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return answer