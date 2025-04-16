from utils import *

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if head.next == None:
        return None
    current = head
    length = 0
    while current:
        length += 1
        current = current.next
    remove_pos = length - n
    if remove_pos == 0: return head.next
    print(f"remove_pos: {remove_pos}")
    prev, current, pos = ListNode(), head, 0
    while current:
        print(f"current.val: {current.val}")
        if pos == remove_pos:
            prev.next = current.next
            return head
        pos += 1
        prev = current
        current = current.next
    
head = create_linked_list([1,2])
new_head = removeNthFromEnd(head, 2)
print_linked_list(new_head)