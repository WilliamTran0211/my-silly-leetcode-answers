from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        check = []
        for n in nums:
            check.append(str(n))
            bin = "".join(check)
            if int(bin, 2) % 5 == 0:
                res.append(True)
            else:
                res.append(False)

        return res


print(Solution().prefixesDivBy5([0, 1, 1]))
