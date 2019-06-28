class Solution:
    def swapPairs(self, head):
        """
        1->2->3->4, it becomes 2->1->4->3
        """
        cur = head
        while cur and cur.next:
            new = cur.next.val
            tmp = cur.val
            cur.val = new
            cur.next.val = tmp
            cur = cur.next.next
        return head
