from collections import defaultdict
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        check = defaultdict(list)
        for n in arr:
            count_1 = bin(n)[2:].count("1")
            check[count_1].append(n)

        cnt_1_lst = sorted(check.keys())
        res = []
        for n in cnt_1_lst:
            list_num = check[n]

            list_num.sort()
            res.extend(list_num)
        return res


print(Solution().sortByBits([1, 1]))  # [0,1,2,4,8,3,5,6,7]
print(Solution().sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
