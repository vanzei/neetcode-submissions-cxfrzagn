class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)

        dp[len(cost) - 1] = cost[-1]
        dp[len(cost)- 2] = cost[-2]

        for n in range(len(cost)-3, -1, -1):
            dp[n] = min(dp[n+1], dp[n+2]) + cost[n]
        return min(dp[0], dp[1])
