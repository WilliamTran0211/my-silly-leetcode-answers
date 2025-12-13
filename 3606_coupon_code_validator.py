from collections import defaultdict
from typing import List


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:

        import re

        pattern = r"^[a-zA-Z0-9\s_-]+$"  # non special string

        business_name = ["electronics", "grocery", "pharmacy", "restaurant"]

        valid_code = []

        for i, code in enumerate(code):
            business = businessLine[i]
            activated = isActive[i]

            if (
                bool(re.fullmatch(pattern, code))
                and (business in business_name)
                and activated
            ):
                valid_code.append((code, business))
        valid_code = sorted(valid_code, key=lambda x: (x[1], x[0]))

        res = []
        for code, _ in valid_code:
            res.append(code)
        return res

    def validateCoupons2(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:

        def isValid(record):
            return (
                record[0] in valid_business
                and record[2]
                and record[1].replace("_", "a").isalnum()
            )

        valid_business = {"electronics", "grocery", "restaurant", "pharmacy"}

        ans = sorted(filter(isValid, zip(businessLine, code, isActive)))
        return [coupId for _, coupId, _ in ans]


print(
    Solution().validateCoupons(
        code=["P", "j", "x", "c", "j", "C", "G"],
        businessLine=[
            "pharmacy",
            "electronics",
            "invalid",
            "restaurant",
            "electronics",
            "pharmacy",
            "restaurant",
        ],
        isActive=[True, True, False, False, True, False, False],
    )
)
