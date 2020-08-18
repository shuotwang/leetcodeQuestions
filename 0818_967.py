def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
    if N == 1:
        return [i for i in range(10)]

    # ans = []
    # def dfs(n: int, num: int):
    #     if n ==
    self.ans = []

    def helper(n: int, num: int):
        if n == 0:
            self.ans.append(num)

        elif n == N:
            for i in range(1, 10):
                helper(n - 1, i)
        else:
            for i in set([-K, K]):
                digit = num % 10 + i
                if 0 <= digit <= 9:
                    helper(n - 1, num * 10 + digit)

    helper(N, None)
    return self.ans