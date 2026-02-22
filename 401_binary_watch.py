from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for hour in range(12):
            # Duyệt tất cả phút có thể
            for minute in range(60):
                # Đếm số bit 1
                if bin(hour).count("1") + bin(minute).count("1") == turnedOn:
                    # Format kết quả
                    result.append(f"{hour}:{minute:02d}")

        return result
