class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1

        profitables = 0
        while j <= len(prices) - 1:
            if prices[i] > prices[j]:
                i += 1
                j += 1
                continue
            else:
                profitables += prices[j] - prices[i]
                i += 1
                j += 1
        return profitables
        