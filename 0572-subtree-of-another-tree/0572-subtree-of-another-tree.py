# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check_same_tree(r: Optional[TreeNode], sr: Optional[TreeNode]) -> bool:
            if not r and not sr:
                return True
            # print(f"{r.val} ?= {sr.val}")
            if not r or not sr:
                return False
            
            if r.val == sr.val:
                left = check_same_tree(r.left, sr.left)
                right = check_same_tree(r.right, sr.right)
                return left and right
            else:
                return False
        queue = [root]
        while len(queue)!=0:
            # print(f"queue : {queue}")
            node = queue.pop(0)
            # print(f"node : {node.val}")
            if node.val == subRoot.val:
                is_same_tree = check_same_tree(node, subRoot)
                if is_same_tree:
                    return is_same_tree
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
            
        
            
            