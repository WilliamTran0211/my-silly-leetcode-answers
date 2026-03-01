class Solution:
    def minPartitions(self, n: str) -> int:
        return max(map(lambda x: int(x), list(n)))


print(Solution().minPartitions("27346209830709182346"))
