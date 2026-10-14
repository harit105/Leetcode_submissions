# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # Handles edge cases:
        # 1. Empty list (head is None) -> fast is None, skips loop
        # 2. 1-node, no cycle -> fast.next is None, skips loop
        # 3. Even length end -> fast becomes None
        # 4. Odd length end  -> fast.next becomes None
        # 5. Short-circuit avoids AttributeError on None.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # Handles cycles (including single-node self-cycles)

            if slow == fast:
                return True
        return False        