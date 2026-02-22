class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        count = 1
        
        # Tạo các block độ dài liên tiếp
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        
        groups.append(count)  # block cuối
        
        # Tính kết quả
        res = 0
        for i in range(len(groups) - 1):
            res += min(groups[i], groups[i + 1])
        
        return res