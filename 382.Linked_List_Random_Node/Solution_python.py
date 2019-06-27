class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.nodes = []
        while head:
            self.nodes.append(head.val)
            head = head.next
        self.w = []
        self.acc =0
        for i in range(len(self.nodes)):
            self.acc+=1
            self.w.append(self.acc)
        
    def getRandom(self):
        """
        Returns a random node's value.
        """
        x = random.randint(1,self.acc)
        low = 0
        high = len(self.nodes)-1
        while low<high:
            mid = low+(high-low)//2
            if x>self.w[mid]:
                low = mid+1
            else:
                high = mid
        return self.nodes[low]
        
