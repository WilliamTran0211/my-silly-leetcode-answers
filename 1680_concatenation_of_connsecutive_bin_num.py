class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        bin_str = ""

        for i in range(1, n + 1):
            bin_str += bin(i)[2:]

        return int(bin_str, 2) % MOD


print(Solution().concatenatedBinary(12))  # 505379714
