from typing import List
from collections import Counter, defaultdict


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        max_val = max(power)
        count = defaultdict(int)
        for p in power:
            count[p] += p  # hoặc cộng nhiều lần nếu trùng

        dp = {}
        sorted_keys = sorted(count.keys())
        dp[sorted_keys[0]] = count[sorted_keys[0]]

        for i in range(1, len(sorted_keys)):
            d = sorted_keys[i]
            prev = sorted_keys[i - 1]

            # tìm damage nhỏ hơn d-2
            j = i - 1
            while j >= 0 and sorted_keys[j] >= d - 2:
                j -= 1
            dp[d] = max(dp[prev], count[d] + (dp[sorted_keys[j]] if j >= 0 else 0))

        return dp[max_val]


print(Solution().maximumTotalDamage([2, 3, 4, 8, 10]))
