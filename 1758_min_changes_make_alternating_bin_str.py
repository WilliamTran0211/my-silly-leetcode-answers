class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        case_0 = ["01"] * (n // 2)
        case_1 = ["10"] * (n // 2)

        if n % 2 != 0:
            case_0.append("0")
            case_1.append("1")

        str_0 = "".join(case_0)
        str_1 = "".join(case_1)

        dff_0 = 0
        dff_1 = 0
        for i in range(n):

            if s[i] != str_0[i]:
                dff_0 += 1

            if s[i] != str_1[i]:
                dff_1 += 1

        return min(dff_0, dff_1)


print(Solution().minOperations("100101000"))
