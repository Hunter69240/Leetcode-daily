#include <stdio.h>
#include <stdlib.h>

// 🔷 Topic: Linked List Manipulation and Addition
// 🔍 Problem: Add two numbers represented by linked lists where each node contains a single digit.
//             The digits are stored in reverse order. The function returns the sum as a new linked list.

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

// Function to add two numbers represented by linked lists
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* temp = NULL;  // Temporary list to store result in reverse order
    int carry = 0;  // To store carry during addition

    // Loop until both lists are exhausted and there's no carry left
    while (l1 || l2 || carry) {
        int sum = carry;  // Start with carry

        // Add l1 node value if it exists
        if (l1) {
            sum += l1->val;
            l1 = l1->next;
        }

        // Add l2 node value if it exists
        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }

        carry = sum / 10;  // Update carry for next digit

        // Create new node with the digit value
        struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = sum % 10;
        newNode->next = temp;  // Insert at head of temp list
        temp = newNode;
    }

    // Reverse the result list to get correct order
    struct ListNode* result = NULL;
    while (temp) {
        struct ListNode* nextNode = temp->next;
        temp->next = result;
        result = temp;
        temp = nextNode;
    }

    return result;
}

int main() {
    // Creating l1 = [2 -> 4 -> 3] which represents the number 342
    struct ListNode* l1_node3 = (struct ListNode*)malloc(sizeof(struct ListNode));
    l1_node3->val = 3;
    l1_node3->next = NULL;

    struct ListNode* l1_node2 = (struct ListNode*)malloc(sizeof(struct ListNode));
    l1_node2->val = 4;
    l1_node2->next = l1_node3;

    struct ListNode* l1_node1 = (struct ListNode*)malloc(sizeof(struct ListNode));
    l1_node1->val = 2;
    l1_node1->next = l1_node2;

    struct ListNode* l1 = l1_node1;

    // Creating l2 = [5 -> 6 -> 4] which represents the number 465
    struct ListNode* l2_node3 = (struct ListNode*)malloc(sizeof(struct ListNode));
    l2_node3->val = 4;
    l2_node3->next = NULL;

    struct ListNode* l2_node2 = (struct ListNode*)malloc(sizeof(struct ListNode));
    l2_node2->val = 6;
    l2_node2->next = l2_node3;

    struct ListNode* l2_node1 = (struct ListNode*)malloc(sizeof(struct ListNode));
    l2_node1->val = 5;
    l2_node1->next = l2_node2;

    struct ListNode* l2 = l2_node1;

    // Print both input lists
    printf("List l1: ");
    printList(l1);

    printf("List l2: ");
    printList(l2);

    // Call the function to add two numbers
    struct ListNode* result = addTwoNumbers(l1, l2);

    // Print the result list
    printf("Result List: ");
    printList(result);

    return 0;
}
