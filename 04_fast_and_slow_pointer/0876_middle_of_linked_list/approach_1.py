# add debug line for easy troubleshooting
from utils import *

def middleNode(head: Optional[ListNode]) -> ListNode:
    arr = linked_list_to_array(head)
    
    slow = head
    fast = head
    s_index, f_index = 0, 0
    print_list_with_indexes(arr, s=s_index, f=f_index)
    while fast and fast.next:
        slow = slow.next
        s_index += 1
        fast = fast.next.next
        f_index += 2
        print_list_with_indexes(arr, s=s_index, f=f_index)
        
    return slow
        

head = create_linked_list([1,2,3,4,5])
print_linked_list(head)