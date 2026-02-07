import functools
from typing import List
from collections import defaultdict


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:

        dp = defaultdict(int)

        @functools.lru_cache(None)
        def dfs(i, state, t):
            if i == len(prices) or t == k:
                return 0
            if (i, state, t) in dp:
                return dp[(i, state, t)]

            p = prices[i]

            if state == 0:  # empty
                return max(
                    dfs(i + 1, 0, t),        # không làm gì
                    dfs(i + 1, 1, t) - p,    # mở long
                    dfs(i + 1, 2, t) + p     # mở short
                )

            if state == 1:  # long
                return max(
                    dfs(i + 1, 1, t),        # giữ long
                    dfs(i + 1, 0, t + 1) + p # bán → đóng long
                )

            if state == 2:  # short
                return max(
                    dfs(i + 1, 2, t),        # giữ short
                    dfs(i + 1, 0, t + 1) - p # mua → đóng short
                )

        res = dfs(0, 0, 0)
        return res


print(Solution().maximumProfit([12, 16, 19, 19, 8, 1, 19, 13, 9], 3))
