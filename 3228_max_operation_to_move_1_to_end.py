class Solution:
    def maxOperations(self, s: str) -> int:
        count_1 = 0
        res = 0
        i = 0
        while i < len(s):
            if s[i] == "1":
                count_1 += 1
            elif s[i] == "0":
                res += count_1
                while i + 1 < len(s) and s[i + 1] == "0":
                    i += 1
            i += 1
        return res


print(Solution().maxOperations("0011010101100"))
