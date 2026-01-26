from collections import defaultdict
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sub_arr = defaultdict(list)
        arr.sort()

        for i in range(len(arr) - 1):
            j = i + 1
            sub = abs(arr[i] - arr[j])
            sub_arr[sub].append([min(arr[i], arr[j]), max(arr[i], arr[j])])

        max_len = 1
        min_key = min(sub_arr.keys())
        for key, lst in sub_arr.items():
            if len(lst) >= max_len:
                min_key = min(min_key, key)

        return list(sub_arr[min_key])


print(Solution().minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))

print(Solution().minimumAbsDifference([40, 11, 26, 27, -20]))

print(
    Solution().minimumAbsDifference(
        [8, -68, -32, -81, 83, 93, -96, 62, -103, -94, -66, 74]
    )
)
