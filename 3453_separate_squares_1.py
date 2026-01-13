from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        def check_area(line):
            above = below = 0

            for x, yi, l in squares:
                if yi + l <= line:
                    below += l * l
                elif yi >= line:
                    above += l * l
                else:
                    below += l * (line - yi)
                    above += l * (yi + l - line)

            return above - below

        # apply binary search
        low = min(yi for _, yi, _ in squares)
        high = max(yi + l for _, yi, l in squares)

        for _ in range(60):
            mid = (low + high) / 2
            if check_area(mid) > 0:
                low = mid
            else:
                high = mid
        return (low + high) / 2
