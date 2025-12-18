from collections import defaultdict, deque
from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)  # prefix sum của dp

        dp[0] = 1
        prefix[0] = 1

        max_dq, min_dq = deque(), deque()

        L = 0

        for i in range(1, n + 1):
            x = nums[i - 1]

            while max_dq and nums[max_dq[-1]] < x:
                max_dq.pop()
            max_dq.append(i - 1)

            while min_dq and nums[min_dq[-1]] > x:
                min_dq.pop()
            min_dq.append(i - 1)

            while nums[max_dq[0]] - nums[min_dq[0]] > k:
                L += 1
                if max_dq[0] < L:
                    max_dq.popleft()
                if min_dq[0] < L:
                    min_dq.popleft()

            dp[i] = (prefix[i - 1] - (prefix[L - 1] if L > 0 else 0)) % mod

            prefix[i] = (prefix[i - 1] + dp[i]) % mod

        return dp[n] % mod


print(Solution().countPartitions([9, 4, 1, 3, 7], 4))
