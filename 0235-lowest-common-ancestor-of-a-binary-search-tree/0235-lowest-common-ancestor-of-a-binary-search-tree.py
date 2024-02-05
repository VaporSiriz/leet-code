# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 1. 내려가면서 list 형태로 더하기?
    def find_node(
        self,
        node: 'TreeNode', 
        target: 'TreeNode',
        ancestors: list
    ) -> list:
        if node == target:
            ancestors.append(node)
            return ancestors
        if node.left:
            left = self.find_node(node.left, target, ancestors)
            if len(left)>0:
                ancestors.append(node)
                return ancestors
        if node.right:
            right = self.find_node(node.right, target, ancestors)
            if len(right)>0:
                ancestors.append(node)
                return ancestors
        return []

    def lowestCommonAncestor(
        self, 
        root: 'TreeNode', 
        p: 'TreeNode', 
        q: 'TreeNode'
    ) -> 'TreeNode':
        pOfAncestors = self.find_node(root, p, [])
        qOfAncestors = self.find_node(root, q, [])
        for pOfAncestor in pOfAncestors:
            for qOfAncestor in qOfAncestors:
                if pOfAncestor is qOfAncestor:
                    return pOfAncestor
        