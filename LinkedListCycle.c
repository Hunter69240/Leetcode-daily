#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

// Function to print the linked list safely (up to some limit to avoid infinite loop)
void printList(struct ListNode* head) {
    int count = 0;
    while (head != NULL && count < 10) { // limit to avoid infinite loop
        printf("%d -> ", head->val);
        head = head->next;
        count++;
    }
    printf("...\n");  // indicates possible cycle
}

bool hasCycle(struct ListNode *head) {
    struct ListNode *slow = head;
    struct ListNode *fast = head;

    while (fast  && fast->next) {
        slow = slow->next;          
        fast = fast->next->next;   

        if (slow == fast) {         
            return true;
        }
    }
    return false; 

int main() {
    // Allocate memory for each node
    struct ListNode* node1 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node2 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node3 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node4 = (struct ListNode*)malloc(sizeof(struct ListNode));

    // Assign values
    node1->val = 3;
    node2->val = 2;
    node3->val = 0;
    node4->val = -4;

    // Link nodes: 3 -> 2 -> 0 -> -4
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;

    // Create the cycle: -4 -> 2
    node4->next = node2;

    // Print list (limited to avoid infinite loop)
    printf("Linked List (with cycle):\n");
    printList(node1);

    bool cycleExists = hasCycle(node1);
    printf("Cycle exists: %s\n", cycleExists ? "true" : "false");
    return 0;
}
