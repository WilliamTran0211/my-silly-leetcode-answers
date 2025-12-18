from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        prefix = []
        prefix_1 = [0] * (n + 1)
        prefix_0 = [0] * (n + 1)

        total_0 = 0
        total_1 = 0

        for i, p in enumerate(prices):
            prefix.append(strategy[i] * p)

            total_0 += -strategy[i] * p
            prefix_0[i + 1] = total_0

            total_1 += (1 - strategy[i]) * p
            prefix_1[i + 1] = total_1

        best = 0
        half = k // 2

        for l in range(0, n - k + 1):
            delta = (
                prefix_0[l + half] - prefix_0[l] + prefix_1[l + k] - prefix_1[l + half]
            )
            best = max(delta, best)
        return sum(prefix) + best


print(Solution().maxProfit(prices=[4, 2, 8], strategy=[-1, 0, 1], k=2))
