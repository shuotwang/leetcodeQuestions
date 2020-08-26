class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 366 days
        #         durations = [1, 7, 30]
        #         memo = {}

        #         def dp(i):
        #             if i > 365:
        #                 return 0

        #             if i in memo:
        #                 return memo[i]

        #             if i in days:
        #                 ans = min(dp(i+d)+c for c, d in zip(costs, durations))
        #             else:
        #                 ans = dp(i+1)

        #             memo[i] = ans
        #             return ans

        #         return dp(1)

        #   based on actual days
        durations = [1, 7, 30]
        memo = {}

        def dp(i):
            if i >= len(days):
                return 0

            if i in memo:
                return memo[i]

            j = i
            ans = float('inf')
            for c, d in zip(costs, durations):
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)

            memo[i] = ans
            return ans

        return dp(0)
