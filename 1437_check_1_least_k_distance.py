from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_idx = -1

        for i, n in enumerate(nums):
            if n == 1:
                if last_idx == -1:
                    last_idx = i
                else:
                    if (i - (last_idx + 1)) < k:
                        return False
                    else:
                        last_idx = i
        return True


print(Solution().kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2))

print(Solution().kLengthApart([1, 0, 0, 1, 0, 1], 2))

print(Solution().kLengthApart([0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 3))
