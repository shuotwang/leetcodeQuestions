class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefix = [0]
        maxl = maxm = summ = 0
        for x in A:
            prefix.append(prefix[-1] + x)

        for x in range(M, len(prefix) - L):
            maxm = max(maxm, prefix[x] - prefix[x - M])
            summ = max(summ, maxm + prefix[x + L] - prefix[x])

        for x in range(L, len(prefix) - M):
            maxl = max(maxl, prefix[x] - prefix[x - L])
            summ = max(summ, maxl + prefix[x + M] - prefix[x])

        return summ

#         L_list, M_list= [], []

#         na = len(A)
#         for i in range(na):
#             if i + L <= na:
#                 L_list.append(sum(A[i: i+L]))
#             if i + M <= na:
#                 M_list.append(sum(A[i: i+M]))
#         print(L_list, M_list)

#         ans = float('-inf')
#         for i in range(na):
#             temp1, temp2 = 0, 0
#             if i - L + 1 > 0 and i < len(M_list):
#                 temp1 = max(L_list[:i-L+1]) + max(M_list[i:])
#             if i - M + 1 > 0 and i < len(L_list):
#                 temp2 = max(M_list[:i-M+1]) + max(L_list[i:])

#             if temp1 and temp2:
#                 temp = max(temp1, temp2)
#             else:
#                 temp = temp1 if temp1 else temp2
#             ans = max(ans, temp)

#         return ans