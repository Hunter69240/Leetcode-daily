// This C program demonstrates the creation of a singly linked list from an array,
// prints the list, deletes the middle node from the list, and then prints the updated list.
// It also handles memory deallocation at the end.

// Include necessary header files
#include <stdio.h>
#include <stdlib.h>

// Definition of singly-linked list node
struct ListNode {
    int val;
    struct ListNode* next;
};

// Function to create a new node with a given value
struct ListNode* createNode(int val) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    return node;
}

// Function to create a linked list from a given array
struct ListNode* createListFromArray(int arr[], int size) {
    if (size == 0) return NULL;
    struct ListNode* head = createNode(arr[0]); // Create head node
    struct ListNode* current = head;
    for (int i = 1; i < size; i++) {
        current->next = createNode(arr[i]);     // Append new nodes
        current = current->next;
    }
    return head;
}

// Function to print the linked list
void printList(struct ListNode* head) {
    while (head != NULL) {
        printf("%d", head->val);                // Print current node value
        if (head->next != NULL)
            printf(" -> ");
        head = head->next;
    }
    printf("\n");
}

// Function to delete the middle node from the linked list
struct ListNode* deleteMiddle(struct ListNode* head) {
    int count = 0;
    struct ListNode* current = head;

    // Count total number of nodes
    while(current != NULL) {
        count++;
        current = current->next;
    }

    // If only one node, delete it by returning NULL
    if(count == 1){
        return NULL;
    }

    current = head;

    // Traverse to the node before the middle one
    for(int i = 1; i < count / 2; i++){
        current = current->next;
    }

    // Skip the middle node
    current->next = current->next->next;
    return head;
}

// Function to free all nodes in the linked list
void freeList(struct ListNode* head) {
    while (head != NULL) {
        struct ListNode* temp = head;
        head = head->next;
        free(temp);                             // Free each node
    }
}

int main() {
    int ad[] = {1, 3, 4, 7, 1, 2, 6};           // Input array
    int size = sizeof(ad) / sizeof(ad[0]);     // Get array size

    // Create linked list from array
    struct ListNode* head = createListFromArray(ad, size);

    // Print original list
    printf("Linked list: ");
    printList(head);

    // Delete the middle node
    head = deleteMiddle(head);

    // Print list after deletion
    printf("After deleting middle node: ");
    printList(head);

    // Free the memory used by the list
    freeList(head);

    return 0;
}
