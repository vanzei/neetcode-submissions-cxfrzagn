class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n+1)
        if n < 2:
            return 1

        for x in range(n-2,-1,-1):
            print(x)
            dp[x] = dp[x+1]+dp[x+2]
            
        print(dp)
        return dp[0]

        