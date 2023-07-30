"""
141. Linked List Cycle

Given head, the head of a linked list, determine if 
the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in 
the list that can be reached again by continuously following 
the next pointer. Internally, pos is used to denote the index 
of the node that tail's next pointer is connected to. Note that 
pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise,
return false.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle1(head):
    existingNodes = []
    pos = head
    if head:
        while pos.next != None:
            if pos in existingNodes:
                return True
            else:
                existingNodes.append(pos)
            pos = pos.next
    return False

# Version 2 uses constant space in memory. Inefficient,
# not optimised.
def hasCycle2( head):
    pos = head
    if head:
        kang1 = pos
        kang2 = pos.next
        while kang2 != None:
            if kang1 == kang2:
                return True
            if kang2.next != None:
                kang2 = kang2.next
            else:
                return False
            if kang1 == kang2:
                return True
            if kang2.next != None:
                kang2 = kang2.next
            else:
                return False
            kang1 = kang1.next
    return False
