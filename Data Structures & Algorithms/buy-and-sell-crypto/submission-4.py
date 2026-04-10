class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        answer = 0 

        while r < len(prices):
            if prices[l] < prices[r]:
                answer = max((prices[r] - prices[l]), answer)
            else:
                l = r
            r += 1

        return answer