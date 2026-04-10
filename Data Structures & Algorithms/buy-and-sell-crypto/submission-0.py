class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                answer = max(prices[j] - prices[i], answer)

        return answer

        