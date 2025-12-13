from collections import defaultdict
import heapq
from typing import List


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        res = []
        adj = defaultdict(list)
        for start, dest in connections:
            adj[start].append(dest)
            adj[dest].append(start)

        online = set()
        station_grp = {}
        min_heaps = defaultdict(list)

        def dfs(station, group_id):
            if station in online:
                return
            online.add(station)
            station_grp[station] = group_id
            heapq.heappush(min_heaps[group_id], station)

            for nei in adj[station]:
                dfs(nei, group_id)

        i = 0
        for s in range(1, c + 1):
            dfs(s, s)

        for q_type, q_station in queries:
            if q_type == 1:
                if q_station in online:
                    res.append(q_station)
                    continue
                group_id = station_grp[q_station]
                min_heap = min_heaps[group_id]
                while min_heap and min_heap[0] not in online:
                    heapq.heappop(min_heap)
                if min_heap:
                    res.append(min_heap[0])
                else:
                    res.append(-1)
            else:
                online.discard(q_station)

        return res


print(
    Solution().processQueries(
        6,
        [[1, 2], [2, 3], [3, 4], [4, 5]],
        [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2], [2, 6], [1, 6]],
    )
)
