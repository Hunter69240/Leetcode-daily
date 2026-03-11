/*
This C program removes all nodes from a sorted linked list that have duplicate values.  
Only distinct elements are retained in a new list, preserving their original order.  
It demonstrates dynamic memory allocation and linked list traversal with duplicate detection.
*/


#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list
struct ListNode {
    int val;
    struct ListNode *next;
};

// Function to print the linked list
void printList(struct ListNode* head) {
    while (head != NULL) {
        printf("%d", head->val);
        if (head->next != NULL)
            printf(" -> ");
        head = head->next;
    }
    printf("\n");
}

// Function to delete all nodes that have duplicate numbers
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode* newHead = NULL;  // Head of the new list
    struct ListNode* newTail = NULL;  // Tail of the new list
    struct ListNode* current = head;  // Pointer to traverse original list

    while (current != NULL) {
        int duplicate = 0;

        // Skip nodes with the same value
        while (current->next && current->val == current->next->val) {
            duplicate = 1;
            current = current->next;
        }

        // If current node is not part of any duplicate sequence
        if (!duplicate) {
            // Allocate new node and copy value
            struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
            newNode->val = current->val;
            newNode->next = NULL;

            // Add newNode to the result list
            if (!newHead) {
                newHead = newNode;
                newTail = newNode;
            } else {
                newTail->next = newNode;
                newTail = newNode;
            }
        }

        // Move to the next node
        current = current->next;
    }

    return newHead; // Return head of list with unique elements only
}

int main() {
    // Allocate and initialize nodes
    struct ListNode* node1 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node2 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node3 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node4 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node5 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node6 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node7 = (struct ListNode*)malloc(sizeof(struct ListNode));

    // Assign values
    node1->val = 1;
    node2->val = 1;
    node3->val = 1;
    node4->val = 2;
    node5->val = 3;
    node6->val = 4;
    node7->val = 4;

    // Link nodes together
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;
    node5->next = node6;
    node6->next = node7;
    node7->next = NULL;

    // Print original list
    printf("Original List: ");
    printList(node1);

    // Process list to remove duplicates
    struct ListNode* result = deleteDuplicates(node1);

    // Print updated list
    printf("After Removing Duplicates: ");
    printList(result);

    return 0;
}
