# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = head
        present = before.next if before else None
        after = present.next if present else None
        if before:
            before.next = None
        while present is not None:
            present.next = before
            before = present
            present = after
            after = after.next if after else None
        return before