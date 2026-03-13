class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        if n == 0:
            return 1

        str_num = list(str(n))

        arr = [0] * len(str_num)

        min_num = 1
        candidate = []
        for i in range(min_num, len(arr) - 1):
                
            candidate.extend([i] * i)

        return int("".join(map(str, arr)))


print(Solution().nextBeautifulNumber(10000))
