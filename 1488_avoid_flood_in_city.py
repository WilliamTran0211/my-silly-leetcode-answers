from typing import List
from collections import defaultdict
import heapq


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n

        # map: hồ -> ngày mưa tiếp theo
        next_rain = {}
        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in next_rain:
                    next_rain[lake].append(i)
                else:
                    next_rain[lake] = [i]

        # heap lưu (ngày_mưa_tiếp_theo, hồ)
        heap = []
        full = set()

        for i, lake in enumerate(rains):
            if lake > 0:  # hôm nay mưa
                if lake in full:
                    # hồ này đã đầy mà chưa khô -> ngập
                    return []
                full.add(lake)
                ans[i] = -1
                # bỏ ngày hôm nay ra khỏi danh sách mưa
                next_rain[lake].pop(0)
                # nếu còn mưa lại sau này, đẩy vào heap
                if next_rain[lake]:
                    heapq.heappush(heap, (next_rain[lake][0], lake))

            else:  # hôm nay không mưa -> có thể làm khô
                if heap:
                    # chọn hồ có ngày mưa gần nhất
                    day, l = heapq.heappop(heap)
                    ans[i] = l
                    full.remove(l)
                else:
                    # nếu không cần làm khô hồ nào, làm khô tùy ý
                    ans[i] = 1

        return ans


print(Solution().avoidFlood([1, 2, 0, 1, 0, 2]))
