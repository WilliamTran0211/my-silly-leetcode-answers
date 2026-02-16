class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:]
        binary_32_bit = binary_str.zfill(32)
        return int(binary_32_bit[::-1], 2)


print(Solution().reverseBits(43261596))  # 964176192
