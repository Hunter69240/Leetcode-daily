# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # value stored in node
        self.next = next      # pointer to next node


def cycleExists(head):
    
    # slow pointer moves 1 step
    # fast pointer moves 2 steps
    slow, fast = head, head.next

    # traverse list while fast pointer can move
    while fast and fast.next:

        # move pointers
        slow = slow.next
        fast = fast.next.next

        # if they meet → cycle exists
        if slow == fast:
            return True

    # fast reached end → no cycle
    return False


# Function to create linked list from array
def createLinkedList(arr):

    # if array empty
    if not arr:
        return None

    # create head node
    head = ListNode(arr[0])

    # pointer used to build list
    curr = head

    # store nodes in list for possible cycle creation
    nodes = [head]

    # build linked list
    for i in range(1, len(arr)):

        curr.next = ListNode(arr[i])  # create new node
        curr = curr.next              # move pointer
        nodes.append(curr)            # store node

    # currently NO cycle
    curr.next = None

    return head


# input array
arr = [3,2,0,-4]

# create linked list
head = createLinkedList(arr)

# check if cycle exists
print(cycleExists(head))