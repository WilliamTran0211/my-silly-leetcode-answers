from collections import defaultdict
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return -1

        # abs(i - j) + abs(j - k) + abs(k - i) = (j-i) + (k-j) + (k-i) = j - i + j - k + k - i = 2k - 2i = 2(k-i)

        his = defaultdict(list)

        for i, n in enumerate(nums):
            his[n].append(i)

        ans = float("inf")

        for key, val in his.items():
            if len(val) >= 3:
                for i in range(len(val) - 2):
                    cal = 2 * (val[i + 2] - val[i])
                    ans = min(ans, cal)
        return ans if ans != float("inf") else -1


print(Solution().minimumDistance([1, 1, 2, 1, 2, 1, 1]))
