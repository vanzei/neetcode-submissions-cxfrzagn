class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        maxP = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                maxP = max(maxP, prices[j] - prices[i])
                j+= 1
            else:
                i = j
                j += 1
        return maxP



        