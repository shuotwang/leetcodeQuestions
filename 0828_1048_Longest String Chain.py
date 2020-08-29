class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        hashmap = collections.defaultdict(list)
        dp = collections.defaultdict(int)

        N = len(words)
        for each in words:
            hashmap[len(each)] += [each]

        for i in range(1, 17):
            for w in hashmap[i]:
                ans = 1
                for k in range(i):
                    nw = w[:k] + w[k + 1:]
                    ans = max(ans, dp[nw] + 1)
                dp[w] = ans

        return max(dp.values())
