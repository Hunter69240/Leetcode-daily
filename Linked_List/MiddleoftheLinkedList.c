#include <stdio.h>
#include <stdlib.h>

// Define the ListNode structure
struct ListNode {
    int val;                    // Value stored in the node
    struct ListNode *next;     // Pointer to the next node
};

// Function to print the linked list
void printList(struct ListNode* head) {
    while (head != NULL) {
        printf("%d", head->val);               // Print current node value
        if (head->next != NULL) printf(" -> "); // Add arrow if more nodes follow
        head = head->next;                      // Move to next node
    }
    printf("\n");
}

// Function to find the middle node of the linked list
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode* slow = head; // Moves one step at a time
    struct ListNode* fast = head; // Moves two steps at a time

    // Traverse the list until fast reaches the end
    while (fast && fast->next) {
        slow = slow->next;          // move slow one step
        fast = fast->next->next;    // move fast two steps
    }

    // When fast reaches the end, slow will be at the middle
    return slow;
}

int main() {
    // Manually allocate memory for 5 nodes
    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node2 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node3 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node4 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node5 = (struct ListNode*)malloc(sizeof(struct ListNode));

    // Assign values and link nodes to form: 1 -> 2 -> 3 -> 4 -> 5
    head->val = 1;
    head->next = node2;

    node2->val = 2;
    node2->next = node3;

    node3->val = 3;
    node3->next = node4;

    node4->val = 4;
    node4->next = node5;

    node5->val = 5;
    node5->next = NULL;

    // Print the original linked list
    printf("Linked List: ");
    printList(head);

    // Find and print the middle node
    struct ListNode* middle = middleNode(head);
    printf("Middle Node: %d\n", middle->val);

    return 0;
}
