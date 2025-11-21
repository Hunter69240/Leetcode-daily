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

int getDecimalValue(struct ListNode* head) {
    int result = 0;
    struct ListNode* current = head;

    // Traverse the linked list
    while (current != NULL) {
        // Shift result left by 1 (multiply by 2) and add current node's value
        result = (result << 1) | current->val;
        current = current->next; // Move to the next node
    }

    return result; // Return the final decimal value
    
}

int main() {
    // Create 3 nodes
    struct ListNode* node1 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node2 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* node3 = (struct ListNode*)malloc(sizeof(struct ListNode));

    // Assign values
    node1->val = 1;
    node2->val = 0;
    node3->val = 1;

    // Link the nodes: 1 -> 0 -> 1
    node1->next = node2;
    node2->next = node3;
    node3->next = NULL;

    // Print the linked list
    printf("Linked List: ");
    printList(node1);

    int a= getDecimalValue(node1);
    printf("Decimal Value: %d\n", a);
    return 0;
}
