# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val > q.val:
            tmp = q
            q = p
            p = tmp

        def dfs(cur):
            if (cur.val > p.val and cur.val < q.val or
                cur.val == p.val and cur.val < q.val or
                cur.val > p.val and cur.val == q.val):
                return cur

            if cur.val < p.val and cur.val < q.val:
                return dfs(cur.right)
            elif cur.val > p.val and cur.val > q.val:
                return dfs(cur.left)

        return dfs(root)
        