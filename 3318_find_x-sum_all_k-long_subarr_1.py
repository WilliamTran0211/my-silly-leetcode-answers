from typing import List
from collections import Counter, defaultdict


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []

        for i in range(len(nums) - k + 1):
            count = Counter(nums[i : i + k])

            if len(count) <= x:
                res.append(sum(nums[i : i + k]))
            else:
                pairs = list(count.items())
                pairs.sort(key=lambda p: (p[1], p[0]), reverse=True)

                cur_sum = 0

                for num, cnt in pairs[:x]:
                    cur_sum += num * cnt

                res.append(cur_sum)

        return res


print(Solution().findXSum([3, 8, 7, 8, 7, 5], 2, 2))
