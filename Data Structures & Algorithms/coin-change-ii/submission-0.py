class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) -1, -1, -1):
            nxtdp = [0] * (amount + 1)
            nxtdp[0] = 1

            for j in range(1, amount + 1):
                nxtdp[j] = dp[j]
                if j - coins[i] >=0:
                    nxtdp[j] += nxtdp[j - coins[i]]
            dp = nxtdp
        
        return dp[amount]


