from collections import defaultdict
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        str_len = len(strs[0])
        del_col = [False] * str_len
        watching = ["a"] * str_len
        res = 0
        for st in strs:
            for i, c in enumerate(st):
                if del_col[i]:
                    continue
                if watching[i] <= c:
                    watching[i] = c
                else:
                    res += 1
                    del_col[i] = True
        return res


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0

        for i in zip(*strs):
            if list(i) != sorted(i):
                counter += 1

        return counter
