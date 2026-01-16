from typing import List


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        MOD = 10**9 + 7

        hFences = sorted([1] + hFences + [m])
        vFences = sorted([1] + vFences + [n])

        h_length = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_length.add(hFences[j] - hFences[i])

        v_length = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_length.add(vFences[j] - vFences[i])

        common = h_length.intersection(v_length)

        if not common:
            return -1

        side = max(common)

        return (side * side) % MOD


print(Solution().maximizeSquareArea(m=4, n=3, hFences=[2, 3], vFences=[2]))
