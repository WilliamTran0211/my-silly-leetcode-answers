from calendar import c
from collections import defaultdict
from tabnanny import check
from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count_op = 0

        if nums == sorted(nums):
            return count_op

        def cal(check_min_pair):
            for i in range(len(nums) - 1):
                curr_sum = nums[i] + nums[i + 1]
                if curr_sum in check_min_pair:
                    idx_pairs = check_min_pair[curr_sum]
                    if idx_pairs[0] > i:
                        check_min_pair[curr_sum] = (i, i + 1)
                else:
                    check_min_pair[curr_sum] = (i, i + 1)

        while True:
            check_min_pair = defaultdict(list)
            cal(check_min_pair)
            curr_min_sum = min(check_min_pair.keys())
            min_pair = check_min_pair[curr_min_sum]

            nums = nums[: min_pair[0]] + nums[min_pair[1] + 1 :]
            nums.insert(min_pair[0], curr_min_sum)
            count_op += 1

            if nums == sorted(nums):
                break

        return count_op


print(Solution().minimumPairRemoval([1, 1, 4, 4, 2, -4, -1]))  # 5

"""
simulation:
1: 1, 1, 4, 4, 2, -5
2: 1, 1, 4, 4, -3
3: 1, 1, 4, 1
4: 2, 4, 1
5: 2, 5

"""
