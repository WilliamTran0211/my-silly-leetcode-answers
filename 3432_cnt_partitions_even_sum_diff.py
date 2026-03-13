from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res = 0
        cut_idx = 1

        while cut_idx <= len(nums) - 1:
            first_part = nums[0:cut_idx]
            sec_part = nums[cut_idx:]

            if abs(sum(first_part) - sum(sec_part)) % 2 == 0:
                res += 1
            cut_idx += 1

        return res


print(Solution().countPartitions([10, 10, 3, 7, 6]))
