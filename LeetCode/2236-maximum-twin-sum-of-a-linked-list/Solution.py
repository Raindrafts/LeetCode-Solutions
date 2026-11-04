# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        slow=fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        prev = None
        curr = slow
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        p1=head
        p2=prev
        maxSum=0
        while p2 is not None:
            totalSum=p1.val+p2.val
            if totalSum>maxSum:
                maxSum=totalSum
            p1=p1.next
            p2=p2.next
        return maxSum