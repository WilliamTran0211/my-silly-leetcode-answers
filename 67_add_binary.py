class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a, 2)
        num_b = int(b, 2)
        return str(bin((num_a + num_b))[2:])


print(Solution().addBinary("11", "1"))
