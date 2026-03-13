from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        check = set()
        res = []
        for i in nums:
            if i not in check:
                check.add(i)
            else:
                check.remove(i)
                res.append(i)

        return res
