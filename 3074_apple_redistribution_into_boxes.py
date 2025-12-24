from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apple = sum(apple)

        capacity.sort(reverse=True)
        res = 0
        for cap in capacity:
            if total_apple > 0:
                total_apple -= cap
                res += 1

        return res


print(Solution().minimumBoxes(apple=[1, 3, 2], capacity=[4, 3, 1, 5, 2]))
