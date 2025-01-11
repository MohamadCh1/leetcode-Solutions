# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = str(l1.val)
        s2 = str(l2.val)
        while(l1.next or l2 .next):
            if l1.next!=None:
                s1 = str(l1.next.val) + s1
                l1=l1.next
            if l2.next!=None:
                s2 = str(l2.next.val)+s2
                l2=l2.next
        s3 = str(int(s1)+int(s2))
        if len(s3)==1:
            return ListNode(int(s3),None)
        l1.val=int(s3[-1])
        l1.next=None
        l=l1
        for i in range(len(s3)-2,-1,-1):
            l.next=ListNode(int(s3[i]),None)
            l=l.next
        return l1