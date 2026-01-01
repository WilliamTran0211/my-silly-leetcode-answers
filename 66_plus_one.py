from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        res = [0] * n
        remember = 0
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                if digits[i] == 9:
                    res[i] = 0
                    remember = 1
                else:
                    res[i] = digits[i] + 1
            else:
                if remember != 0:
                    if digits[i] == 9:
                        res[i] = 0
                        remember = 1
                    else:
                        res[i] = digits[i] + 1
                        remember = 0
                else:
                    res[i] = digits[i]

        if remember != 0:
            res.insert(0, 1)

        return res

    def plusOne2(self, digits: List[int]) -> List[int]:
        astr = int("".join([str(i) for i in digits])) + 1
        return [int(i) for i in str(astr)]


print(Solution().plusOne([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
