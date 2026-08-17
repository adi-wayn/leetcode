# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        max_pq = max(p.val, q.val)
        min_pq = min(p.val, q.val)

        def lca(root: TreeNode, min_pq, max_pq):
            if min_pq <= root.val <= max_pq:
                return root

            if max_pq < root.val:
                return lca(root.left, min_pq, max_pq)
            else:
                return lca(root.right, min_pq, max_pq)
        
        return lca(root, min_pq, max_pq)
        
