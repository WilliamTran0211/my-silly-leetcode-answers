from math import floor, sqrt
from turtle import right
from typing import List


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def check(time):
            total = 0
            for t in workerTimes:
                x = floor(((-1 + sqrt(1 + (8 * time) / t))) / 2)
                total += x
                if total >= mountainHeight:
                    return True
            return False

        low = 0
        high = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        while low < high:
            mid = (high + low) // 2

            if check(mid):
                high = mid
            else:
                low = mid + 1

        return low


print(Solution().minNumberOfSeconds(4, [2, 1, 1]))
