from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        def max_consecutive(bars):
            bars.sort()
            longest = curr = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    curr += 1
                else:
                    curr = 1
                longest = max(longest, curr)
            return longest + 1  # k bars removed → k+1 length

        maxH = max_consecutive(hBars)
        maxV = max_consecutive(vBars)

        side = min(maxH, maxV)
        return side * side
