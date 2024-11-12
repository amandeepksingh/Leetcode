# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node_arr = []
        for l in lists:
            while l:
                node_arr.append(l.val)
                l = l.next
        sorted_list = ListNode()
        curr = sorted_list
        node_arr.sort()
        for n in node_arr:
            curr.next = ListNode(n)
            curr = curr.next
        return sorted_list.next

        