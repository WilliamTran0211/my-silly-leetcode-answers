from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        n = len(source)

        rules = defaultdict(list)
        for i in range(len(original) - 1):
            l = len(original[i])
            rules[l].append((original[i], changed[i], cost[i]))

        dp = [inf] * (n + 1)
        dp[0] = 0

        for i in range(0, n - 1):
            if dp[i] == inf:
                continue

            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            for l in rules:
                if i + l > n:
                    continue

                src_sub = source[i : i + l]
                tgt_sub = target[i : i + l]

                for orig, chg, cst in rules[l]:
                    if src_sub == orig and tgt_sub == chg:
                        dp[i + l] = min(dp[i + l], dp[i] + cst)

        return -1 if dp[n] == inf else dp[n]


print(
    Solution().minimumCost(
        source="abcdefgh",
        target="acdeeghh",
        original=["bcd", "fgh", "thh"],
        changed=["cde", "thh", "ghh"],
        cost=[1, 3, 5],
    )
)
