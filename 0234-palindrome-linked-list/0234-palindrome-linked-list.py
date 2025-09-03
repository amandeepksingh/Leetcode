class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
    # When this loop ends:
    # slow points to the middle of the list.
    # fast is None (even length) or last node (odd length).
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

    # prev = slow → prev is now at middle.
    # slow = slow.next → move slow to start of 2nd half.
    # prev.next = None → cut the list into two halves.
        prev, slow, prev.next = slow, slow.next, None

    # traverse second half and create second reversed list 
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev

        # final comparison 
        while slow:
            if fast.val != slow.val: 
                return False
            fast, slow = fast.next, slow.next
        return True