from utils import *

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    prev, slow, fast = ListNode(), head, head
    s_index, f_index = 0, 0
    arr = linked_list_to_array(head)
    print_list_with_indexes(arr)
    
    for i in range(n):
        fast = fast.next
        f_index += 1
        print_list_with_indexes(arr, s = s_index, f=f_index)
        
    while fast:
        prev = slow
        fast = fast.next
        slow = slow.next
        s_index += 1
        f_index += 1
        
        print_list_with_indexes(arr, s = s_index, f=f_index)
    prev.next = slow.next
    if slow == head:
        return head.next
    return head
head = create_linked_list([1,2])
print_linked_list(removeNthFromEnd(head, 1))

    