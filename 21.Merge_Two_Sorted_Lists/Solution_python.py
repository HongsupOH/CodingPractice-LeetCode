class Solution:
    def mergeTwoLists(self, l1, l2):
        ans = ListNode(-1)
        dummy = ans
        while l1 and l2:
            if l1.val<l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return ans.next
