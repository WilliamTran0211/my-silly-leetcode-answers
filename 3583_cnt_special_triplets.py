from collections import defaultdict
from typing import Counter, List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        # MOD = 10**9 - 7
        # res = 0
        # for i in range(len(nums) - 1):
        #     n = nums[i]
        #     if n % 2 == 0 or n == 1:
        #         find_mid = n // 2
        #         for j in range(i + 1, len(nums)):
        #             m = nums[j]
        #             if find_mid == m:
        #                 rest_nums = nums[j + 1 :]
        #                 res += rest_nums.count(n)
        #             else:
        #                 continue

        # return res % MOD
        MOD = 10**9 + 7
        num_cnt = Counter(nums)
        num_partial_cnt = defaultdict(int)

        ans = 0
        for v in nums:
            target = v * 2
            l_cnt = num_partial_cnt[target]
            num_partial_cnt[v] += 1

            r_cnt = num_cnt[target] - num_partial_cnt[target]
            ans = (ans + l_cnt * r_cnt) % MOD

        return ans


print(Solution().specialTriplets([8, 4, 2, 8, 4, 1, 3, 2, 8]))

print(Solution().specialTriplets([84, 2, 93, 1, 2, 2, 26]))  # 2
