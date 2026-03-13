class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # len_bit = len(bin(n)[2:])
        # mask = (1 << len_bit + 1) - 1
        # bin_out = bin(~(n) & mask)
        # res = bin_out[-len_bit:]
        # return int(res, 2)
        mask = (1 << n.bit_length()) - 1
        return (~n) & mask if n != 0 else 1


# print(Solution().bitwiseComplement(67185))  # 63886
print(Solution().bitwiseComplement(0))
