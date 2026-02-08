from turtle import left
from typing import Optional

from leetcode_utils import TreeNode, utils


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):

            if not node:
                return (True, 0)

            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)
            
            current_balanced = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
            )

            current_height = 1 + max(left_height, right_height)

            return (current_balanced, current_height)

        balanced, _ = dfs(root)
        return balanced


# root = utils.build_binary_tree([3, 9, 20, None, None, 15, 7])
# print(Solution().isBalanced(root))

root = utils.build_binary_tree(
    [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, None, None, 5, 5]
)
print(Solution().isBalanced(root))
