from typing import List
from collections import Counter


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = Counter(x % value for x in nums)
        mex = 0
        while True:
            r = mex % value
            if cnt[r] > 0:
                cnt[r] -= 1
                mex += 1
            else:
                return mex


print(Solution().findSmallestInteger([1, -10, 7, 13, 6, 8], 5))
