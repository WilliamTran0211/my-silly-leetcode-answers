from typing import Optional
from leetcode_utils import TreeNode, utils


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        tìm sub tree chứa tất cả các node sâu nhất
        """
        if not root.left and not root.right:
            return root

        self.res = None
        self.res_level = -1

        def dfs(current):
            if not current:
                return None, 0
            left_tree, left_lvl = dfs(current.left)
            right_tree, right_lvl = dfs(current.right)

            if left_lvl > right_lvl:
                return left_tree, left_lvl + 1
            if right_lvl > left_lvl:
                return right_tree, right_lvl + 1

            return current, left_lvl + 1

        return dfs(root)[0]


print(
    "ans",
    Solution().subtreeWithAllDeepest(
        utils.build_binary_tree([3, 5, 1, 6, 2, 0, 8, 9, 10, 7, 4])
    ),
)  # [5,6,2,9,10,7,4]


print(
    "ans",
    Solution().subtreeWithAllDeepest(
        utils.build_binary_tree(
            [3, 5, 1, 6, 2, 0, 8, 9, 10, 7, 4, None, None, None, None, None, None, 11]
        )
    ),
)
