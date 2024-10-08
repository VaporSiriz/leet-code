# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, present_node = None, head
        while present_node:
            next_node = present_node.next
            present_node.next = prev_node
            prev_node, present_node = present_node, next_node
        return prev_node