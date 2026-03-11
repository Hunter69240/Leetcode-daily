class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(arr):
    head = None
    tail = None

    for value in arr:
        node = ListNode(value)
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    return head


def print_list(head):
    while head:
        print(head.val, end=" → ")
        head = head.next
    print("None")


def add_two_numbers(l1, l2):
    stack_1 = []
    stack_2 = []
    res = None
    carry = 0

    # push digits of first number into stack_1
    while l1:
        stack_1.append(l1.val)
        l1 = l1.next

    # push digits of second number into stack_2
    while l2:
        stack_2.append(l2.val)
        l2 = l2.next

    # add digits while stacks are not empty or carry exists
    while stack_1 or stack_2 or carry != 0:
        if stack_1:
            num1 = stack_1.pop()
        else:
            num1 = 0

        if stack_2:
            num2 = stack_2.pop()
        else:
            num2 = 0

        total = carry + num1 + num2
        carry = total // 10
        digit = total % 10

        new_node = ListNode(digit)
        new_node.next = res
        res = new_node

        print_list(res)

    return res


l1_vals = [7, 2, 4, 3]
l2_vals = [5, 6, 4]

l1 = build_linked_list(l1_vals)
l2 = build_linked_list(l2_vals)

add_two_numbers(l1, l2)


# ---------------------------------------------------------
# EXPLANATION:
# This code adds two numbers represented as linked lists.
#
# Each linked list stores digits in FORWARD ORDER.
# Example:
#   l1 = 7 → 2 → 4 → 3   represents 7243
#   l2 = 5 → 6 → 4       represents 564
#
# The result must also be returned in forward order.
#
# Since addition happens from RIGHT to LEFT,
# we use STACKS to reverse the order of digits.
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY STACKS ARE USED:
# - Linked lists do not allow backward traversal
# - Addition needs to start from the least significant digit
# - Stacks reverse the traversal order
#
# stack_1 → digits of l1
# stack_2 → digits of l2
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# l1 = 7 → 2 → 4 → 3
# l2 = 5 → 6 → 4
#
# stack_1 = [7, 2, 4, 3]
# stack_2 = [5, 6, 4]
#
# carry = 0
# res = None
#
# -------------------------
# Iteration 1:
# pop 3 and 4
# total = 3 + 4 + 0 = 7
# digit = 7, carry = 0
# res = 7 → None
#
# -------------------------
# Iteration 2:
# pop 4 and 6
# total = 4 + 6 = 10
# digit = 0, carry = 1
# res = 0 → 7 → None
#
# -------------------------
# Iteration 3:
# pop 2 and 5
# total = 2 + 5 + 1 = 8
# digit = 8, carry = 0
# res = 8 → 0 → 7 → None
#
# -------------------------
# Iteration 4:
# pop 7 and 0
# total = 7 + 0 = 7
# digit = 7, carry = 0
# res = 7 → 8 → 0 → 7 → None
#
# -------------------------
# FINAL RESULT:
# 7 → 8 → 0 → 7 → None
#
# Which represents the number 7807
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n + m) where n and m are lengths of the two lists
#
# SPACE COMPLEXITY:
# O(n + m) due to stacks
# ---------------------------------------------------------
