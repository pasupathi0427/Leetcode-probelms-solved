# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2) :


        if list1==None:
            return list2

        if list2==None:
            return list1

        if list1==None and list2==None:
            return None
        
        dummy=ListNode(0)
        curr=dummy

        while list1 and list2:
            if (list1.val <= list2.val):
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next

            curr=curr.next
            if list1==None :
                curr.next=list2
            else:
                curr.next=list1

        return dummy.next


        
