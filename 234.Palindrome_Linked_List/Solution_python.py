class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mid = head
        fast = head
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        
        inv = None
        while mid:
            cur = mid
            mid = mid.next
            cur.next = inv
            inv = cur
        while inv:
            if head.val!=inv.val:
                return False
            inv = inv.next
            head = head.next
        return True
