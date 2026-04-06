class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        profitable = 0

        while j <= len(prices)-1:
            if prices[i] < prices[j]:
                profitable += prices[j] - prices[i]
            i += 1    
            j += 1
        
        return profitable
            
