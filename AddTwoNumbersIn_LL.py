class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
def addTwoNumbers(head1: Node, head2: Node) -> Node:
    dummy = Node()
    temp = dummy
    carry = 0
    while (head1 or head2) or carry:
        res = 0
        if head1:
            res += head1.data
            head1 = head1.next 
        if head2:
            res += head2.data
            head2 = head2.next
        res += carry
        carry = res//10 
        node = Node(res%10)
        temp.next = node 
        temp = temp.next 
    return dummy.next
