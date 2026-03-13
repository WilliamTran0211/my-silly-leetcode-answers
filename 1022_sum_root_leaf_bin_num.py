from typing import Optional

from leetcode_utils import TreeNode, utils


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        his = []

        def get_bin(his, root, tmp, is_left=False):
            if root:
                tmp.append(str(root.val))
                if root.left and root.left.val is not None:
                    get_bin(his, root.left, tmp, is_left=True)
                if root.right and root.right.val is not None:
                    get_bin(his, root.right, tmp, is_left=False)
                if root.left is None and root.right is None:
                    his.append(int(("".join(tmp)),2))
                tmp.pop(-1)

        get_bin(his, root, tmp=[], is_left=False)
        return sum(his)


print(Solution().sumRootToLeaf(utils.build_binary_tree([1, 0, 1, 0, 1, 0, 1])))
