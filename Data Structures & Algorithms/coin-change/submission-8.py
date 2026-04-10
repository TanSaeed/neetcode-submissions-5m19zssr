class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        answer = [amount + 1] * (amount + 1)
        answer[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a-c >= 0:
                    answer[a] = min(answer[a], 1+answer[a-c])
        return answer[amount] if answer[amount] != amount + 1 else -1
