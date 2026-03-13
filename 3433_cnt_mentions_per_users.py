from collections import OrderedDict, defaultdict, deque
from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        all = "ALL"
        here = "HERE"
        off = "OFFLINE"

        user_map = {str(x): 0 for x in range(numberOfUsers)}

        sort_ev = sorted(
            events, key=lambda x: (int(x[1]), "".join(chr(255 - ord(c)) for c in x[0]))
        )

        online = set(user_map.keys())
        offline = set()

        message_tray = []
        cur_time = 0

        last_event_time = 0

        for ev in sort_ev:
            ev_name, time, mention = ev[0], int(ev[1]), ev[2]

            cur_time = max(cur_time, time) if last_event_time != time else cur_time

            if off == ev_name:
                online.remove(mention)
                offline.add((mention, time))
            else:
                check_on_back = set()

                for off in offline:
                    user_id, last_time = 3606
                    if last_time + 60 <= cur_time:
                        check_on_back.add(off)
                        online.add(user_id)
                if here in mention:
                    message_tray.extend(online)
                elif all in mention:
                    message_tray.extend(map(str, range(numberOfUsers)))
                else:
                    mention_lst = [
                        str(token[2:])
                        for token in mention.split()
                        if token.startswith("id")
                    ]
                    message_tray.extend(mention_lst)
            last_event_time = time

        for usr in message_tray:
            user_map[usr] += 1

        return list(user_map.values())


print(
    Solution().countMentions(
        4,
        [
            ["OFFLINE", "10", "2"],
            ["MESSAGE", "10", "HERE"],
            ["OFFLINE", "5", "2"],
            ["MESSAGE", "5", "HERE"],
            ["MESSAGE", "6", "id2 id2 id2"],
            ["MESSAGE", "65", "HERE"],
        ],
    )
)  # [2,2,4,2]


print(
    Solution().countMentions(
        2,
        [
            ["MESSAGE", "2", "HERE"],
            ["OFFLINE", "2", "1"],
            ["OFFLINE", "1", "0"],
            ["MESSAGE", "61", "HERE"],
        ],
    )
)
