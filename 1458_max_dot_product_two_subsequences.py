from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """
        sub1 = [x1, x2, x3]
        sub2 = [y1, y2, y3]

        dot product = x1*y1 + x2*y2 + x3*y3
        """
        inf = float("inf")
        n, m = len(nums1), len(nums2)
        dp = [[-inf] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = max(
                    nums1[i - 1] * nums2[j - 1] + max(0, dp[i - 1][j - 1]),
                    dp[i - 1][j],
                    dp[i][j - 1],
                )
        return dp[n][m]


print(Solution().maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]))
