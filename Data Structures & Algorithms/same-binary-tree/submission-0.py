# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        p_tree = []
        q_tree = []

        def dfs(node, tree_list):
            if node is None:
                tree_list.append(None)
                return

            tree_list.append(node.val)

            dfs(node.left, tree_list)
            dfs(node.right, tree_list)

            return tree_list

        p_tree = dfs(p, p_tree)
        q_tree = dfs(q, q_tree)

        return True if p_tree == q_tree else False

