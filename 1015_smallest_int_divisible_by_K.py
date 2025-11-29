class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # repunit là số chỉ có số 1 và chia hết cho 1 số nào đó
        # Muốn thêm chữ số 1 vào cuối số, chỉ cần nhân số đó với 10 rồi cộng thêm 1
        if k % 2 != 0 and k % 5 != 0:
            res = 0
            r = 0
            check = set()
            while True:
                r = (r * 10 + 1) % k
                res += 1

                if r == 0:
                    break
                if r in check:
                    return -1
                else:
                    check.add(r)

            return res

        return -1


print(Solution().smallestRepunitDivByK(3))
print(Solution().smallestRepunitDivByK(17))
print(Solution().smallestRepunitDivByK(21))
print(Solution().smallestRepunitDivByK(15))
print(Solution().smallestRepunitDivByK(47))
