from collections import defaultdict
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        cnt = defaultdict(list)

        for i in range(n):
            cnt[nums[i]].append(i)

        for idx_lst in cnt.values():
            m = len(idx_lst)
            total = sum(idx_lst)

            left_sum = 0

            for j in range(m):
                i = idx_lst[j]

                # left
                left = i * j - left_sum

                # right
                right = (total - left_sum - i) - i * (m - j - 1)

                ans[i] = left + right

                left_sum += i

        return ans


print(
    Solution().distance([1, 3, 1, 1, 2, 2, 1, 3, 4, 5, 6, 7, 7, 1, 1, 9, 3])
)  # [38,21,30,28,1, 1,28, 15,0, 0, 0, 1, 1, 42,46,0,24]
