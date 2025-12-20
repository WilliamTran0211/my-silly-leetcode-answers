from typing import List
from collections import defaultdict


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        check = defaultdict(list)

        for i in range(len(colors) - 1):
            j = i + 1
            if colors[i] == colors[j]:
                check[colors[i]].append(neededTime[i])
                if j == len(colors) - 1:
                    check[colors[i]].append(neededTime[j])
            else:
                if colors[i] in check:
                    check[colors[i]].append(neededTime[i])
                    time = check[colors[i]]
                    time.sort(reverse=True)
                    res += sum(time[1:])
                    check.pop(colors[i])
                else:
                    continue
        if check:
            _, rest = check.popitem()
            rest.sort(reverse=True)
            res += sum(rest[1:])
        return res


print(Solution().minCost("aabaa", [1, 2, 3, 4, 1]))

print(
    Solution().minCost(
        "zzzzaaayyyxxx", [9999, 10000, 9998, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
)
