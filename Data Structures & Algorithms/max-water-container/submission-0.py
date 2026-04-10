class Solution:
    def maxArea(self, heights: List[int]) -> int:

        answer = 0

        l, r = 0 , len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            answer = max(area, answer)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1

        return answer
        