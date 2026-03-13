class Solution:
    def smallestNumber(self, n: int) -> int:
        tmp = []
        while n > 0:
            tmp.append(n % 2)
            n = n // 2
        str_res = "".join(["1"] * len(tmp))
        return int(str_res, 2)


print(Solution().smallestNumber(5))
