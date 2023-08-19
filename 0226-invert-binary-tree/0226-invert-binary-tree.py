# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def changeChilds(self, root: Optional[TreeNode]):
        left = root.left
        right = root.right
        root.left = right
        root.right = left
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.left:
                root.left = self.invertTree(root.left)
            if root.right:
                root.right = self.invertTree(root.right)
            self.changeChilds(root)
        return root