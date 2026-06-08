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
                cur.val == q.val and cur.val > p.val
            ):
                return cur

            if cur.val > p.val and cur.val > q.val:
                return dfs(cur.left)
            elif cur.val < p.val and cur.val < q.val:
                return dfs(cur.right)

        return dfs(root)

        
        