class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            j = i +1

            while j <= len(prices) - 1:
                if prices[i] < prices[j]:
                    partial = ( prices[j] - prices[i] )
                    res = max(partial, res)
                j+= 1
        return res